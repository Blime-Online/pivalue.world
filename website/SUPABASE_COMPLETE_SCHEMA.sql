-- ============================================
-- Pi Value World - Complete Supabase Schema
-- ============================================
-- Run this ENTIRE SQL script in Supabase SQL Editor
-- Project: Pi Value World
-- Creator: Harinand Sindukumar (harinand@iths.online)
-- Website: https://iths.online
-- GitHub: https://github.com/harinandsindukumar/
-- ============================================

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================
-- 1. SUBMISSIONS TABLE
-- Stores all calculation submissions
-- ============================================
CREATE TABLE IF NOT EXISTS submissions (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    github_username VARCHAR(39) NOT NULL,
    verification_code VARCHAR(16) NOT NULL UNIQUE,
    submission_id VARCHAR(12) NOT NULL UNIQUE,
    time_limit INTEGER NOT NULL CHECK (time_limit IN (2, 5, 10)),
    calculations_performed BIGINT NOT NULL,
    precision_digits INTEGER NOT NULL,
    elapsed_seconds DECIMAL(10,2) NOT NULL,
    result TEXT,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'verified', 'rejected')),
    submitted_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    verified_at TIMESTAMP WITH TIME ZONE,
    verified_by VARCHAR(39),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for faster searches
CREATE INDEX idx_submissions_verification_code ON submissions(verification_code);
CREATE INDEX idx_submissions_submission_id ON submissions(submission_id);
CREATE INDEX idx_submissions_github_username ON submissions(github_username);
CREATE INDEX idx_submissions_status ON submissions(status);
CREATE INDEX idx_submissions_created_at ON submissions(created_at DESC);

-- ============================================
-- 2. CERTIFICATES TABLE
-- Stores generated certificates
-- ============================================
CREATE TABLE IF NOT EXISTS certificates (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    submission_id UUID NOT NULL REFERENCES submissions(id) ON DELETE CASCADE,
    certificate_url TEXT,
    certificate_image TEXT,
    certificate_data JSONB,
    download_count INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for certificate lookups
CREATE INDEX idx_certificates_submission_id ON certificates(submission_id);

-- ============================================
-- 3. COUNTER TABLE
-- Stores the global Pi counter value
-- ============================================
CREATE TABLE IF NOT EXISTS counter (
    id INTEGER PRIMARY KEY DEFAULT 1,
    value DECIMAL(10,2) DEFAULT 3.14,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Insert initial counter value
INSERT INTO counter (id, value) VALUES (1, 3.14) ON CONFLICT (id) DO NOTHING;

-- ============================================
-- 4. AUDIT_LOG TABLE
-- Tracks important actions
-- ============================================
CREATE TABLE IF NOT EXISTS audit_log (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id UUID,
    old_value JSONB,
    new_value JSONB,
    performed_by VARCHAR(39),
    performed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_audit_log_table_name ON audit_log(table_name);
CREATE INDEX idx_audit_log_record_id ON audit_log(record_id);

-- ============================================
-- FUNCTIONS AND TRIGGERS
-- ============================================

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger for submissions table
CREATE TRIGGER update_submissions_updated_at
    BEFORE UPDATE ON submissions
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Function to increment Pi counter
CREATE OR REPLACE FUNCTION increment_pi_counter()
RETURNS DECIMAL AS $$
DECLARE
    current_value DECIMAL;
    new_value DECIMAL;
BEGIN
    SELECT value INTO current_value FROM counter WHERE id = 1;
    new_value := current_value + 0.01;
    
    UPDATE counter SET value = new_value, updated_at = NOW() WHERE id = 1;
    
    RETURN new_value;
END;
$$ LANGUAGE plpgsql;

-- Function to verify submission (admin only)
CREATE OR REPLACE FUNCTION verify_submission(
    p_submission_id UUID,
    p_verified_by VARCHAR(39)
)
RETURNS BOOLEAN AS $$
DECLARE
    v_status VARCHAR(20);
BEGIN
    SELECT status INTO v_status FROM submissions WHERE id = p_submission_id;
    
    IF v_status != 'pending' THEN
        RAISE EXCEPTION 'Submission is not pending';
    END IF;
    
    UPDATE submissions 
    SET status = 'verified', 
        verified_at = NOW(),
        verified_by = p_verified_by
    WHERE id = p_submission_id;
    
    PERFORM increment_pi_counter();
    
    INSERT INTO audit_log (action, table_name, record_id, new_value, performed_by)
    VALUES ('verify', 'submissions', p_submission_id, '{"status": "verified"}', p_verified_by);
    
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Function to reject submission (admin only)
CREATE OR REPLACE FUNCTION reject_submission(
    p_submission_id UUID,
    p_verified_by VARCHAR(39),
    p_reason TEXT DEFAULT NULL
)
RETURNS BOOLEAN AS $$
BEGIN
    UPDATE submissions 
    SET status = 'rejected',
        verified_at = NOW(),
        verified_by = p_verified_by
    WHERE id = p_submission_id;
    
    INSERT INTO audit_log (action, table_name, record_id, new_value, performed_by)
    VALUES ('reject', 'submissions', p_submission_id, 
            '{"status": "rejected", "reason": "' || COALESCE(p_reason, '') || '"}', 
            p_verified_by);
    
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Function to create certificate for verified submission
CREATE OR REPLACE FUNCTION create_certificate_for_submission(
    p_submission_id UUID,
    p_certificate_image TEXT DEFAULT NULL
)
RETURNS UUID AS $$
DECLARE
    v_cert_id UUID;
    v_cert_data JSONB;
    v_submission RECORD;
BEGIN
    -- Get submission data
    SELECT * INTO v_submission FROM submissions WHERE id = p_submission_id;
    
    IF v_submission IS NULL THEN
        RAISE EXCEPTION 'Submission not found';
    END IF;
    
    IF v_submission.status != 'verified' THEN
        RAISE EXCEPTION 'Submission must be verified before certificate generation';
    END IF;
    
    -- Build certificate data
    v_cert_data := jsonb_build_object(
        'username', v_submission.github_username,
        'time_limit', v_submission.time_limit,
        'calculations', v_submission.calculations_performed,
        'precision', v_submission.precision_digits,
        'verification_code', v_submission.verification_code,
        'submission_id', v_submission.submission_id,
        'verified_date', v_submission.verified_at,
        'pi_value', (SELECT value FROM counter WHERE id = 1)
    );
    
    -- Insert certificate
    INSERT INTO certificates (
        submission_id,
        certificate_image,
        certificate_data
    ) VALUES (
        p_submission_id,
        p_certificate_image,
        v_cert_data
    ) RETURNING id INTO v_cert_id;
    
    RETURN v_cert_id;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- ============================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- ============================================

-- Enable RLS on all tables
ALTER TABLE submissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE certificates ENABLE ROW LEVEL SECURITY;
ALTER TABLE counter ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_log ENABLE ROW LEVEL SECURITY;

-- Submissions policies
CREATE POLICY "Public can view verified submissions"
    ON submissions FOR SELECT
    USING (status = 'verified');

CREATE POLICY "Anyone can create submissions"
    ON submissions FOR INSERT
    WITH CHECK (true);

-- Certificates policies
CREATE POLICY "Public can view certificates"
    ON certificates FOR SELECT
    USING (true);

-- Counter policies
CREATE POLICY "Public can view counter"
    ON counter FOR SELECT
    USING (true);

-- ============================================
-- VIEWS FOR COMMON QUERIES
-- ============================================

-- View for recent verified submissions
CREATE OR REPLACE VIEW recent_submissions AS
SELECT 
    id,
    github_username,
    verification_code,
    submission_id,
    time_limit,
    calculations_performed,
    precision_digits,
    elapsed_seconds,
    status,
    submitted_at
FROM submissions
WHERE status = 'verified'
ORDER BY submitted_at DESC
LIMIT 10;

-- View for submission statistics
CREATE OR REPLACE VIEW submission_stats AS
SELECT
    COUNT(*) as total_submissions,
    COUNT(*) FILTER (WHERE status = 'verified') as verified_count,
    COUNT(*) FILTER (WHERE status = 'pending') as pending_count,
    COUNT(*) FILTER (WHERE status = 'rejected') as rejected_count,
    COUNT(DISTINCT github_username) as unique_participants,
    MAX(calculations_performed) as max_calculations,
    AVG(calculations_performed) as avg_calculations
FROM submissions;

-- View for certificates with submission details
CREATE OR REPLACE VIEW certificate_details AS
SELECT 
    c.id,
    c.submission_id,
    s.github_username,
    s.time_limit,
    s.calculations_performed,
    s.precision_digits,
    s.verification_code,
    s.submission_id as short_id,
    s.verified_at,
    c.certificate_image,
    c.certificate_data,
    c.download_count,
    c.created_at
FROM certificates c
JOIN submissions s ON c.submission_id = s.id
WHERE s.status = 'verified';

-- ============================================
-- SAMPLE DATA (OPTIONAL - FOR TESTING)
-- ============================================

-- Uncomment to insert test data
/*
INSERT INTO submissions (
    github_username, verification_code, submission_id, 
    time_limit, calculations_performed, precision_digits, 
    elapsed_seconds, status, verified_at, verified_by
) VALUES 
    (
        'testuser1', 
        'A1B2C3D4E5F6G7H8', 
        'abc123def456',
        5,
        15000,
        1000,
        300.00,
        'verified',
        NOW(),
        'harinandsindukumar'
    );

-- Create certificate for test submission
SELECT create_certificate_for_submission(
    (SELECT id FROM submissions WHERE verification_code = 'A1B2C3D4E5F6G7H8'),
    'assets/certificate.png'
);
*/

-- ============================================
-- MAINTENANCE QUERIES
-- ============================================

-- Clean up old pending submissions (older than 30 days)
-- DELETE FROM submissions WHERE status = 'pending' AND created_at < NOW() - INTERVAL '30 days';

-- Vacuum and analyze tables
-- VACUUM ANALYZE submissions;
-- VACUUM ANALYZE certificates;

-- ============================================
-- SETUP COMPLETE!
-- ============================================
-- Your database is now ready to use.
-- Next steps:
-- 1. Test by inserting a submission
-- 2. Verify it using: SELECT verify_submission('submission-id', 'harinandsindukumar');
-- 3. Generate certificate: SELECT create_certificate_for_submission('submission-id');
-- 4. Query certificates: SELECT * FROM certificate_details;
-- ============================================

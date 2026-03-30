-- ============================================
-- Pi Value World - Supabase Database Schema
-- ============================================
-- 
-- Setup Instructions:
-- 1. Go to https://supabase.com and create a project
-- 2. Go to SQL Editor in your Supabase dashboard
-- 3. Copy and paste this entire schema
-- 4. Run the SQL to create all tables and policies
-- 5. Update website/js/supabase.js with your credentials
-- ============================================

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================
-- Table: submissions
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

-- Index for faster searches
CREATE INDEX idx_submissions_verification_code ON submissions(verification_code);
CREATE INDEX idx_submissions_submission_id ON submissions(submission_id);
CREATE INDEX idx_submissions_github_username ON submissions(github_username);
CREATE INDEX idx_submissions_status ON submissions(status);
CREATE INDEX idx_submissions_created_at ON submissions(created_at DESC);

-- ============================================
-- Table: certificates
-- Stores generated certificates
-- ============================================
CREATE TABLE IF NOT EXISTS certificates (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    submission_id UUID NOT NULL REFERENCES submissions(id) ON DELETE CASCADE,
    certificate_url TEXT,
    certificate_data JSONB,
    download_count INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for certificate lookups
CREATE INDEX idx_certificates_submission_id ON certificates(submission_id);

-- ============================================
-- Table: counter
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
-- Table: audit_log
-- Tracks important actions (optional)
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
-- Functions and Triggers
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
    -- Check current status
    SELECT status INTO v_status FROM submissions WHERE id = p_submission_id;
    
    IF v_status != 'pending' THEN
        RAISE EXCEPTION 'Submission is not pending';
    END IF;
    
    -- Update submission
    UPDATE submissions 
    SET status = 'verified', 
        verified_at = NOW(),
        verified_by = p_verified_by
    WHERE id = p_submission_id;
    
    -- Increment counter
    PERFORM increment_pi_counter();
    
    -- Log the action
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
    
    -- Log the action
    INSERT INTO audit_log (action, table_name, record_id, new_value, performed_by)
    VALUES ('reject', 'submissions', p_submission_id, 
            '{"status": "rejected", "reason": "' || COALESCE(p_reason, '') || '"}', 
            p_verified_by);
    
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- ============================================
-- Row Level Security (RLS) Policies
-- ============================================

-- Enable RLS on all tables
ALTER TABLE submissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE certificates ENABLE ROW LEVEL SECURITY;
ALTER TABLE counter ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_log ENABLE ROW LEVEL SECURITY;

-- Submissions policies
-- Anyone can read verified submissions
CREATE POLICY "Public can view verified submissions"
    ON submissions FOR SELECT
    USING (status = 'verified');

-- Allow insert for anyone (for new submissions)
CREATE POLICY "Anyone can create submissions"
    ON submissions FOR INSERT
    WITH CHECK (true);

-- Only authenticated users can update (for verification)
-- You'll need to implement authentication for this
-- CREATE POLICY "Admin can update submissions"
--     ON submissions FOR UPDATE
--     USING (auth.role() = 'authenticated');

-- Certificates policies
-- Anyone can read certificates
CREATE POLICY "Public can view certificates"
    ON certificates FOR SELECT
    USING (true);

-- Counter policies
-- Anyone can read counter
CREATE POLICY "Public can view counter"
    ON counter FOR SELECT
    USING (true);

-- Audit log policies
-- Only admins can read audit log (requires auth)
-- CREATE POLICY "Admin can view audit log"
--     ON audit_log FOR SELECT
--     USING (auth.role() = 'authenticated');

-- ============================================
-- Views for Common Queries
-- ============================================

-- View for recent submissions
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

-- ============================================
-- Sample Data (Optional - for testing)
-- ============================================

-- Uncomment to insert sample data
/*
INSERT INTO submissions (
    github_username, verification_code, submission_id, 
    time_limit, calculations_performed, precision_digits, 
    elapsed_seconds, status
) VALUES 
    (
        'testuser1', 
        'A1B2C3D4E5F6G7H8', 
        'abc123def456',
        5,
        15000,
        1000,
        300.00,
        'verified'
    ),
    (
        'testuser2',
        'X9Y8Z7W6V5U4T3S2',
        'xyz789ghi012',
        2,
        6000,
        1000,
        120.00,
        'pending'
    );
*/

-- ============================================
-- Maintenance Queries (Run Periodically)
-- ============================================

-- Clean up old pending submissions (older than 30 days)
-- DELETE FROM submissions WHERE status = 'pending' AND created_at < NOW() - INTERVAL '30 days';

-- Vacuum and analyze tables
-- VACUUM ANALYZE submissions;
-- VACUUM ANALYZE certificates;

-- ============================================
-- Backup and Restore Notes
-- ============================================
-- 
-- Supabase automatically backs up your database daily.
-- You can also:
-- 1. Use pg_dump for manual backups
-- 2. Export data via Supabase dashboard
-- 3. Use the API to backup data programmatically
-- 
-- ============================================

# 🥧 Pi Value World - Database Schema Documentation

**Project:** Pi Value World  
**Created by:** Harinand Sindukumar  
**Contact:** harinand@iths.online | https://iths.online  
**GitHub:** https://github.com/harinandsindukumar/

---

## 📊 Database Overview

This document describes the complete database schema for Pi Value World, hosted on Supabase (PostgreSQL).

### Database Purpose
- Store calculation submissions from users
- Track certificate generation
- Maintain global Pi counter (increments with each verified submission)
- Log audit trail of important actions
- Enable public verification of certificates

---

## 🗄️ Table Structures

### 1. **submissions** Table

Stores all Pi calculation submissions from users.

#### Columns:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | UUID | PRIMARY KEY, DEFAULT uuid_generate_v4() | Unique identifier for each submission |
| `github_username` | VARCHAR(39) | NOT NULL | User's GitHub username (max 39 chars) |
| `verification_code` | VARCHAR(16) | NOT NULL, UNIQUE | 16-character unique verification code |
| `submission_id` | VARCHAR(12) | NOT NULL, UNIQUE | 12-character unique submission ID |
| `time_limit` | INTEGER | NOT NULL, CHECK (2, 5, 10) | Selected time limit in minutes |
| `calculations_performed` | BIGINT | NOT NULL | Total number of calculations completed |
| `precision_digits` | INTEGER | NOT NULL | Number of decimal places calculated |
| `elapsed_seconds` | DECIMAL(10,2) | NOT NULL | Actual time spent calculating |
| `result` | TEXT | NULL | Full calculation result (optional) |
| `status` | VARCHAR(20) | DEFAULT 'pending', CHECK ('pending', 'verified', 'rejected') | Current verification status |
| `submitted_at` | TIMESTAMP WITH TIME ZONE | DEFAULT NOW() | When submission was created |
| `verified_at` | TIMESTAMP WITH TIME ZONE | NULL | When submission was verified |
| `verified_by` | VARCHAR(39) | NULL | Username of verifier/admin |
| `created_at` | TIMESTAMP WITH TIME ZONE | DEFAULT NOW() | Record creation timestamp |
| `updated_at` | TIMESTAMP WITH TIME ZONE | DEFAULT NOW() | Last update timestamp |

#### Indexes:
- `idx_submissions_verification_code` - Fast lookup by verification code
- `idx_submissions_submission_id` - Fast lookup by submission ID
- `idx_submissions_github_username` - Search by GitHub username
- `idx_submissions_status` - Filter by status
- `idx_submissions_created_at` - Recent submissions (DESC)

---

### 2. **certificates** Table

Stores generated certificates for verified submissions.

#### Columns:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | UUID | PRIMARY KEY, DEFAULT uuid_generate_v4() | Unique certificate identifier |
| `submission_id` | UUID | NOT NULL, FK → submissions(id) | Reference to submission |
| `certificate_url` | TEXT | NULL | URL/path to certificate file |
| `certificate_data` | JSONB | NULL | Certificate metadata and details |
| `download_count` | INTEGER | DEFAULT 0 | Number of times downloaded |
| `created_at` | TIMESTAMP WITH TIME ZONE | DEFAULT NOW() | Generation timestamp |

#### Indexes:
- `idx_certificates_submission_id` - Lookup by submission

#### Relationships:
- Foreign Key: `submission_id` → `submissions(id)` ON DELETE CASCADE

---

### 3. **counter** Table

Maintains the global Pi value counter that increments with each verified submission.

#### Columns:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY, DEFAULT 1 | Single row (id=1) |
| `value` | DECIMAL(10,2) | DEFAULT 3.14 | Current Pi counter value |
| `updated_at` | TIMESTAMP WITH TIME ZONE | DEFAULT NOW() | Last update timestamp |

#### Initial Data:
```sql
INSERT INTO counter (id, value) VALUES (1, 3.14) ON CONFLICT (id) DO NOTHING;
```

---

### 4. **audit_log** Table

Tracks important administrative actions for security and compliance.

#### Columns:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | UUID | PRIMARY KEY, DEFAULT uuid_generate_v4() | Unique log entry |
| `action` | VARCHAR(50) | NOT NULL | Action type (e.g., 'verify', 'reject') |
| `table_name` | VARCHAR(50) | NOT NULL | Affected table name |
| `record_id` | UUID | NULL | ID of affected record |
| `old_value` | JSONB | NULL | Previous values (for updates) |
| `new_value` | JSONB | NULL | New values (for inserts/updates) |
| `performed_by` | VARCHAR(39) | NULL | Username who performed action |
| `performed_at` | TIMESTAMP WITH TIME ZONE | DEFAULT NOW() | When action occurred |

#### Indexes:
- `idx_audit_log_table_name` - Filter by table
- `idx_audit_log_record_id` - Filter by record

---

## 🔧 Functions & Triggers

### 1. **update_updated_at_column()**

**Purpose:** Automatically update the `updated_at` timestamp on record modification.

**Returns:** TRIGGER

**Usage:**
```sql
CREATE TRIGGER update_submissions_updated_at
    BEFORE UPDATE ON submissions
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
```

---

### 2. **increment_pi_counter()**

**Purpose:** Increment the global Pi counter by 0.01.

**Returns:** DECIMAL (new value)

**Logic:**
1. Retrieve current counter value
2. Add 0.01 to value
3. Update counter table
4. Return new value

**Example:**
```sql
SELECT increment_pi_counter(); -- Returns 3.15, 3.16, etc.
```

---

### 3. **verify_submission(p_submission_id UUID, p_verified_by VARCHAR)**

**Purpose:** Verify a submission and increment counter (admin only).

**Parameters:**
- `p_submission_id` - Submission to verify
- `p_verified_by` - Username of verifier

**Returns:** BOOLEAN

**Logic:**
1. Check submission status is 'pending'
2. Update status to 'verified'
3. Set verified_at and verified_by
4. Call increment_pi_counter()
5. Log action in audit_log
6. Return TRUE

**Security:** SECURITY DEFINER (requires elevated privileges)

---

### 4. **reject_submission(p_submission_id UUID, p_verified_by VARCHAR, p_reason TEXT)**

**Purpose:** Reject a submission (admin only).

**Parameters:**
- `p_submission_id` - Submission to reject
- `p_verified_by` - Username of verifier
- `p_reason` - Optional rejection reason

**Returns:** BOOLEAN

**Logic:**
1. Update status to 'rejected'
2. Set verified_at and verified_by
3. Log action with reason in audit_log
4. Return TRUE

**Security:** SECURITY DEFINER

---

## 🔐 Row Level Security (RLS) Policies

### submissions Table

**Policy 1: Public can view verified submissions**
```sql
CREATE POLICY "Public can view verified submissions"
    ON submissions FOR SELECT
    USING (status = 'verified');
```
- Anyone can read verified submissions
- Pending/rejected submissions are private

**Policy 2: Anyone can create submissions**
```sql
CREATE POLICY "Anyone can create submissions"
    ON submissions FOR INSERT
    WITH CHECK (true);
```
- Allows anonymous submissions
- No authentication required

---

### certificates Table

**Policy: Public can view certificates**
```sql
CREATE POLICY "Public can view certificates"
    ON certificates FOR SELECT
    USING (true);
```
- All certificates publicly accessible
- Enables certificate verification

---

### counter Table

**Policy: Public can view counter**
```sql
CREATE POLICY "Public can view counter"
    ON counter FOR SELECT
    USING (true);
```
- Counter value visible to all users
- Website can display current Pi value

---

### audit_log Table

**Policy: Admin access only** (commented out by default)
```sql
-- CREATE POLICY "Admin can view audit log"
--     ON audit_log FOR SELECT
--     USING (auth.role() = 'authenticated');
```
- Requires authentication to view
- Currently disabled for development

---

## 📊 Views

### 1. **recent_submissions**

**Purpose:** Display 10 most recent verified submissions.

**Definition:**
```sql
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
```

**Usage:**
```sql
SELECT * FROM recent_submissions;
```

---

### 2. **submission_stats**

**Purpose:** Provide overall statistics about submissions.

**Definition:**
```sql
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
```

**Usage:**
```sql
SELECT * FROM submission_stats;
```

**Sample Output:**
```
total_submissions | verified_count | pending_count | rejected_count | unique_participants | max_calculations | avg_calculations
------------------+----------------+---------------+----------------+--------------------+------------------+-----------------
              150 |            120 |            25 |              5 |                 85 |           25000.0 |       12500.5
```

---

## 🚀 Setup Instructions

### Step 1: Create Supabase Project

1. Go to https://supabase.com
2. Sign up/Login
3. Create new project
4. Note your project URL and API key

### Step 2: Run Schema

1. Open SQL Editor in Supabase dashboard
2. Copy entire contents of `website/supabase-schema.sql`
3. Paste into SQL Editor
4. Click "Run" ▶️
5. Verify all tables created successfully

### Step 3: Verify Tables

Check Table Editor shows:
- ✅ submissions
- ✅ certificates
- ✅ counter (with initial value 3.14)
- ✅ audit_log

### Step 4: Test Insert

```sql
-- Test submission
INSERT INTO submissions (
    github_username, verification_code, submission_id,
    time_limit, calculations_performed, precision_digits,
    elapsed_seconds, status
) VALUES (
    'testuser',
    'TEST123456789ABC',
    'test123456789',
    5,
    15000,
    1000,
    300.00,
    'pending'
);

-- Verify counter
SELECT * FROM counter; -- Should show 3.14

-- Test counter increment
SELECT increment_pi_counter(); -- Should return 3.15
```

---

## 📈 Query Examples

### Get Submission by Code
```sql
SELECT * FROM submissions 
WHERE verification_code = 'A1B2C3D4E5F6G7H8';
```

### Get Recent Verified Submissions
```sql
SELECT * FROM recent_submissions;
```

### Get Statistics
```sql
SELECT * FROM submission_stats;
```

### Verify a Submission
```sql
SELECT verify_submission(
    'submission-uuid-here',
    'harinandsindukumar'
);
```

### Get Current Pi Value
```sql
SELECT value FROM counter WHERE id = 1;
```

### Search by Username
```sql
SELECT * FROM submissions 
WHERE github_username = 'harinandsindukumar'
ORDER BY created_at DESC;
```

---

## 🔒 Security Considerations

1. **RLS Enabled:** All tables have Row Level Security
2. **Public Read:** Only verified data is publicly readable
3. **Insert Allowed:** Anyone can submit, but requires verification
4. **Admin Functions:** verify_submission() and reject_submission() use SECURITY DEFINER
5. **Audit Trail:** All admin actions logged in audit_log

---

## 📦 Maintenance

### Regular Tasks

**Weekly:**
- Review pending submissions
- Clean up spam (if any)

**Monthly:**
```sql
-- Clean old pending submissions (> 30 days)
DELETE FROM submissions 
WHERE status = 'pending' 
AND created_at < NOW() - INTERVAL '30 days';

-- Update statistics
VACUUM ANALYZE submissions;
VACUUM ANALYZE certificates;
```

**Backup:**
- Supabase provides automatic daily backups
- Export via dashboard regularly
- Use pg_dump for manual backups

---

## 📞 Support

**Database Administrator:** Harinand Sindukumar  
**Email:** harinand@iths.online  
**Website:** https://iths.online  
**GitHub:** https://github.com/harinandsindukumar/

---

**Last Updated:** March 30, 2024  
**Schema Version:** 1.0  
**Project:** Pi Value World

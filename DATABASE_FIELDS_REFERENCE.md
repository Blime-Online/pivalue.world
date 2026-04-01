# 📊 Complete Database Fields Reference

## submissions Table - All Fields

When a user runs `piclalculation.py`, ALL these fields are inserted into the database:

### Field-by-Field Breakdown

| Field Name | Type | Example | Description | When Set |
|------------|------|---------|-------------|----------|
| `id` | UUID | `a1b2c3d4-e5f6-...` | Auto-generated unique ID | Always (auto) |
| `github_username` | VARCHAR(39) | `"Blime-Online"` | User's GitHub username | Script run |
| `verification_code` | VARCHAR(16) | `"A1B2C3D4E5F6G7H8"` | 16-char unique code | Script run |
| `submission_id` | VARCHAR(12) | `"abc123def456"` | 12-char unique ID | Script run |
| `time_limit` | INTEGER | `5` | Chosen time (2/5/10 min) | Script run |
| `calculations_performed` | BIGINT | `13245` | Total calculations done | Script run |
| `precision_digits` | INTEGER | `1000` | Decimal places achieved | Script run |
| `elapsed_seconds` | DECIMAL | `120.45` | Actual time spent | Script run |
| `result` | TEXT | `"3.142857..."` | Full calculation result | Script run |
| `status` | VARCHAR | `"pending"` | **pending** → **verified** | Script → Actions |
| `submitted_at` | TIMESTAMP | `"2025-04-01T12:34:56Z"` | When calculation done | Script run |
| `verified_at` | TIMESTAMP | `NULL` → timestamp | When PR merged | NULL → Actions |
| `verified_by` | VARCHAR | `NULL` → `"GitHub Actions..."` | Who verified | NULL → Actions |
| `created_at` | TIMESTAMP | Auto | Record creation | Always (auto) |
| `updated_at` | TIMESTAMP | Auto | Last update | Always (auto) |

---

## certificates Table - All Fields

Created automatically after verification:

| Field Name | Type | Example | Description |
|------------|------|---------|-------------|
| `id` | UUID | Auto | Unique certificate ID |
| `submission_id` | UUID | Links to submissions.id | Foreign key |
| `certificate_url` | TEXT | `https://pivalue.iths.online/certificate.html?id=...` | Web link |
| `certificate_image` | TEXT | URL to PNG | Certificate image (optional) |
| `certificate_data` | JSONB | `{...}` | Complete submission data |
| `download_count` | INTEGER | `0` | Times downloaded |
| `created_at` | TIMESTAMP | Auto | When created |

---

## counter Table - Single Row

Global Pi counter that increments with each verification:

| Field Name | Type | Default | Current Value |
|------------|------|---------|---------------|
| `id` | INTEGER | `1` | `1` |
| `value` | DECIMAL | `3.14` | `3.14 + (0.01 × verifications)` |
| `updated_at` | TIMESTAMP | Auto | Last update time |

---

## 🔄 Data Flow Timeline

### Phase 1: Script Run (User's Computer)

```python
# piclalculation.py generates:
{
    "github_username": "Blime-Online",
    "time_limit": 5,
    "calculations_performed": 13245,
    "precision_digits": 1000,
    "elapsed_seconds": 300.45,
    "verification_code": "A1B2C3D4E5F6G7H8",
    "submission_id": "abc123def456",
    "result": "3.142857142857...",
    "timestamp": "2025-04-01T12:34:56.789Z"
}
```

**Database Insert (PENDING):**
```sql
INSERT INTO submissions (
    github_username,      -- "Blime-Online"
    verification_code,    -- "A1B2C3D4E5F6G7H8"
    submission_id,        -- "abc123def456"
    time_limit,           -- 5
    calculations_performed, -- 13245
    precision_digits,     -- 1000
    elapsed_seconds,      -- 300.45
    result,               -- "3.142857142857..."
    status,               -- "pending" ← IMPORTANT!
    submitted_at,         -- "2025-04-01T12:34:56Z"
    verified_by,          -- NULL
    verified_at           -- NULL
)
```

---

### Phase 2: After PR Merge (GitHub Actions)

**Database Update:**
```sql
UPDATE submissions 
SET 
    status = 'verified',
    verified_at = '2025-04-03T14:20:00Z',
    verified_by = 'GitHub Actions (PR merge)'
WHERE submission_id = 'abc123def456'
```

**Certificate Created:**
```sql
INSERT INTO certificates (
    submission_id,
    certificate_url,
    certificate_data,
    download_count
) VALUES (
    (SELECT id FROM submissions WHERE submission_id = 'abc123def456'),
    'https://pivalue.iths.online/certificate.html?id=abc123def456',
    {complete_submission_json},
    0
)
```

**Counter Incremented:**
```sql
UPDATE counter 
SET value = value + 0.01,
    updated_at = NOW()
WHERE id = 1
```

---

## 🔍 Search Queries

Users can search by:

### 1. Submission ID
```sql
SELECT * FROM submissions 
WHERE submission_id = 'abc123def456';
```

### 2. Verification Code
```sql
SELECT * FROM submissions 
WHERE verification_code = 'A1B2C3D4E5F6G7H8';
```

### 3. GitHub Username
```sql
SELECT * FROM submissions 
WHERE github_username = 'Blime-Online';
```

---

## 📊 Status Lifecycle

```
pending ──────────────→ verified
   │                        │
   │                        │
Script run              PR merged
Upload to GitHub       GitHub Actions
Create PR              Sync complete
```

**Status Values:**
- `pending` - Initial state (user ran script)
- `verified` - After PR merge (GitHub Actions)
- `rejected` - Manual rejection by maintainer (rare)

---

## 💡 Important Notes

### Data Integrity

✅ **All JSON fields mapped to DB columns**  
✅ **Type casting ensures correct format** (int, float, string)  
✅ **No data loss during sync**  
✅ **Complete audit trail** (timestamps, verified_by)  

### Search Optimization

Indexes exist on:
- `submission_id` (unique)
- `verification_code` (unique)
- `github_username`
- `status`

### Security

- Service role key required for inserts
- Row Level Security (RLS) can be enabled
- No sensitive personal data stored
- All submissions are public

---

## 🎯 For Developers

### Querying Pending Submissions

```sql
-- Get all pending submissions awaiting PR merge
SELECT * FROM submissions 
WHERE status = 'pending'
ORDER BY submitted_at DESC;
```

### Querying Verified Submissions

```sql
-- Get all verified submissions
SELECT * FROM submissions 
WHERE status = 'verified'
ORDER BY verified_at DESC;
```

### Count Statistics

```sql
-- Total submissions
SELECT COUNT(*) FROM submissions;

-- Verified count
SELECT COUNT(*) FROM submissions WHERE status = 'verified';

-- Pending count
SELECT COUNT(*) FROM submissions WHERE status = 'pending';
```

---

This ensures **ALL data** from the JSON file is preserved in the database at every step! 🎉

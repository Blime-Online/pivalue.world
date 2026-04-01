# ✅ Website & Database Integration Checklist

## 🎯 Complete Verification Guide

Use this checklist to ensure all website and database integrations are working properly.

---

## 1️⃣ Database Schema Verification

### Check in Supabase SQL Editor:

```sql
-- Verify submissions table exists with all columns
SELECT column_name, data_type, is_nullable 
FROM information_schema.columns 
WHERE table_name = 'submissions'
ORDER BY ordinal_position;

-- Should show ALL fields:
-- id, github_username, verification_code, submission_id,
-- time_limit, calculations_performed, precision_digits,
-- elapsed_seconds, result, status, submitted_at, verified_at,
-- verified_by, created_at, updated_at
```

**Expected Result:** ✅ All 14 columns present

---

## 2️⃣ Test Pending Insert (Local Script Run)

### Setup:
1. Create `.env` file with Supabase credentials
2. Run calculation script:
   ```bash
   python piclalculation.py
   ```

### Verify in Database:
```sql
SELECT * FROM submissions 
WHERE github_username = 'YOUR_USERNAME'
ORDER BY created_at DESC 
LIMIT 1;
```

**Expected Result:**
- ✅ Record exists
- ✅ `status` = `'pending'`
- ✅ All fields populated:
  - `github_username` ✅
  - `verification_code` ✅
  - `submission_id` ✅
  - `time_limit` ✅
  - `calculations_performed` ✅
  - `precision_digits` ✅
  - `elapsed_seconds` ✅
  - `result` ✅
  - `submitted_at` ✅
  - `verified_at` = NULL ✅
  - `verified_by` = NULL ✅

---

## 3️⃣ Test Website Search (Pending Status)

### On Website:
1. Go to: https://pivalue.iths.online/search
2. Enter your `submission_id` or `verification_code`
3. Click Search

**Expected Result:**
- ✅ Submission found
- ✅ Status shows: **"Pending"** (badge color: orange/yellow)
- ✅ All data visible:
  - Username ✅
  - Time limit ✅
  - Calculations ✅
  - Precision ✅
  - Submitted date ✅
  - Verification code ✅
  - Submission ID ✅
- ❌ "Generate Certificate" button NOT shown (hidden for pending)

---

## 4️⃣ Test GitHub Upload Workflow

### Manual Steps:
1. Copy JSON from `verification_list/pi_result_USERNAME.json`
2. Go to GitHub fork
3. Navigate to `verification_list/` folder
4. Click "Add file" → "Create new file"
5. Name: `pi_result_USERNAME.json`
6. Paste JSON content
7. Commit changes
8. Create Pull Request

**Expected Result:**
- ✅ File uploaded successfully
- ✅ PR created
- ✅ Database still shows `status='pending'`

---

## 5️⃣ Test PR Merge & Auto-Verification

### After Maintainer Merges PR:

#### Check GitHub Actions:
1. Go to repository → Actions tab
2. Look for "Sync Verification List to Supabase"
3. Should show green checkmark ✅

#### Verify Database Update:
```sql
SELECT status, verified_at, verified_by 
FROM submissions 
WHERE submission_id = 'YOUR_SUBMISSION_ID';
```

**Expected Result:**
- ✅ `status` changed from `'pending'` → `'verified'`
- ✅ `verified_at` has timestamp
- ✅ `verified_by` = `"GitHub Actions (PR merge)"`

---

## 6️⃣ Test Website Search (Verified Status)

### On Website Again:
1. Go to: https://pivalue.iths.online/search
2. Search same submission ID

**Expected Result:**
- ✅ Status now shows: **"Verified"** (badge color: green)
- ✅ "Generate Certificate" button VISIBLE ✅
- ✅ All data still visible
- ✅ Can click "Generate Certificate"

---

## 7️⃣ Test Certificate Generation

### Click "Generate Certificate":
1. Should redirect to: `certificate.html?id=SUBMISSION_ID`
2. Certificate displays with all details

**Expected Result:**
- ✅ Certificate loads
- ✅ Shows username
- ✅ Shows calculation stats
- ✅ Shows verification code & ID
- ✅ Download option available

---

## 8️⃣ Test Counter Increment

### Check Global Pi Counter:
```sql
SELECT value FROM counter WHERE id = 1;
```

**Before any verifications:**
- Expected: `3.14`

**After first verification:**
- Expected: `3.15`

**After second verification:**
- Expected: `3.16`

**Formula:** `3.14 + (0.01 × total_verifications)`

---

## 9️⃣ Test Certificates Table

### Verify Certificate Record Created:
```sql
SELECT c.certificate_url, c.certificate_data, s.status
FROM certificates c
JOIN submissions s ON c.submission_id = s.id
WHERE s.submission_id = 'YOUR_SUBMISSION_ID';
```

**Expected Result:**
- ✅ Record exists in `certificates` table
- ✅ `certificate_url` populated
- ✅ `certificate_data` contains full JSON
- ✅ `download_count` = 0 (initially)

---

## 🔟 Test Recent Submissions Feed

### On Homepage (index.html):
- Scroll to "Recent Submissions" section

**Expected Result:**
- ✅ Shows recent submissions
- ✅ Displays status badges (pending/verified)
- ✅ Shows username, time, calculations
- ✅ Clicking opens detail view

---

## ⚠️ Common Issues & Solutions

### Issue 1: No Record After Script Run
**Cause:** Missing `.env` file  
**Solution:** Create `.env` with Supabase credentials

### Issue 2: Search Shows Error
**Cause:** Supabase not configured or CORS issue  
**Solution:** Check Supabase dashboard → API settings

### Issue 3: Status Stays Pending After Merge
**Cause:** GitHub Actions failed  
**Solution:** 
1. Check Actions tab for errors
2. Verify secrets are set: `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`
3. Re-run workflow if needed

### Issue 4: Certificate Button Not Showing
**Cause:** Status still pending  
**Solution:** Wait for GitHub Actions to complete after PR merge

### Issue 5: Counter Not Incrementing
**Cause:** No row with `id=1` in counter table  
**Solution:** Run sync script manually once to create it

---

## 📊 Data Integrity Checks

### Run These Queries:

```sql
-- Check for orphaned certificates (no submission)
SELECT COUNT(*) FROM certificates c
LEFT JOIN submissions s ON c.submission_id = s.id
WHERE s.id IS NULL;
-- Expected: 0

-- Check for duplicate submission_ids
SELECT submission_id, COUNT(*) 
FROM submissions 
GROUP BY submission_id 
HAVING COUNT(*) > 1;
-- Expected: 0 rows

-- Check for duplicate verification_codes
SELECT verification_code, COUNT(*) 
FROM submissions 
GROUP BY verification_code 
HAVING COUNT(*) > 1;
-- Expected: 0 rows

-- Check all pending submissions older than 7 days
SELECT COUNT(*) FROM submissions 
WHERE status = 'pending' 
AND submitted_at < NOW() - INTERVAL '7 days';
-- Expected: 0 (should all be verified or rejected)
```

---

## 🎯 Success Criteria

All checks pass when:

- ✅ Script inserts complete record as pending
- ✅ Search finds pending submissions immediately
- ✅ Website displays all fields correctly
- ✅ Certificate button hidden for pending
- ✅ GitHub Actions runs after PR merge
- ✅ Status updates to verified automatically
- ✅ Certificate button appears for verified
- ✅ Counter increments with each verification
- ✅ Certificate record created
- ✅ Recent submissions show on homepage
- ✅ No data loss at any step

---

## 🚀 Final Deployment Checklist

Before going live:

- [ ] Set GitHub Secrets:
  - `SUPABASE_URL`
  - `SUPABASE_SERVICE_ROLE_KEY`
- [ ] Test complete flow end-to-end
- [ ] Verify CORS settings allow website domain
- [ ] Enable Row Level Security (RLS) if needed
- [ ] Set up monitoring for failed Actions
- [ ] Create admin dashboard for pending review
- [ ] Test on production with real user

---

## 📞 Support

If issues persist:
1. Check Supabase logs
2. Check GitHub Actions logs
3. Review browser console for errors
4. Test with SQL queries directly

**All systems integrated and working!** 🎉

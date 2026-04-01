# 📋 Verification List

**This is where you submit your Pi Value World calculation results!**

---

## How to Submit

### Step 1: Run Calculation
```bash
python piclalculation.py
# Complete the challenge
# Get your Verification Code and Submission ID
```

### Step 2: Copy Your Result File
After running, you'll have a file like:
- `pi_result_yourusername.json`

### Step 3: Add to This Folder
Copy or move your result file into the `verification_list/` folder.

### Step 4: Create Pull Request
1. Commit the file
2. Push to your fork
3. Open PR on GitHub
4. Include your codes in PR description

### Step 5: Wait for Merge
Once merged, website automatically:
- Scans this folder
- Validates your codes
- Generates certificate
- Updates status to "Verified"

---

## What Gets Verified

Your JSON file should contain:
- ✅ github_username
- ✅ verification_code (16 chars)
- ✅ submission_id (12 chars)
- ✅ time_limit
- ✅ calculations_performed
- ✅ precision_digits
- ✅ timestamp

---

## After Merge

Visit: https://pivalue.iths.online/search
- Search your Submission ID
- View verified record
- Download certificate!

---

**Questions?** See [HOW_IT_WORKS.md](../HOW_IT_WORKS.md)

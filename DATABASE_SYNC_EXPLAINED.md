# 📊 When Does Your Data Get Into Database?

## ⚠️ IMPORTANT: Understanding the Workflow

Many users are confused about when their submission appears in the database. Here's the complete flow:

---

## 🔄 Complete Timeline

### Step 1: Run Python Script (You do this)
```bash
python piclalculation.py
```

**What happens:**
- ✅ JSON file created on YOUR computer
- ✅ File saved to: `verification_list/pi_result_YOUR_USERNAME.json`
- ❌ **NOT in database yet!**

**Status:** Local file only

---

### Step 2: Upload to GitHub (You do this)
```
1. Go to your fork on GitHub
2. Navigate to verification_list/ folder
3. Create new file
4. Paste JSON content
5. Commit changes
```

**What happens:**
- ✅ File now on GitHub
- ❌ **Still NOT in database!**

**Status:** File on GitHub, waiting for review

---

### Step 3: Create Pull Request (You do this)
```
1. Click "Pull requests" tab
2. Click "New pull request"
3. Select your branch
4. Create PR
```

**What happens:**
- ✅ PR submitted for review
- ❌ **Still NOT in database!**

**Status:** Pending review

---

### Step 4: PR Merged (Maintainer does this)
```
1. Maintainer reviews your PR
2. Approves and merges to main branch
```

**What happens:**
- ✅ Your file is now in main repository
- ❌ **Still NOT in database... YET!**

**Status:** Merged, triggers automation

---

### Step 5: GitHub Actions Runs (Automatic!)
```
Trigger: Push to main branch (verification_list/)
Action: Runs sync_supabase.py script
```

**What happens:**
- ✅ Script reads your JSON file
- ✅ Connects to Supabase database
- ✅ Inserts record into `submissions` table
- ✅ Creates certificate record
- ✅ Updates global counter

**Status:** ✅ **NOW IN DATABASE!**

---

### Step 6: Search Works (Automatic!)
```
Website: https://pivalue.iths.online/search
```

**What happens:**
- ✅ Website queries Supabase database
- ✅ Finds your submission by ID
- ✅ Shows verified status
- ✅ Certificate available for download

**Status:** ✅ **PUBLIC AND SEARCHABLE!**

---

## ⏱️ Timeline Summary

| Step | Who | Time | Database? |
|------|-----|------|-----------|
| 1. Run script | You | 2-10 min | ❌ NO |
| 2. Upload to GitHub | You | 2 min | ❌ NO |
| 3. Create PR | You | 2 min | ❌ NO |
| 4. Wait for merge | You | 1-3 days | ❌ NO |
| 5. PR merged | Maintainer | 5 min | ❌ NO |
| 6. **GitHub Actions** | **Automatic** | **2-5 min** | **✅ YES!** |
| 7. Search works | Automatic | Instant | ✅ YES |

**Total time:** 1-3 days + 5 minutes

---

## 🔍 Why This Process?

### Security
- ✅ Prevents spam submissions
- ✅ Human review before database
- ✅ Validates JSON format
- ✅ Prevents fake results

### Quality Control
- ✅ Ensures proper formatting
- ✅ Checks for duplicates
- ✅ Verifies calculation data
- ✅ Maintains database integrity

### Automation
- ✅ No manual database work needed
- ✅ Syncs automatically after merge
- ✅ Creates certificates instantly
- ✅ Updates counter automatically

---

## ❓ Common Questions

### Q: "I ran the script but search doesn't find me?"

**A:** That's normal! You need to:
1. Upload JSON to GitHub ✅
2. Create Pull Request ✅
3. Wait for merge ✅
4. GitHub Actions runs ✅

**Only then** will search find you!

---

### Q: "My PR was merged 10 minutes ago, still not found?"

**A:** Check GitHub Actions:
1. Go to repository → Actions tab
2. Look for "Sync Verification List to Supabase"
3. Is it ✅ green (success)? Then you're in!
4. Is it ❌ red (failed)? Maintainer needs to fix

Usually takes 2-5 minutes after merge.

---

### Q: "Can I skip the PR and go straight to database?"

**A:** **NO!** The PR review is required for:
- Security (prevents spam)
- Validation (checks your data)
- Fairness (everyone follows same process)

---

### Q: "How do I know if GitHub Actions ran?"

**A:** Check the Actions tab:
1. Go to: https://github.com/YOUR_USERNAME/pivalue.world/actions
2. Look for workflow: "Sync Verification List to Supabase"
3. Green checkmark = Success! You're in database
4. Red X = Failed, contact maintainer

---

## 🎯 Visual Flow

```
┌─────────────────────┐
│  You run script     │ → File on YOUR computer
│  (piclalculation.py)│   ❌ Not in database
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Upload to GitHub   │ → File on GitHub
│  (manual upload)    │   ❌ Not in database
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Create PR          │ → Waiting for review
│  (pull request)     │   ❌ Not in database
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  PR Merged          │ → In main repository
│  (by maintainer)    │   ❌ Not in database
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  GitHub Actions     │ → Runs sync script
│  (AUTOMATIC!)       │   ✅ SYNCING NOW!
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Database Record    │
│  ✅ INSERTED!       │
│  - submissions      │
│  - certificates     │
│  - counter updated  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Website Search     │
│  ✅ WORKS!          │
│  Find by ID         │
│  Download cert      │
└─────────────────────┘
```

---

## 💡 Pro Tips

### For Users:
1. ✅ Save your Submission ID and Verification Code
2. ✅ Screenshot your calculation results
3. ✅ Watch for PR merge notification
4. ✅ Check Actions tab after merge
5. ✅ Search website 10 minutes after merge

### For Maintainers:
1. ✅ Monitor Actions tab for failed runs
2. ✅ Check Supabase secrets are set correctly
3. ✅ Review PRs promptly (don't make users wait)
4. ✅ Re-run failed workflows if needed

---

## 🛠️ Troubleshooting

### If database record NOT created after merge:

**Check these:**
1. ✅ GitHub Actions ran successfully
2. ✅ SUPABASE_URL secret is set
3. ✅ SUPABASE_SERVICE_ROLE_KEY secret is set
4. ✅ JSON file has valid format
5. ✅ Network connection working

**Fix:**
- Go to Actions tab
- Click failed workflow
- Read error logs
- Fix issue (usually missing secrets)
- Click "Re-run jobs"

---

## 📞 Need Help?

If stuck:
1. Check [README.md](README.md) for workflow
2. Check [QUICKSTART.md](QUICKSTART.md) for steps
3. View [Actions tab](https://github.com/harinandsindukumar/pivalue.world/actions) for errors
4. Create GitHub issue with details

---

**Remember: Database record = AFTER merge + GitHub Actions run!** ⚡

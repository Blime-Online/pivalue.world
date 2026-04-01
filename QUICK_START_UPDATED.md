# 🥧 Pi Value World - Updated Quick Start Guide

**Including Auto-Submit Helper!**

---

## 🚀 Quick Start (Updated)

### Step 1: Fork & Clone Repository

```bash
# 1. Fork this repo on GitHub
# 2. Then clone your fork:
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
cd pivalue.world
```

### Step 2: Run Calculation Script

```bash
cd src
python piclalculation.py
```

**Requirements:**
- Python 3.6 or higher
- No external dependencies required!

### Step 3: Follow Prompts & Get Codes

1. Enter your GitHub username
2. Choose time limit (2, 5, or 10 minutes)
3. Let script calculate 22/7 repeatedly
4. **Save your Verification Code and Submission ID!**

Script will:
- ✅ Create JSON file in root folder
- ✅ AUTO-ADD to verification_list/ folder
- ✅ Display your unique codes

### Step 4: Submit to GitHub (CHOOSE METHOD!)

#### METHOD A - Automatic (RECOMMENDED ⭐)

```bash
# From root folder
python src/auto_submit.py
```

**What it does automatically:**
- ✅ Finds your submission file
- ✅ Adds to git
- ✅ Commits with proper message
- ✅ Pushes to your forked repository
- ✅ Shows PR creation instructions

**One command = Everything done!**

#### METHOD B - Manual (Traditional)

```bash
# From root folder
git add verification_list/
git commit -m "Add Pi Value World submission for YOUR_USERNAME"
git push
```

**For git experts who want control.**

### Step 5: Create Pull Request

**After submitting to GitHub:**

1. Go to your fork on GitHub
2. Click "Contribute" → "Open Pull Request"
3. Use title: `feat: add submission for YOUR_USERNAME`
4. Include details from your JSON file
5. Create PR!

### Step 6: After Merge - Get Certificate!

**Once maintainer merges your PR:**

- ✅ Website auto-verifies your submission
- ✅ Status: Not Verified → VERIFIED
- ✅ Pi counter increases (+0.01)
- ✅ Certificate generated automatically!

**Download at:** https://pivalue.iths.online/search

---

## 📋 Complete Documentation

### Main Guides:

1. **[README.md](README.md)** - Project overview
2. **[COMPLETE_USER_GUIDE.md](COMPLETE_USER_GUIDE.md)** - Comprehensive guide
3. **[HOW_IT_WORKS.md](HOW_IT_WORKS.md)** - Visual walkthrough
4. **[WORKFLOW_GUIDE_COMPLETE.md](WORKFLOW_GUIDE_COMPLETE.md)** - Full 6-step process
5. **[EASY_SUBMISSION_GUIDE.md](EASY_SUBMISSION_GUIDE.md)** ⭐ - Auto-submit guide

### Quick References:

- **[src/README.md](src/README.md)** - Python scripts instructions
- **[verification_list/README.md](verification_list/README.md)** - Submission folder info
- **[REPO_STRUCTURE.md](REPO_STRUCTURE.md)** - Folder organization

---

## 💡 Pro Tips

### For Beginners:
- ✅ Use auto-submit (`python src/auto_submit.py`) - easiest!
- ✅ Take screenshot of your codes
- ✅ Keep your JSON file safe
- ✅ Follow guided steps

### For Git Experts:
- ✅ Manual method gives full control
- ✅ Customize commit messages
- ✅ Traditional workflow

### For Everyone:
- ✅ Close other programs before calculation
- ✅ Choose longer time for impressive certificate
- ✅ Don't modify the calculation script
- ✅ Write good PR description

---

## ❓ Common Questions

### Q: Which submission method should I use?
**A:** Auto-submit is recommended for beginners! Both work perfectly.

### Q: Do I need to install anything for auto-submit?
**A:** No! It's pure Python, no dependencies.

### Q: What if auto-submit fails?
**A:** Use manual method as backup. Both achieve same result.

### Q: How long until I get certificate?
**A:** Usually 1-3 days after PR merge.

### Q: Does Pi counter really increase?
**A:** YES! Every merged PR adds +0.01 to displayed value.

---

## 🎯 Workflow Summary

```
1. FORK              → GitHub
2. CLONE             → Computer
3. RUN               → python src/piclalculation.py
                     → AUTO-ADDS to verification_list/
4. SUBMIT            → CHOOSE ONE:
                     
   Method A (Easy):  → python src/auto_submit.py
                     → DONE! (commits & pushes)
                     
   Method B (Manual):→ git add verification_list/
                     → git commit -m "..."
                     → git push
5. CREATE PR         → On GitHub
6. AFTER MERGE       → Auto-verify → Certificate!
```

---

**Ready to start? Pick your method and go! 🚀**

*Created by Harinand Sindukumar*  
*Contact: harinand@iths.online*  
*Domain: https://pivalue.iths.online*

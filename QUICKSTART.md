# 🥧 Pi Value World - Quick Start Guide

**Get started in 5 minutes or less!**

---

## For Participants (Want to earn a certificate?)

### Step 0: Fork the Repository (DO THIS FIRST!)

**⚠️ IMPORTANT: Fork BEFORE cloning!**

1. Go to: https://github.com/harinandsindukumar/pivalue.world
2. Click "Fork" button (top right corner)
3. GitHub creates YOUR copy at: `https://github.com/YOUR_USERNAME/pivalue.world`

**Why fork first?** You need your own copy to push branches to!

### Step 1: Clone YOUR Fork (NOT the Original!)

**⚠️ Clone YOUR forked repository, NOT the original!**

```bash
# Replace YOUR_USERNAME with YOUR actual GitHub username
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
cd pivalue.world
```

**Example for @Blime-Online:**
```bash
git clone https://github.com/Blime-Online/pivalue.world.git
cd pivalue.world
```

**❌ WRONG - Don't clone the original repo:**
```bash
# DON'T do this (can't push to harinandsindukumar's repo):
git clone https://github.com/harinandsindukumar/pivalue.world.git
```

**✅ CORRECT - Clone YOUR own fork:**
```bash
# DO this (clone your own fork where you have write access):
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
```

Don't have Git? [Download here](https://git-scm.com/)

Or download as ZIP from YOUR fork on GitHub and extract.

### Step 2: Create Your Branch (DO THIS IMMEDIATELY!)

**RIGHT after cloning, create your submission branch:**

```bash
# Go into the repository folder
cd pivalue.world

# Create and switch to your submission branch
git checkout -b submission/YOUR_USERNAME-timestamp
```

**Example:**
```bash
cd pivalue.world
git checkout -b submission/harinandsindukumar-1711812345
```

**⚠️ CRITICAL:** Do this BEFORE running any scripts!
**❌ NEVER work on main branch!**

### Step 3: Run the Script (2-10 minutes)

```bash
python piclalculation.py
```

**No Python?** Download from [python.org](https://www.python.org/)

### Step 4: Get Your Codes

The script will ask you:

1. **Enter GitHub username**
   - Type your GitHub username exactly
   - Example: `harinandsindukumar`

2. **Select time limit**
   - Press `1` for 2 minutes
   - Press `2` for 5 minutes  
   - Press `3` for 10 minutes

3. **Wait for calculation**
   - Watch it calculate 22/7 repeatedly
   - See your PC's performance in real-time
   - Can stop early with Ctrl+C if needed

4. **Save your codes**
   - **Verification Code**: 16 characters (e.g., `A1B2C3D4E5F6G7H8`)
   - **Submission ID**: 12 characters (e.g., `abc123def456`)
   - **IMPORTANT**: Screenshot or write these down!

### Step 5: Submit for Verification (1 minute)

**BEFORE submitting, verify you're on your branch:**

```bash
# Check current branch
git branch
# Should show: * submission/yourname-timestamp
```

**If you accidentally ran the script from main branch:**
```bash
# Create your submission branch now
git checkout -b submission/YOUR_USERNAME-timestamp
```

Then continue with submission.

### Step 6: PR Review and Merge (2 minutes)

**IMPORTANT: You should already be on your submission branch!**

1. After calculation finishes, locate `pi_result_{username}.json`.
2. Add this file to the repository verification list: `verification_list/`.
3. **Verify you're on correct branch:**
   ```bash
   git branch
   # Should show: * submission/yourname-timestamp
   ```
4. Run: `python submit_now.py`
   - This adds, commits, and pushes your files.
5. Create a Pull Request on GitHub.

### Step 6: PR Review and Merge (2 minutes)

1. Go to GitHub repository
2. You'll see your pushed branch
3. Click "Pull requests" → "New pull request"
4. Select: `base: main ← compare: your-branch`
5. Fill in PR description with your codes
6. Wait for approval

### Step 7: Get Your Certificate! (After approval)

Once your PR is merged:

1. Visit the website: [https://pivalue.world](https://pivalue.world)
2. Search for your Submission ID
3. Download your certificate (PNG or PDF)
4. Share on your GitHub profile!

---

## Total Time Required

- **Setup**: 2 minutes
- **Calculation**: 2-10 minutes (your choice)
- **Submission**: 3 minutes
- **Total**: 7-15 minutes

---

## What You'll Need

✅ Python 3.6+ (5 min to install)
✅ Git (optional, can use ZIP)
✅ GitHub account (free)
✅ 10-15 minutes of time

---

## Common Questions

**Q: Is this free?**
A: Yes, completely free!

**Q: Can I do this multiple times?**
A: Once per time limit (2min, 5min, 10min)

**Q: What if I make a mistake?**
A: Just run the script again!

**Q: How long does approval take?**
A: Usually 1-3 days

**Q: Can I use any computer?**
A: Yes! Use your own hardware only.

**Q: What if script doesn't run?**
A: Check Python is installed correctly. See SETUP_GUIDE.md

---

## Troubleshooting

### "python is not recognized"

**Windows:**
```bash
py piclalculation.py
```

Or add Python to PATH.

**Mac/Linux:**
```bash
python3 piclalculation.py
```

### "ModuleNotFoundError"

Install required package:
```bash
pip install pyperclip
```

(Only needed if you want clipboard features)

### Script runs but shows errors

Check:
- Python version: `python --version`
- You're in correct directory: `cd pivalue.world`
- File exists: `ls` or `dir`

---

## Tips for Best Results

1. **Close other programs** - More CPU power = more calculations
2. **Use longer time** - 10 minutes = more impressive certificate
3. **Don't modify script** - Results won't verify
4. **Save codes immediately** - Can't recover if lost
5. **Screenshot results** - Backup proof of your calculation

---

## Next Steps After First Certificate

- Try different time limits
- Compete with friends
- Add certificate to GitHub README
- Star the repository ⭐
- Share on social media

---

## Need Help?

📖 **Full Guide**: See README.md
🔧 **Setup Issues**: See SETUP_GUIDE.md
🐛 **Bugs**: Create GitHub issue
💬 **Questions**: GitHub Discussions

---

## Ready to Start?

```bash
python piclalculation.py
```

Good luck! 🥧

---

*Remember: The goal is fun and learning. Enjoy the challenge!*

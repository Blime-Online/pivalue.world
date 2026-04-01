# 🥧 Pi Value World - How It Works

**Complete workflow from fork to certificate!**

**Domain:** https://pivalue.iths.online  
**Repository:** https://github.com/harinandsindukumar/pivalue.world

---

## 🎯 The Complete Workflow (7 Simple Steps)

```
USER JOURNEY:
Fork Repo → Clone → Create Branch (FIRST!) → Run Script → Get Codes → Add to Verification → PR → Certificate!
```

---

## Step 1: Fork the Repository

**What to do:**
1. Go to https://github.com/harinandsindukumar/pivalue.world
2. Click "Fork" button (top right)
3. Wait for GitHub to create your copy

**Why fork?**
- You get your own copy of the project
- You can make changes without affecting main repo
- You can submit your results via Pull Request

---

## Step 2: Clone Your Fork

**On your computer:**

```bash
# Replace YOUR_USERNAME with your GitHub username
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
cd pivalue.world
```

**What this does:**
- Downloads the repository to your computer
- You now have all files locally
- Ready to run the calculation script!

---

## Step 3: Create Your Branch (DO THIS IMMEDIATELY!)

**⚠️ CRITICAL: Create your branch RIGHT AFTER cloning, BEFORE running any scripts!**

**Navigate into the repository:**
```bash
cd pivalue.world
```

**Create and switch to submission branch:**
```bash
git checkout -b submission/YOUR_USERNAME-timestamp
```

**Example:**
```bash
cd pivalue.world
git checkout -b submission/harinandsindukumar-1711812345
```

**Why create branch NOW?**
- ✅ Best Git workflow practice
- ✅ Prevents accidental commits to main
- ✅ Keeps repository organized
- ✅ Required for submission acceptance
- ✅ Makes PR creation easier

**Verify you're on correct branch:**
```bash
git branch
```
The `*` should show `submission/yourname`, NOT `main`.

**⚠️ WARNING:** If you accidentally run scripts from main branch, create your branch now and continue!

---

## Step 4: Run the Calculation File

**In your terminal:**

```bash
python piclalculation.py
```

**What happens next:**

### A. Enter Your GitHub Username
```
Enter your GitHub username: harinandsindukumar
```

### B. Choose Time Limit
```
Select time limit:
1. 2 minutes
2. 5 minutes
3. 10 minutes

Enter choice (1/2/3): 2
```

### C. Watch the Magic Happen
```
🔢 Starting calculation for 2 minute(s)...
⏳ Press Ctrl+C to stop early

⚡ Calculations: 1000 | Elapsed: 45.23s
⚡ Calculations: 2000 | Elapsed: 90.45s
...
```

### D. Get Your Important Codes!
```
============================================================
🎉 Calculation Complete!
============================================================
👤 GitHub Username: @harinandsindukumar
⏱️  Time Limit: 2 minute(s)
⚡ Actual Time: 120.00 seconds
🔢 Total Calculations: 13,245
📊 Precision Achieved: 1000 decimal places

🎫 Your Verification Code: A1B2C3D4E5F6G7H8
🆔 Your Submission ID: abc123def456

💾 Results saved to: pi_result_harinandsindukumar.json
============================================================
```

**🚨 IMPORTANT: Save these codes!**
- Take a screenshot
- Write them down
- Don't lose them!

**You now have:**
1. ✅ Result file: `pi_result_harinandsindukumar.json`
2. ✅ Verification Code: `A1B2C3D4E5F6G7H8` (16 chars)
3. ✅ Submission ID: `abc123def456` (12 chars)

---

## Step 5: Create Your Branch (REQUIRED!)

**⚠️ CRITICAL: You MUST create a new branch before submitting!**

**Why branches are required:**
- Keeps main branch clean and stable
- Standard GitHub contribution workflow
- Makes pull request review easier
- Required for submission acceptance
- Prevents conflicts with other submissions

**Create and switch to a submission branch:**

```bash
# Replace YOUR_USERNAME with your actual username
git checkout -b submission/YOUR_USERNAME-timestamp
```

**Example:**
```bash
git checkout -b submission/harinandsindukumar-1711812345
```

**Check your current branch:**
```bash
git branch
```

The `*` shows your current branch. Make sure you're NOT on `main`!

**⚠️ IMPORTANT:** The `submit_now.py` script will check that you're on a branch (not main) before proceeding!

---

## Step 6: Add to Verification Folder

**Navigate to verification folder:**

```bash
cd verification_list
```

**Copy your result file:**

```bash
# From root folder
cp pi_result_harinandsindukumar.json verification_list/
```

**Or manually:**
1. Find your file: `pi_result_yourusername.json`
2. Copy it
3. Paste into `verification_list/` folder

**What's in the file?**
```json
{
  "github_username": "harinandsindukumar",
  "time_limit": 2,
  "calculations_performed": 13245,
  "precision_digits": 1000,
  "verification_code": "A1B2C3D4E5F6G7H8",
  "submission_id": "abc123def456",
  "result": "3.142857142857...",
  "timestamp": "2024-03-30T..."
}
```

---

## Step 7: Create Pull Request

**Go to GitHub:**

1. Navigate to your forked repo
2. You'll see "This branch is X commits ahead"
3. Click "Contribute" → "Open Pull Request"

**Fill in PR details:**

**Title:**
```
feat: add submission for harinandsindukumar
```

**Description:**
```markdown
## My Pi Value World Submission

**GitHub Username:** @harinandsindukumar  
**Time Limit:** 2 minutes  
**Calculations Performed:** 13,245  
**Precision:** 1000 digits  

**Verification Code:** A1B2C3D4E5F6G7H8  
**Submission ID:** abc123def456  

I have completed the Pi Value World challenge! 
Please verify and merge my submission.

Thank you! 🥧
```

**Click:** "Create Pull Request"

**What happens next:**
- Maintainer gets notified
- They review your submission
- Check codes are valid
- If everything OK → Merge!

---

## Step 8: Website Verifies & Generates Certificate

### Automatic Process:

**After PR is merged:**

1. **Website Scans Verification Folder**
   - System detects new file in `verification_list/`
   - Reads your Submission ID and Verification Code

2. **Validation Check**
   - Checks if codes match format
   - Verifies not duplicate
   - Confirms calculation data is valid

3. **Status Update**
   - Changes from: ❌ "Not Verified"
   - Changes to: ✅ "Verified"

4. **Certificate Generation**
   - Beautiful certificate created automatically
   - Includes all your details
   - Ready to download!

### You Can Now:

**Visit Website:** https://pivalue.iths.online/search

**Search for your submission:**
- Enter your Submission ID: `abc123def456`
- Or Verification Code: `A1B2C3D4E5F6G7H8`

**Your Record Shows:**
```
✅ Status: Verified
👤 Username: @harinandsindukumar
⏱️ Time Limit: 2 minute(s)
🔢 Calculations: 13,245
📊 Precision: 1000 digits
🎫 Code: A1B2C3D4E5F6G7H8
🆔 ID: abc123def456
```

**Actions Available:**

1. **Download Certificate**
   - Click "📥 Download PNG"
   - High-quality A4 certificate
   - Includes your logo, username, all details

2. **Get Shareable Link**
   - Click "🔗 Copy Link"
   - URL like: `https://pivalue.iths.online/certificate.html?id=abc123def456`
   - Add to GitHub profile, LinkedIn, etc.

3. **Share on Social Media**
   - Twitter/X button
   - LinkedIn button
   - Show off your achievement!

---

## 🎨 What Your Certificate Looks Like

```
                    [PI VALUE WORLD LOGO]
                    
              Certificate of Achievement
              
                  Pi Value World Challenge
                  
            This is to certify that
            
                 @harinandsindukumar
                 
    has successfully completed the Pi Value World Challenge
    
    ┌─────────────┬─────────────┬─────────────┐
    │ Time Limit  │Calculations │  Precision  │
    │  2 minute(s)│   13,245    │  1000 digits│
    └─────────────┴─────────────┴─────────────┘
    
              Verification Details
              
    Verification Code: A1B2C3D4E5F6G7H8
    Submission ID: abc123def456
    Verified on: March 30, 2024
    
    _______________________________________
    Authorized by Pi Value World Team
    
    Pi Value World | https://pivalue.iths.online
```

**Certificate includes:**
- ✅ Your GitHub username
- ✅ Time limit chosen
- ✅ Number of calculations
- ✅ Precision achieved
- ✅ Verification code
- ✅ Submission ID
- ✅ Verification date
- ✅ Pi Value World logo
- ✅ Professional design (yellow/black/white)
- ✅ Official seal

---

## 🔄 Status Flow (Visual Guide)

```
┌──────────────────┐
│  1. Not Started  │  ← Before running script
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  2. Running      │  ← Script calculating 22/7
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  3. Got Codes    │  ← Have ID + Code
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  4. Added to     │  ← In verification_list/
│     Verify List  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  5. PR Created   │  ← Waiting for merge
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  6. PR Merged    │  ✅ Approved by maintainer
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  7. Auto Scan    │  🔍 Website detects submission
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  8. Validated    │  ✅ Codes verified
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  9. VERIFIED!    │  🎉 Status changed!
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ 10. Certificate  │  🎓 Ready to download!
│     Generated    │
└──────────────────┘
```

---

## 🔍 Search & View All Submissions

**Anyone can search:**

1. Go to: https://pivalue.iths.online/search
2. Enter any Submission ID or Verification Code
3. See complete details

**What you'll find:**
- All verified submissions
- Usernames and results
- Calculation stats
- Certificate links

**Filter by status:**
- ✅ Verified (green badge)
- ⏳ Pending (yellow badge)
- ❌ Rejected (red badge)

---

## 📊 Live Statistics on Website

**Homepage shows:**

- **Current Pi Value:** 3.14, 3.15, 3.16... (increments with each verified submission!)
- **Total Submissions:** Count of all submissions
- **Verified Certificates:** How many earned certificates
- **Active Participants:** Unique users
- **Recent Submissions:** Latest entries

---

## 🎯 Why This Workflow?

### Benefits:

✅ **Simple & Clear:**
- Just 6 steps
- No complicated setup
- Anyone can follow

✅ **Transparent:**
- All submissions public in verification_list/
- Anyone can verify codes
- Open process

✅ **Secure:**
- Manual review via PR
- Anti-cheat validation
- Duplicate prevention

✅ **Automatic:**
- Website scans automatically
- Certificate generation instant
- No manual work needed

✅ **Educational:**
- Learn Git/GitHub workflow
- Understand PR process
- Practice open source contribution

---

## 💡 Pro Tips

### For Best Results:

1. **Close other programs** before running script
   - More CPU power = more calculations
   
2. **Choose longer time** for impressive certificate
   - 10 minutes = more calculations than 2 minutes
   
3. **Don't modify script**
   - Results won't verify
   - Will be rejected in PR review
   
4. **Save codes immediately**
   - Screenshot the output
   - Can't recover if lost
   
5. **Check JSON file** before submitting
   - Verify all fields correct
   - Username matches GitHub
   
6. **Write good PR description**
   - Include all details
   - Makes review faster

---

## ❓ Common Questions

### Q: Can I participate multiple times?
**A:** Yes! Once per time limit (2min, 5min, 10min). Each gives different certificate.

### Q: What if I close script early?
**A:** Still works! Results based on actual calculation time. May affect certificate quality.

### Q: How long does verification take?
**A:** Usually 1-3 days after PR is merged. Website scans automatically.

### Q: Can I edit my submission?
**A:** No. If mistake, create new PR with new codes.

### Q: Is it free?
**A:** Completely free! No hidden costs.

### Q: Do I need programming experience?
**A:** No! Just follow the steps. Very beginner-friendly.

---

## 🎉 Summary

**The Complete Flow:**

1. **Fork** → Get your copy on GitHub
2. **Clone** → Download to your computer
3. **Run** → Execute `piclalculation.py`
4. **Get Codes** → Save ID + Verification Code
5. **Add to verification_list/** → Put file in folder
6. **PR** → Create Pull Request
7. **Merge** → Maintainer approves
8. **Scan** → Website detects automatically
9. **Verify** → Codes validated
10. **Certificate!** → Download and share!

**That's it! Simple, clear, and automatic! 🚀**

---

**Ready to start?**  
Go to: https://github.com/harinandsindukumar/pivalue.world

**Questions?**  
Email: harinand@iths.online

**Good luck! 🥧**

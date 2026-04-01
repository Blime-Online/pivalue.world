# 🥧 Pi Value World - Complete User Guide

**Consistent 7-Step Workflow Across All Documentation**

---

## ⚠️ IMPORTANT: Consistency Notice

**All official guides now use the SAME consistent workflow:**

```
1. FORK    → Fork repository on GitHub
2. CLONE   → Clone YOUR fork to computer  
3. BRANCH  → Create submission branch (DO THIS FIRST!)
4. RUN     → Execute piclalculation.py
5. GET     → Receive ID + Code (JSON file)
6. VERIFY  → Add to verification_list/ + PR
7. CERTIFY → Website auto-verifies → Certificate!
```

**Domain:** https://pivalue.iths.online  
**Repository:** https://github.com/harinandsindukumar/pivalue.world

---

## 📋 The Official 7-Step Process

### Step 1: Fork the Repository

**On GitHub:**
1. Go to: https://github.com/harinandsindukumar/pivalue.world
2. Click "Fork" button (top right corner)
3. Wait for GitHub to create your copy

**Why fork?**
- You get your own copy of the project
- You can make changes without affecting main repo
- Standard open source contribution workflow

---

### Step 2: Clone Your Fork

**On your computer:**

```bash
# Replace YOUR_USERNAME with your actual GitHub username
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
cd pivalue.world
```

**What this does:**
- Downloads the repository to your computer
- You now have all files locally
- Ready to run the calculation script!

---

### Step 3: Create Your Branch (DO THIS IMMEDIATELY AFTER CLONING!)

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

**⚠️ WARNING:** If you run scripts from main branch, you'll need to:
1. Create your branch now: `git checkout -b submission/yourname`
2. Continue with the workflow

---

### Step 4: Run the Calculation Script

**In your terminal/command prompt:**

```bash
python piclalculation.py
```

**The script will:**

#### A. Ask for your GitHub username:
```
Enter your GitHub username: harinandsindukumar
```

#### B. Let you choose time limit:
```
Select time limit:
1. 2 minutes
2. 5 minutes  
3. 10 minutes

Enter choice (1/2/3): 2
```

#### C. Calculate 22/7 repeatedly:
```
🔢 Starting calculation for 2 minute(s)...
⏳ Press Ctrl+C to stop early

⚡ Calculations: 1000 | Elapsed: 45.23s
⚡ Calculations: 2000 | Elapsed: 90.45s
...
```

#### D. Give you TWO IMPORTANT codes:
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

**🚨 CRITICAL: Save these codes!**
- Take a screenshot
- Write them down somewhere safe
- You'll need both codes for verification

---

### Step 5: Create Your Branch (REQUIRED!)

**⚠️ CRITICAL: You MUST create a new branch before submitting!**

**Create and switch to a submission branch:**

```bash
# Replace YOUR_USERNAME with your actual username
git checkout -b submission/YOUR_USERNAME-timestamp
```

**Example:**
```bash
git checkout -b submission/harinandsindukumar-1711812345
```

**Why branches are required:**
- ✅ Keeps main branch clean and stable
- ✅ Standard GitHub contribution workflow
- ✅ Makes pull request review easier
- ✅ Required for submission acceptance
- ✅ Prevents conflicts with other submissions

**Check your current branch:**
```bash
git branch
```

The current branch will have a `*` next to it. Make sure you're NOT on `main`!

**⚠️ WARNING:** If you try to run `submit_now.py` from main branch, it will warn you and refuse to proceed!

---

### Step 6: Add to Verification List

**Navigate to verification folder:**

```bash
cd verification_list
```

**Copy your result file:**

```bash
# From root folder
cp ../pi_result_harinandsindukumar.json .
```

**Or manually:**
1. Find your file: `pi_result_yourusername.json`
2. Copy it
3. Paste into `verification_list/` folder

**What's in the JSON file?**
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

### Step 7: Create Pull Request

**Go to GitHub:**

1. Navigate to your forked repo:
   ```
   https://github.com/YOUR_USERNAME/pivalue.world
   ```

2. You'll see: "This branch is X commits ahead"

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

### Step 6: Get Your Certificate!

**After your PR is merged:**

#### Automatic Process:
1. **Website scans** `verification_list/` automatically
2. **Validates** your Submission ID + Verification Code
3. **Updates status:** ❌ Not Verified → ✅ Verified
4. **Generates certificate** instantly!

#### Download Your Certificate:

1. Visit: https://pivalue.iths.online/search

2. Search for your submission:
   - Enter Submission ID: `abc123def456`
   - OR Verification Code: `A1B2C3D4E5F6G7H8`

3. Your record shows:
   ```
   ✅ Status: Verified
   👤 Username: @harinandsindukumar
   ⏱️ Time Limit: 2 minutes
   🔢 Calculations: 13,245
   📊 Precision: 1000 digits
   🎫 Code: A1B2C3D4E5F6G7H8
   🆔 ID: abc123def456
   ```

4. **Actions available:**
   - 📥 **Download PNG** - High-quality A4 certificate
   - 🔗 **Copy Link** - Shareable URL for profiles
   - 📱 **Share** - Twitter/LinkedIn buttons

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
    │  2 minutes  │   13,245    │  1000 digits│
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
- ✅ Time limit chosen (2/5/10 minutes)
- ✅ Number of calculations performed
- ✅ Precision achieved (decimal places)
- ✅ Verification code (16 characters)
- ✅ Submission ID (12 characters)
- ✅ Verification date
- ✅ Pi Value World logo
- ✅ Professional yellow/black/white design
- ✅ Official seal and signature

---

## 🔄 Visual Workflow Diagram

```
USER SIDE:                          SYSTEM SIDE:
┌─────────────┐                     
│ 1. FORK     │  → On GitHub       
└─────────────┘                     
         ↓                          
┌─────────────┐                     
│ 2. CLONE    │  → To computer     
└─────────────┘                     
         ↓                          
┌─────────────┐                     
│ 3. CREATE   │  → git checkout -b 
│    BRANCH   │     submission/... 
│   (FIRST!)  │  DO BEFORE SCRIPTS!
└─────────────┘                     
         ↓                          
┌─────────────┐                     
│ 4. RUN      │  → piclalculation.py
└─────────────┘                     
         ↓                          
┌─────────────┐                     
│ 5. GET      │  → Codes + JSON    
└─────────────┘                     
         ↓                          
┌─────────────┐                     
│ 6. ADD to   │  → verification_/  
│  verify_list│                    
└─────────────┘                     
         ↓                          
┌─────────────┐                     
│ 7. CREATE   │  → On GitHub       
│     PR      │                    
└─────────────┘                     
         ↓                          
                                    ┌─────────────┐
                                    │ PR MERGED   │
                                    └─────────────┘
                                           ↓
                                    ┌─────────────┐
                                    │ AUTO SCAN   │
                                    └─────────────┘
                                           ↓
                                    ┌─────────────┐
                                    │ VALIDATE    │
                                    └─────────────┘
                                           ↓
                                    ┌─────────────┐
                                    │ STATUS      │
                                    │ UPDATED     │
                                    └─────────────┘
                                           ↓
                                    ┌─────────────┐
                                    │ CERTIFICATE │
                                    │ GENERATED   │
                                    └─────────────┘
                                           ↓
                                    ┌─────────────┐
                                    │ DOWNLOAD!   │
                                    └─────────────┘
```

---

## 📊 Status Flow

### Submission Status Progression:

```
Before running script:     (No record exists)
          ↓
After running script:      (JSON file created)
          ↓
Added to verify_list:      ⏳ Pending (not yet merged)
          ↓
PR submitted:              ⏳ Pending (awaiting review)
          ↓
PR merged:                 ⏳ Pending (website scan pending)
          ↓
Website validates:         ✅ VERIFIED!
          ↓
Certificate generated:     🎉 Ready to download!
```

### Status Badges on Website:

- 🟢 **Verified** (Green) - Certificate available
- 🟡 **Pending** (Yellow) - Waiting for PR merge or website scan
- 🔴 **Rejected** (Red) - Issue found (can resubmit)

---

## ❓ Common Questions

### Q: Do I need programming experience?
**A:** No! Just follow the 6 steps. Very beginner-friendly.

### Q: Is it free?
**A:** Completely free! No hidden costs.

### Q: Can I participate multiple times?
**A:** Yes! Once per time limit (2min, 5min, 10min). Each gives different certificate.

### Q: What if I close script early?
**A:** Still works! Results based on actual calculation time.

### Q: How long does verification take?
**A:** Usually 1-3 days after PR merge. Website scans automatically.

### Q: Can I edit my submission?
**A:** No. If mistake, create new PR with new codes.

### Q: Where do I get the codes?
**A:** The script displays them at the end. Take a screenshot!

### Q: What if I lose my codes?
**A:** Can't recover. You'll need to run the script again.

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

## 🚀 Quick Reference Commands

### Fork & Clone:
```bash
# Fork on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
cd pivalue.world
```

### Run Calculation:
```bash
python piclalculation.py
```

### Add to Verification:
```bash
cp pi_result_yourusername.json verification_list/
```

### Commit & Push:
```bash
git add verification_list/pi_result_yourusername.json
git commit -m "Add my Pi Value World submission"
git push
```

---

## 📞 Support & Resources

### Documentation Files:

All guides use the SAME consistent workflow:

1. **README.md** - Main project documentation
2. **HOW_IT_WORKS.md** - Detailed step-by-step guide
3. **OFFICIAL_RULES_GUIDE.md** - Rules and guidelines
4. **verification_list/README.md** - Submission instructions
5. **COMPLETE_USER_GUIDE.md** - This comprehensive guide

### Contact Information:

- **Creator:** Harinand Sindukumar
- **Email:** harinand@iths.online
- **Website:** https://iths.online
- **GitHub:** https://github.com/harinandsindukumar/
- **Domain:** https://pivalue.iths.online

### Help Channels:

| Purpose | Contact | Response Time |
|---------|---------|---------------|
| General Questions | harinand@iths.online | 1-2 days |
| Technical Issues | GitHub Issues | 1-3 days |
| Rule Appeals | harinand@iths.online | 5-7 days |

---

## ✅ Consistency Checklist

**All official documentation now uses:**

- ✅ Same 7-step workflow
- ✅ Same domain: pivalue.iths.online
- ✅ Same script name: piclalculation.py
- ✅ Same branch requirement: submission/username...
- ✅ Same verification method: verification_list/
- ✅ Same certificate generation: automatic after PR merge
- ✅ Same contact information throughout

**No conflicting information!**

---

## 🎉 Summary

**The Complete Journey:**

1. **FORK** → Your copy on GitHub
2. **CLONE** → Download to computer
3. **RUN** → Execute calculation script
4. **GET** → Save your two codes
5. **BRANCH** → Create submission branch (REQUIRED!)
6. **VERIFY** → Add to folder + PR
7. **CERTIFY** → Auto-verified → Download!

**Simple, clear, and consistent across all guides! 🥧**

---

*Created by Harinand Sindukumar*  
*https://pivalue.iths.online*  
*Contact: harinand@iths.online*

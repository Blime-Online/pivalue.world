# 🥧 Pi Value World - Complete Workflow Guide

**Super Simple 6-Step Process with Auto-Verification!**

**Domain:** https://pivalue.iths.online  
**Repository:** https://github.com/harinandsindukumar/pivalue.world

---

## ⚡ Quick Summary

```
1. FORK              → Your copy on GitHub
2. CLONE             → Download to computer
3. RUN               → python piclalculation.py (AUTO-ADDS to verification_list/)
4. COMMIT & PUSH     → Git commands (provided!)
5. CREATE PR         → Pull Request to main branch
6. AFTER MERGE       → Auto-verify → Certificate + Pi counter increases!
```

---

## 🎯 Detailed Step-by-Step Guide

### Step 1: Fork the Repository

**On GitHub:**

1. Go to: https://github.com/harinandsindukumar/pivalue.world
2. Click "Fork" button (top right corner)
3. Wait for GitHub to create your copy

**Why fork?**
- You get your own copy of the project
- Standard open source contribution workflow
- You can submit changes without affecting main repo

---

### Step 2: Clone Your Fork

**On your computer:**

```bash
# Replace YOUR_USERNAME with your GitHub username
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
cd pivalue.world
```

**What this does:**
- Downloads repository to your computer
- You now have all files locally
- Ready to run calculation script!

---

### Step 3: Run Calculation Script (AUTO-ADDS!)

**Navigate to src folder:**

```bash
cd src
```

**Run the script:**

```bash
python piclalculation.py
```

**What happens automatically:**

#### A. Script asks for details:
```
Enter your GitHub username: harinandsindukumar

Select time limit:
1. 2 minutes
2. 5 minutes
3. 10 minutes

Enter choice (1/2/3): 2
```

#### B. Calculates 22/7 repeatedly:
```
🔢 Starting calculation for 2 minute(s)...
⏳ Press Ctrl+C to stop early

⚡ Calculations: 1000 | Elapsed: 45.23s
⚡ Calculations: 2000 | Elapsed: 90.45s
...
```

#### C. Shows your results:
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
============================================================
```

#### D. **AUTOMATICALLY SAVES:**
```
💾 Results saved to: pi_result_harinandsindukumar.json
✅ AUTO-ADDED to verification_list/: verification_list/pi_result_harinandsindukumar.json
```

**You don't need to manually copy anything!** ✅

---

### Step 4: Commit & Push (Easy Commands!)

**The script shows you exactly what to run:**

```bash
# From root folder (go back one level)
cd ..

# Add the verification_list folder
git add verification_list/

# Commit with your username
git commit -m 'Add Pi Value World submission for harinandsindukumar'

# Push to your fork
git push
```

**That's it!** Your file is now on GitHub.

---

### Step 5: Create Pull Request

**Go to GitHub:**

1. Navigate to your fork:
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

After merge:
- Website will auto-verify my submission
- Pi counter will increase by 0.01
- Certificate will be generated

Thank you! 🥧
```

**Click:** "Create Pull Request"

---

### Step 6: After Merge - Automatic Magic! ✨

#### What Happens Automatically:

**Immediately after maintainer merges your PR:**

1. **GitHub Actions Triggers**
   - Workflow detects change in `verification_list/`
   - Runs sync_supabase.py automatically
   - Uploads your submission to database

2. **Website Validates**
   - Checks your Submission ID format
   - Verifies Verification Code
   - Confirms not duplicate
   - Marks as "Verified" ✅

3. **Status Updates**
   ```
   Before merge: ⏳ Pending / Not Verified
   After merge:  ✅ VERIFIED
   ```

4. **Pi Counter Increases!**
   ```
   Before your merge: 3.14
   After your merge:  3.15 (+0.01)
   
   Next person: 3.15 → 3.16
   And so on...
   ```

5. **Certificate Generated**
   - Beautiful A4 certificate created
   - Includes all your details
   - Ready to download!

#### You Can Now:

**Visit:** https://pivalue.iths.online/search

**Search for your submission:**
- Enter Submission ID: `abc123def456`
- Or Verification Code: `A1B2C3D4E5F6G7H8`

**Your record shows:**
```
✅ Status: VERIFIED (green badge)
👤 Username: @harinandsindukumar
⏱️ Time Limit: 2 minutes
🔢 Calculations: 13,245
📊 Precision: 1000 digits
🎫 Code: A1B2C3D4E5F6G7H8
🆔 ID: abc123def456

[📥 Download PNG] [🔗 Copy Link] [📱 Share]
```

**Download your certificate!** 🎉

---

## 🔄 Visual Flow Diagram

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
│ 3. RUN      │  → piclalculation.py
└─────────────┘                     
         │                          
         ├─→ Creates JSON file     
         │                          
         └─→ AUTO-ADDS to          
             verification_list/    
                     ↓                          
┌─────────────┐                     
│ 4. COMMIT   │  → Git commands    
│     & PUSH  │                    
└─────────────┘                     
         ↓                          
┌─────────────┐                     
│ 5. CREATE   │  → On GitHub       
│     PR      │                    
└─────────────┘                     
         ↓                          
                                    ┌─────────────┐
                                    │ MAINTAINER  │
                                    │ MERGES PR   │
                                    └─────────────┘
                                           ↓
                                    ┌─────────────┐
                                    │ GITHUB      │
                                    │ ACTIONS     │
                                    │ TRIGGERS    │
                                    └─────────────┘
                                           ↓
                                    ┌─────────────┐
                                    │ SYNC TO     │
                                    │ SUPABASE    │
                                    └─────────────┘
                                           ↓
                                    ┌─────────────┐
                                    │ AUTO        │
                                    │ VALIDATION  │
                                    └─────────────┘
                                           ↓
                                    ┌─────────────┐
                                    │ STATUS:     │
                                    │ ✅ VERIFIED │
                                    └─────────────┘
                                           ↓
                                    ┌─────────────┐
                                    │ PI COUNTER  │
                                    │ +0.01       │
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

## 📊 Pi Counter System

### How It Works:

**Starting Value:** 3.14

**Each Merged PR:**
```
Current Pi Value + 0.01 = New Pi Value
```

**Examples:**
```
User 1 merges: 3.14 → 3.15
User 2 merges: 3.15 → 3.16
User 3 merges: 3.16 → 3.17
...
User 100 merges: 4.13 → 4.14
```

### Where to See:

**Homepage Hero Section:**
- Large display showing current Pi value
- Increments automatically with each merge
- Visible to all visitors
- Shows community progress

**Database Counter:**
- Stored in Supabase `counter` table
- Updated by sync_supabase.py script
- Accurate and permanent record

---

## 🎯 What Makes This Easy?

### ✅ No Manual Steps:

**OLD WAY (Confusing):**
- Run script
- Manually copy file
- Navigate folders
- Figure out where to put it

**NEW WAY (Simple):**
- Run script → ✅ AUTO-ADDS!
- Just commit and push
- Create PR
- Done!

### ✅ Clear Instructions:

**Script tells you exactly what to do:**
```
🎯 NEXT STEPS - SUPER SIMPLE!
1. ✅ Result file created (done!)
2. ✅ Auto-added to verification_list/ (done!)
3. 📝 Run these commands:
   git add verification_list/
   git commit -m 'Add Pi Value World submission for YOUR_USERNAME'
   git push
4. 🔄 Create Pull Request on GitHub
5. ⏳ Wait for merge
6. 🎉 Get certificate!
```

### ✅ Automatic Verification:

**No manual review needed:**
- Website scans automatically
- Validates codes automatically
- Updates status automatically
- Generates certificate automatically

---

## 💡 Pro Tips

### For Best Results:

1. **Close other programs** before running
   - More CPU power = more calculations
   
2. **Choose longer time** for impressive certificate
   - 10 minutes = more calculations than 2 minutes
   
3. **Don't modify script**
   - Results won't verify
   - Will be rejected

4. **Take screenshot of codes**
   - Just in case
   - Can find in JSON file too

5. **Write good PR description**
   - Include all details from script output
   - Makes it clear you followed process

---

## ❓ Common Questions

### Q: Do I need to manually copy files?
**A:** NO! Script auto-adds to verification_list/ automatically!

### Q: What if I close script early?
**A:** Still works! Results based on actual calculation time.

### Q: How long until I get certificate?
**A:** Usually 1-3 days after PR merge (depends on maintainer).

### Q: Can I participate multiple times?
**A:** Yes! Once per time limit (2min, 5min, 10min). Each gives different certificate.

### Q: Does Pi counter really increase?
**A:** YES! Every merged PR adds +0.01 to the displayed Pi value on website.

### Q: What if PR is rejected?
**A:** Fix the issue mentioned in comments and resubmit.

### Q: Where do I find my codes?
**A:** 
- Displayed at end of script
- Saved in JSON file
- Both in root folder and verification_list/

---

## 📝 Exact Commands Reference

### Full Sequence:

```bash
# 1. Fork on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
cd pivalue.world

# 2. Go to source folder
cd src

# 3. Run calculation
python piclalculation.py
# Follow prompts, get your codes

# 4. Go back to root
cd ..

# 5. Add and commit (script shows exact commands!)
git add verification_list/
git commit -m 'Add Pi Value World submission for YOUR_USERNAME'
git push

# 6. Create PR on GitHub
# Go to your fork → Contribute → Open PR
```

---

## 🎉 Summary

**The Complete Journey:**

1. **FORK** → Your copy on GitHub
2. **CLONE** → Download to computer
3. **RUN** → Script calculates AND auto-adds!
4. **COMMIT** → Just run provided commands
5. **CREATE PR** → On GitHub to main branch
6. **AFTER MERGE** → Auto-verify + Pi increases + Certificate!

**Super simple, fully automatic! 🥧🚀**

---

*Created by Harinand Sindukumar*  
*Contact: harinand@iths.online*  
*Domain: https://pivalue.iths.online*

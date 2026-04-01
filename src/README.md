# 🐍 Python Source Files

**This is where you'll find the main Python scripts!**

---

## 🎯 What's Here

### Main Scripts:

1. **`piclalculation.py`** ⭐ **START HERE**
   - Main calculation script
   - Run this to participate in the challenge
   - Generates your verification codes

2. **`generate_certificate.py`**
   - Certificate generator (optional)
   - For manual certificate creation
   - Most users don't need this

---

## 🚀 How to Use

### Step 1: Navigate to This Folder
```bash
cd src
```

### Step 2: Run Calculation Script
```bash
python piclalculation.py
```

### Step 3: Follow the Prompts
- Enter your GitHub username
- Choose time limit (2, 5, or 10 minutes)
- Let it calculate 22/7 repeatedly
- **Save your Verification Code and Submission ID!**

### Step 4: Get Your Result File
After completion, you'll have:
- `pi_result_yourusername.json` (in root folder)
- Verification Code (16 characters)
- Submission ID (12 characters)

---

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies needed!
- Works on Windows, Mac, Linux

---

## 🔍 What Each Script Does

### piclalculation.py

**Purpose:** Calculate 22/7 repeatedly for a set time

**What happens:**
1. Asks for your GitHub username
2. You choose time limit
3. Calculates 22/7 using high precision (Decimal module)
4. Counts how many calculations completed
5. Generates unique codes
6. Saves results to JSON file

**Output:**
```
🎫 Verification Code: A1B2C3D4E5F6G7H8
🆔 Submission ID: abc123def456
💾 Results saved to: pi_result_harinandsindukumar.json
```

---

### generate_certificate.py

**Purpose:** Generate beautiful A4 certificates

**When to use:**
- Manual certificate generation
- Testing purposes
- Custom certificate creation

**Most users:** Don't need to run this!
- Certificates are auto-generated after PR merge
- Website handles everything automatically

---

## 💡 Pro Tips

1. **Close other programs** before running
   - More CPU power = more calculations
   
2. **Don't modify the script**
   - Results won't verify
   - Will be rejected

3. **Take screenshot of codes**
   - Can't recover if lost
   - Need both codes for submission

4. **Check generated JSON**
   - Verify all fields correct
   - Username matches GitHub

---

## 🔄 What Happens Next

After running the script:

1. ✅ You have your codes
2. ✅ JSON file created
3. ⏭️ Copy JSON to `verification_list/` folder
4. ⏭️ Create Pull Request
5. ⏭️ Wait for merge
6. ⏭️ Certificate auto-generated!

---

## ❓ Common Questions

### Q: Can I run this from root folder?
**A:** Yes! Both locations work:
```bash
# From root
python piclalculation.py

# From src folder
cd src
python piclalculation.py
```

### Q: Do I need to install anything?
**A:** No! Pure Python, no dependencies.

### Q: How long does it take?
**A:** Depends on your time limit choice (2/5/10 minutes).

### Q: Can I stop early?
**A:** Yes! Press Ctrl+C. Results based on actual time.

---

## 📞 Need Help?

- **Read:** [COMPLETE_USER_GUIDE.md](../COMPLETE_USER_GUIDE.md)
- **Check:** [README.md](../README.md)
- **Email:** harinand@iths.online

---

**Ready to calculate? Run `python piclalculation.py`! 🥧**

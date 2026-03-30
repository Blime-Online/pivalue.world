# 🥧 Pi Value World - Certificate Generation Guide

**Complete guide to generating beautiful certificates with user details and logo**

---

## 📋 What's Included in Each Certificate

Every certificate generated includes:

✅ **User Information:**
- GitHub username (@username)
- Time limit chosen (2, 5, or 10 minutes)
- Number of calculations performed
- Precision digits achieved

✅ **Verification Details:**
- 16-character verification code
- 12-character submission ID
- Verification date

✅ **Branding:**
- Pi Value World logo (π.png)
- Professional yellow/black/white theme
- Official seal and signature

---

## 🎨 Method 1: Python Certificate Generator (Recommended)

### Prerequisites

Install Pillow library:
```bash
pip install Pillow
```

### Steps:

1. **Run the calculation script:**
   ```bash
   python piclalculation.py
   ```
   - Enter your GitHub username
   - Choose time limit (2/5/10 minutes)
   - Complete the calculation
   - Save your verification code and submission ID

2. **Generate certificate automatically:**
   ```bash
   python generate_certificate.py
   ```

3. **The script will:**
   - Find your result file automatically
   - Load the Pi Value World logo
   - Generate a beautiful certificate (2480x3508 pixels, A4 size)
   - Save as PNG: `certificate_username_SUBMISSIONID.png`

### Example Output:

```
============================================================
🥧 Pi Value World - Certificate Generator 🥧
============================================================

✅ Found 1 result file(s):

1. pi_result_harinandsindukumar.json

Select file number (1-1): 1
🎨 Generating your Pi Value World Certificate...
✅ Logo added from website/assets/pi.png

============================================================
🎉 Certificate Generated Successfully!
============================================================
👤 Username: @harinandsindukumar
⏱️  Time Limit: 5 minute(s)
🔢 Calculations: 15,234
📊 Precision: 1000 digits
🎫 Verification Code: A1B2C3D4E5F6G7H8
🆔 Submission ID: abc123def456
💾 Saved to: certificate_harinandsindukumar_abc123def456.png
============================================================
```

---

## 🌐 Method 2: Website Certificate Generator

### After Your Submission is Verified:

1. **Visit the website:**
   - Go to https://pivalue.world
   - Search for your submission ID
   - Or use direct link: `/certificate.html?id=YOUR_ID`

2. **Download options:**
   - Click "📥 Download PNG" for image
   - Click "📄 Download PDF" for PDF document
   - Click "🔗 Copy Shareable Link" for web link

3. **Share on social media:**
   - GitHub profile
   - Twitter/X
   - LinkedIn

---

## 📊 Database Integration

### Supabase Schema

The complete SQL schema includes certificate generation function:

```sql
-- Create certificate for verified submission
SELECT create_certificate_for_submission(
    'submission-uuid-here',
    'assets/certificate.png'
);
```

This function:
1. Validates submission is verified
2. Builds certificate data JSON
3. Stores in certificates table
4. Returns certificate ID

### Query Certificates:

```sql
-- Get all certificates with details
SELECT * FROM certificate_details;

-- Get specific certificate
SELECT * FROM certificate_details 
WHERE short_id = 'abc123def456';
```

---

## 🎯 Certificate Design Details

### Layout Specifications:

**Canvas Size:**
- Width: 2480 pixels (A4 at 300 DPI)
- Height: 3508 pixels (A4 at 300 DPI)
- Resolution: 300 DPI (print quality)

**Elements Position:**

1. **Logo** (Top center)
   - Size: 300x300 pixels
   - Position: Y=150px from top
   - Format: PNG with transparency support

2. **Title** (Below logo)
   - Text: "Certificate of Achievement"
   - Font: Arial Bold 80pt
   - Color: Black

3. **Subtitle**
   - Text: "Pi Value World Challenge"
   - Font: Arial 40pt
   - Color: Gray (#666666)

4. **Username** (Prominent center)
   - Format: @username
   - Font: Arial Bold 90pt
   - Color: Gold (#FFD700) with black stroke

5. **Statistics Boxes** (3 boxes)
   - Box 1: Time Limit
   - Box 2: Calculations
   - Box 3: Precision
   - Size: 600x350 pixels each
   - Background: Light yellow (#FFFACD)
   - Border: Gold (#FFD700)

6. **Verification Details**
   - Verification Code (monospace font)
   - Submission ID (monospace font)
   - Date (formatted: Month DD, YYYY)

7. **Footer**
   - Pi Value World branding
   - Website URL
   - Signature line

### Color Scheme:

- Primary Yellow: #FFD700
- Light Yellow: #FFFACD
- Black: #000000
- White: #FFFFFF
- Gray: #666666

---

## 🔧 Customization Options

### Modify Certificate Template:

Edit `generate_certificate.py`:

```python
# Change logo
logo_path = "your-custom-logo.png"

# Change colors
draw.rectangle([...], fill='#YOUR_COLOR', outline='#YOUR_BORDER')

# Change fonts
font = ImageFont.truetype("your-font.ttf", size=80)

# Change size
width, height = 2480, 3508  # A4
# or
width, height = 3300, 2550  # Letter
```

### Add Custom Fields:

```python
# Add organization name
org_text = "Presented by: Your Organization"
draw.text((width//2, y_position), org_text, fill='black', font=font)

# Add QR code for verification
# import qrcode
# qr = qrcode.make(f"https://pivalue.world/search?id={submission_id}")
# cert.paste(qr, (x, y))
```

---

## 📁 File Structure

```
piworld/
├── generate_certificate.py      # Certificate generator script
├── piclalculation.py           # Calculation script
├── pi.png                       # Logo file
│
├── website/
│   ├── assets/
│   │   ├── pi.png              # Web logo
│   │   └── certificate.png     # Certificate template
│   └── js/
│       └── certificate.js      # Web certificate generator
│
└── certificates/                # Generated certificates (optional folder)
    └── certificate_username_ID.png
```

---

## 🚀 Quick Start Examples

### Example 1: Generate from Result File

```bash
# Run calculation
python piclalculation.py
# ... complete challenge ...

# Generate certificate
python generate_certificate.py
# Select your result file
# Done! Certificate saved.
```

### Example 2: Manual Entry

```bash
python generate_certificate.py
# No files found, entering manually:
GitHub username: harinandsindukumar
Time limit: 5
Calculations: 15000
Precision: 1000
Verification code: A1B2C3D4E5F6G7H8
Submission ID: abc123def456

# Certificate generated!
```

### Example 3: Batch Generation

```python
# Generate multiple certificates
import json
from generate_certificate import create_certificate

users = [
    {
        'username': 'user1',
        'time_limit': 5,
        'calculations': 15000,
        'precision': 1000,
        'verification_code': 'ABC123',
        'submission_id': 'DEF456'
    },
    # ... more users
]

for user in users:
    create_certificate(**user)
```

---

## ✅ Quality Checklist

Before sharing your certificate:

- [ ] Logo displays correctly
- [ ] Username is correct
- [ ] Time limit matches your choice
- [ ] Calculations count is accurate
- [ ] Precision digits are correct
- [ ] Verification code matches
- [ ] Submission ID matches
- [ ] Date is correct
- [ ] Colors look good
- [ ] No typos or errors

---

## 🎨 Sample Certificate Text

```
                    [PI VALUE WORLD LOGO]
                    
              Certificate of Achievement
              
                  Pi Value World Challenge
                  
            This is to certify that
            
                 @harinandsindukumar
                 
    has successfully completed the Pi Value World Challenge
    
    ┌─────────────┬─────────────┬─────────────┐
    │ Time Limit  │Calculations │  Precision  │
    │  5 minute(s)│   15,234    │  1000 digits│
    └─────────────┴─────────────┴─────────────┘
    
              Verification Details
              
    Verification Code: A1B2C3D4E5F6G7H8
    Submission ID: abc123def456
    Verified on: March 30, 2024
    
    _______________________________________
    Authorized by Pi Value World Team
    
    Pi Value World | https://pivalue.world
```

---

## 📞 Support

**Issues with certificate generation?**

- Check Pillow is installed: `pip install Pillow`
- Verify logo exists: `website/assets/pi.png`
- Check permissions to save files
- Contact: harinand@iths.online

---

## 🌟 Pro Tips

1. **High Quality:** Keep default 300 DPI for print quality
2. **Logo Size:** 300x300px looks best on certificate
3. **Fonts:** Use Arial or similar professional fonts
4. **Colors:** Stick to yellow/black/white theme
5. **Backup:** Save both PNG and PDF versions
6. **Share:** Use shareable link for GitHub profile

---

**Your certificate is now ready to showcase! 🎉**

*Created by Harinand Sindukumar | https://iths.online*

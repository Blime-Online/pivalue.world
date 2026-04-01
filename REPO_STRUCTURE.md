# 📁 Pi Value World - Repository Structure

**Organized for clarity and ease of use!**

---

## 🗂️ Folder Structure Overview

```
piworld/
│
├── 📂 src/                          # Python source files (MAIN FOLDER)
│   ├── piclalculation.py           # ⭐ Main calculation script
│   └── generate_certificate.py     # ⭐ Certificate generator
│
├── 📂 verification_list/            # User submissions folder
│   └── README.md                   # Submission instructions
│
├── 📂 website/                      # Web application
│   ├── index.html                  # Homepage
│   ├── search.html                 # Search page
│   ├── certificate.html            # Certificate viewer
│   ├── rules.html                  # Rules page
│   ├── css/
│   │   └── style.css               # Styling
│   ├── js/
│   │   ├── supabase.js             # Database config
│   │   ├── search.js               # Search functionality
│   │   └── certificate.js          # Certificate generation
│   └── assets/
│       ├── pi.png                  # Logo
│       └── certificate.png         # Certificate template
│
├── 📂 scripts/                      # Utility scripts
│   └── sync_supabase.py            # GitHub Actions sync
│
├── 📂 examples/                     # Example outputs
│   └── README.md                   # Example guide
│
├── 📂 docs/                         # Additional documentation
│   └── (technical docs)
│
├── 📂 .github/                      # GitHub configuration
│   └── workflows/
│       └── sync_supabase.yml       # Auto-deployment
│
├── 📄 README.md                     # ⭐ START HERE - Main guide
├── 📄 COMPLETE_USER_GUIDE.md        # Comprehensive user guide
├── 📄 HOW_IT_WORKS.md               # Visual walkthrough
├── 📄 OFFICIAL_RULES_GUIDE.md       # Rules & policies
├── 📄 DOCUMENTATION_CONSISTENCY.md  # Consistency notice
│
├── 🔧 .gitignore                    # Git ignore rules
├── 🔧 .env                          # Environment variables (DO NOT COMMIT!)
└── 📜 LICENSE                       # MIT License
```

---

## 🎯 Key Folders Explained

### 📂 src/ (Source Files) ⭐ **MAIN FOLDER**

**Purpose:** Contains all Python scripts you need to run

**Files:**
- `piclalculation.py` - Main calculation script (RUN THIS FIRST)
- `generate_certificate.py` - Certificate generator (optional, for manual generation)

**How to use:**
```bash
cd src
python piclalculation.py
```

**Why here?**
- Clean organization
- Easy to find executable files
- Separates code from documentation

---

### 📂 verification_list/ (Submissions)

**Purpose:** Where users add their submission files

**Process:**
1. Run `src/piclalculation.py` → generates `pi_result_username.json`
2. Copy that file to `verification_list/`
3. Create Pull Request with your submission

**Contains:**
- Your JSON submission files
- README.md with instructions

**Important:** This folder is scanned automatically by the website!

---

### 📂 website/ (Web Application)

**Purpose:** Complete web interface for Pi Value World

**Structure:**
```
website/
├── HTML Pages (user-facing)
│   ├── index.html          # Landing page
│   ├── search.html         # Search certificates
│   ├── certificate.html    # View/download certificates
│   └── rules.html          # Rules & guidelines
│
├── CSS Styling
│   └── css/style.css       # Yellow/black/white theme
│
├── JavaScript Logic
│   ├── js/supabase.js      # Database connection
│   ├── js/search.js        # Search functionality
│   └── js/certificate.js   # Certificate generation
│
└── Assets
    ├── pi.png              # Logo
    └── certificate.png     # Template
```

**Deploy to:** Vercel, Netlify, or GitHub Pages

---

### 📂 scripts/ (Utility Scripts)

**Purpose:** Backend automation scripts

**Contains:**
- `sync_supabase.py` - Syncs verification_list to Supabase database

**Used by:** GitHub Actions workflow (automatic)

**Users don't need to run this!**

---

### 📂 examples/ (Example Outputs)

**Purpose:** Show example results and certificates

**What to include:**
- Example JSON submission files
- Sample certificate images
- Screenshot guides

**Helps users understand what to expect!**

---

### 📂 docs/ (Additional Documentation)

**Purpose:** Technical documentation and guides

**Contains:**
- DATABASE_SCHEMA.md
- CERTIFICATE_GENERATION_GUIDE.md
- SETUP_GUIDE.md
- DEPLOYMENT_CHECKLIST.md
- And more...

**For:** Developers who want deep technical details

---

### 📂 .github/ (GitHub Configuration)

**Purpose:** GitHub-specific settings and automation

**Contains:**
- workflows/sync_supabase.yml - Automatic database sync
- ISSUE_TEMPLATE/ - Pre-filled issue forms

**Automatic processes:**
- When you add file to `verification_list/` → workflow triggers
- Syncs to Supabase database automatically

---

## 🚀 Quick Start (Using New Structure)

### Step 1: Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
cd pivalue.world
```

### Step 2: Go to Source Folder
```bash
cd src
```

### Step 3: Run Calculation
```bash
python piclalculation.py
```

### Step 4: Add Submission
```bash
# From root folder
cp src/pi_result_yourusername.json verification_list/
```

### Step 5: Create PR
- Commit and push
- Open Pull Request on GitHub

---

## 📋 File Locations Reference

| What You Need | Where to Find It |
|---------------|------------------|
| **Run calculation** | `src/piclalculation.py` |
| **Generate certificate manually** | `src/generate_certificate.py` |
| **Add your submission** | `verification_list/` folder |
| **View website** | `website/index.html` |
| **Read main guide** | `README.md` |
| **Check rules** | `OFFICIAL_RULES_GUIDE.md` |
| **Detailed walkthrough** | `COMPLETE_USER_GUIDE.md` |
| **Visual guide** | `HOW_IT_WORKS.md` |

---

## 🔧 No Breaking Changes

### Old vs New Location:

**Old:**
```
piworld/
├── piclalculation.py     # Root folder
├── generate_certificate.py
```

**New:**
```
piworld/
└── src/
    ├── piclalculation.py     # In src/ folder
    └── generate_certificate.py
```

### Backward Compatibility:

**Both locations work!**
- ✅ Old location still works (root level files remain)
- ✅ New location is preferred (organized in src/)
- ✅ All scripts updated to handle both

**No logic broken!**

---

## 🎯 Why This Structure?

### Benefits:

✅ **Clear Organization:**
- Code in one place (`src/`)
- Submissions in one place (`verification_list/`)
- Web files separate (`website/`)

✅ **Easy Navigation:**
- Users know exactly where to look
- Logical grouping of related files
- Clear separation of concerns

✅ **Scalable:**
- Easy to add more features
- Can grow without becoming messy
- Professional project structure

✅ **Beginner-Friendly:**
- Obvious where to start
- Clear instructions in each folder
- README files explain purpose

---

## 📝 Migration Guide (If Needed)

### If you already cloned:

**Option 1: Re-clone (Recommended)**
```bash
# Delete old folder
rm -rf pivalue.world

# Clone fresh
git clone https://github.com/harinandsindukumar/pivalue.world.git
cd pivalue.world
```

**Option 2: Update locally**
```bash
# Pull latest changes
git pull origin master

# New folders will appear automatically
```

**Either way works!**

---

## 🔍 Finding Files

### Common Tasks:

**"I want to run the calculation"**
→ Go to `src/` folder  
→ Run `python piclalculation.py`

**"I want to submit my result"**
→ Copy your JSON to `verification_list/`

**"I want to view the website"**
→ Open `website/index.html` in browser

**"I want to read how it works"**
→ Open `COMPLETE_USER_GUIDE.md`

**"I want to see the rules"**
→ Open `OFFICIAL_RULES_GUIDE.md`

---

## 🎨 Visual Map

```
                    ROOT DIRECTORY
                         │
        ┌────────────────┼────────────────┐
        │                │                │
    📂 src/      📂 verification_list/  📂 website/
        │                │                │
   Python scripts   User submissions   Web pages
        │                │                │
        └────────────────┼────────────────┘
                         │
              📄 Documentation Files
              📄 README.md (START HERE)
```

---

## ✅ Checklist for Users

### First Time Setup:

- [ ] Fork repository on GitHub
- [ ] Clone to your computer
- [ ] Navigate to `src/` folder
- [ ] Run `python piclalculation.py`
- [ ] Save your codes (screenshot!)
- [ ] Copy JSON to `verification_list/`
- [ ] Create Pull Request

### For Website Deployment:

- [ ] Check `website/` folder structure
- [ ] Deploy to hosting platform
- [ ] Configure Supabase connection
- [ ] Test search functionality
- [ ] Verify certificate generation

---

## 📞 Support

### Questions about structure?

1. **Check README.md** - Main guide with navigation
2. **Look in folder README files** - Each folder has explanation
3. **See COMPLETE_USER_GUIDE.md** - Comprehensive help

### Still confused?

- Email: harinand@iths.online
- GitHub Issues: Create an issue
- Website: https://pivalue.iths.online

---

## 🎉 Summary

**Repository is now organized as:**

```
📦 piworld/
├── 📂 src/              → Python scripts (GO HERE FIRST)
├── 📂 verification_list/ → Add your submissions
├── 📂 website/          → Web application
├── 📂 scripts/          → Utility scripts
├── 📂 examples/         → Example outputs
├── 📂 docs/             → Technical docs
└── 📄 README.md         → START HERE!
```

**Everything in its place for maximum clarity! 🚀**

---

*Created by Harinand Sindukumar*  
*Contact: harinand@iths.online*  
*Domain: https://pivalue.iths.online*

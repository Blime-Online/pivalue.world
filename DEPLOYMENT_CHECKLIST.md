# 🥧 Pi Value World - Deployment Checklist

Your Supabase is configured! Follow this checklist to complete deployment.

---

## ✅ Configuration Status

### Supabase Credentials
- ✅ **URL**: `https://ywpjpzbembudsyihxylz.supabase.co`
- ✅ **Key**: Configured in `website/js/supabase.js`
- ✅ **Environment File**: Created `.env` file

---

## 📋 Next Steps

### 1. Setup Supabase Database (Required) ⚠️

**IMPORTANT:** You need to create the database tables in your Supabase project.

#### Steps:

1. **Go to Supabase Dashboard**
   - Visit: https://supabase.com/dashboard
   - Login to your account
   - Select project: `ywpjpzbembudsyihxylz`

2. **Open SQL Editor**
   - Click "SQL Editor" in left sidebar
   - Click "New Query"

3. **Create Tables**
   - Open file: `website/supabase-schema.sql`
   - Copy ALL the SQL code
   - Paste into Supabase SQL Editor
   - Click "Run" or press Ctrl+Enter
   
4. **Verify Tables Created**
   - Go to "Table Editor"
   - You should see these tables:
     - ✅ submissions
     - ✅ certificates
     - ✅ counter
     - ✅ audit_log

5. **Test Connection**
   - Insert a test row in submissions table:
   ```sql
   INSERT INTO submissions (
       github_username, 
       verification_code, 
       submission_id,
       time_limit,
       calculations_performed,
       precision_digits,
       elapsed_seconds,
       status
   ) VALUES (
       'testuser',
       'TEST123456789ABC',
       'test123456789',
       2,
       5000,
       1000,
       120.00,
       'pending'
   );
   ```

---

### 2. Test Website Locally (5 minutes)

#### Option A: Python Server
```bash
cd website
python -m http.server 8000
```
Then visit: http://localhost:8000

#### Option B: Open HTML Directly
Just double-click `website/index.html`

#### What to Check:
- [ ] Homepage loads
- [ ] Counter shows "3.14"
- [ ] Navigation works
- [ ] Search page accessible
- [ ] Verify page form displays
- [ ] No console errors (F12 → Console)

---

### 3. Deploy Website (Choose One)

#### Option A: GitHub Pages (Free & Easy)

```bash
# Make sure you're in website folder
cd website

# Create gh-pages branch
git checkout --orphan gh-pages
git reset --hard

# Add all files
git add .
git commit -m "Deploy Pi Value World website"

# Push to GitHub
git push origin gh-pages
```

Then in GitHub:
1. Go to repo settings
2. Pages section
3. Source: Select `gh-pages` branch
4. Your site will be live at: `https://username.github.io/pivalue.world`

#### Option B: Vercel (Recommended for Production)

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Deploy:
```bash
cd website
vercel --prod
```

3. Follow prompts
4. Done! Free URL provided

#### Option C: Netlify

1. Go to https://app.netlify.com/drop
2. Drag and drop the `website` folder
3. Get instant deployment!

---

### 4. Test Full Flow (End-to-End)

#### Test Calculation Script:
```bash
cd c:\Users\SANAL\myprojects\piworld
python piclalculation.py
```

**Test Run:**
1. Enter GitHub username: `testuser`
2. Choose time: `1` (2 minutes)
3. Let it run for ~30 seconds
4. Press Ctrl+C to stop early
5. Note the Verification Code and Submission ID
6. Check JSON file created: `pi_result_testuser.json`

#### Test Verification Script:
```bash
python verify.py
```

1. Choose option 1 (use existing file)
2. Submit verification
3. Check submission file created

---

### 5. Verify Database Integration

Open browser console (F12) and check for:

✅ **Success Messages:**
- "🥧 Pi Value World - Database Module Loaded"
- No error messages

❌ **If you see errors:**
- Check Supabase credentials in `website/js/supabase.js`
- Verify tables are created in Supabase
- Check browser console for specific error

---

### 6. Configure Row Level Security (RLS)

In Supabase Dashboard:

1. **Authentication → Policies**
2. Find `submissions` table
3. Enable RLS if not already enabled
4. Verify policies from schema are active:
   - ✅ Public can view verified submissions
   - ✅ Anyone can create submissions

---

### 7. Setup GitHub Webhook (Optional - For Auto-Increment)

For automatic counter increment on PR merge:

1. **GitHub Repo Settings**
   - Webhooks → Add webhook
   - Payload URL: Will create with Supabase Edge Function
   - Content type: application/json
   - Events: Pull requests

2. **Create Supabase Edge Function** (Advanced)
   ```bash
   npm install -g supabase
   supabase login
   supabase link --project-ref ywpjpzbembudsyihxylz
   supabase functions new increment-counter
   ```

---

## 🎯 Quick Test Commands

### Test Python Scripts:
```bash
# Navigate to project
cd c:\Users\SANAL\myprojects\piworld

# Run calculation (quick test - 2 min)
python piclalculation.py

# Then verify
python verify.py
```

### Test Website:
```bash
# Start local server
cd website
python -m http.server 8000

# Or open directly
start index.html
```

---

## 🔍 Troubleshooting

### Website Shows "Supabase not configured"
**Solution:** Check `website/js/supabase.js` has correct credentials
```javascript
const SUPABASE_CONFIG = {
    url: 'https://ywpjpzbembudsyihxylz.supabase.co',
    anonKey: 'sb_publishable_ikmQddB_jRs42qrkHBL6tg_f65ek8YU'
};
```

### Can't Insert Data into Database
**Solution:** Check RLS policies are disabled or properly configured
```sql
-- Temporarily disable RLS for testing
ALTER TABLE submissions DISABLE ROW LEVEL SECURITY;
```

### Counter Shows 3.14 Always
**Solution:** Make sure counter table has initial value
```sql
INSERT INTO counter (id, value) VALUES (1, 3.14) 
ON CONFLICT (id) DO NOTHING;
```

---

## 📊 Success Criteria

Before going live, verify:

- [ ] Supabase tables created successfully
- [ ] Can insert test submission via SQL
- [ ] Website loads without errors
- [ ] Python scripts run correctly
- [ ] Result files generated
- [ ] No console errors on website
- [ ] Search page accessible
- [ ] Certificate page displays properly

---

## 🚀 Ready to Launch!

Once all checkboxes are complete:

1. ✅ Database configured
2. ✅ Website deployed
3. ✅ Scripts tested
4. ✅ End-to-end flow works

**You're ready to share with the world!** 🌟

---

## 📞 Support

If you encounter issues:

- Check SETUP_GUIDE.md for detailed instructions
- Review console errors in browser (F12)
- Verify Supabase dashboard shows all tables
- Test Python scripts locally first

**Good luck! 🥧**

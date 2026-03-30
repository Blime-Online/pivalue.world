# 🥧 Pi Value World - Setup Guide

Complete setup instructions for developers and administrators.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [For Users](#for-users)
3. [For Developers](#for-developers)
4. [Supabase Setup](#supabase-setup)
5. [Website Deployment](#website-deployment)
6. [GitHub Integration](#github-integration)
7. [Troubleshooting](#troubleshooting)

---

## Quick Start

### For Users (Want to participate?)

```bash
# 1. Clone the repository
git clone https://github.com/harinandsindukumar/pivalue.world.git
cd pivalue.world

# 2. Run the calculation script
python piclalculation.py

# 3. Follow the prompts!
```

That's it! The script will guide you through the rest.

---

## For Developers

### Prerequisites

- **Python**: Version 3.6 or higher
- **Git**: For version control
- **Text Editor**: VS Code, PyCharm, etc.
- **Optional**: Supabase account (for backend)

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
cd pivalue.world

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install optional dependencies
pip install pyperclip requests
```

### Running Locally

```bash
# Test the calculation script
python piclalculation.py

# Test the verification script
python verify.py
```

### Website Development

No build process needed! The website is static HTML/CSS/JS.

```bash
# Option 1: Open HTML file directly
open website/index.html

# Option 2: Use Python HTTP server
cd website
python -m http.server 8000
# Visit: http://localhost:8000

# Option 3: Use VS Code Live Server extension
```

---

## Supabase Setup

### Step 1: Create Supabase Project

1. Go to [https://supabase.com](https://supabase.com)
2. Sign up/Login
3. Click "New Project"
4. Fill in:
   - **Name**: pivalue-world
   - **Database Password**: Choose a strong password
   - **Region**: Choose closest to your users
5. Click "Create new project"

### Step 2: Get API Credentials

1. In your Supabase dashboard, go to **Settings** → **API**
2. Copy these values:
   - **Project URL**: `https://xxxxx.supabase.co`
   - **anon/public key**: `eyJhbG...` (long string)

### Step 3: Create Database Tables

1. Go to **SQL Editor** in Supabase dashboard
2. Click "New Query"
3. Open the file `website/supabase-schema.sql` from this repo
4. Copy entire contents
5. Paste into Supabase SQL Editor
6. Click "Run" ▶️
7. Wait for success message

### Step 4: Configure Website

1. Open `website/js/supabase.js`
2. Find this section:

```javascript
const SUPABASE_CONFIG = {
    url: 'YOUR_SUPABASE_URL',
    anonKey: 'YOUR_SUPABASE_ANON_KEY'
};
```

3. Replace with your credentials:

```javascript
const SUPABASE_CONFIG = {
    url: 'https://your-project.supabase.co',
    anonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
};
```

4. Save the file

### Step 5: Add Supabase JS Library

Add this to all HTML pages that need database access (in `<head>`):

```html
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
```

The template files already include this where needed.

### Step 6: Test Connection

1. Open browser console (F12)
2. Go to your website
3. Look for console messages:
   - ✅ "🥧 Pi Value World - Database Module Loaded"
   - ⚠️ If you see warnings, check your configuration

---

## Website Deployment

### Option 1: GitHub Pages (Free & Easy)

```bash
# 1. Make sure you're in the website directory
cd website

# 2. Create a new branch for GitHub Pages
git checkout --orphan gh-pages
git reset --hard

# 3. Add all website files
git add .

# 4. Commit
git commit -m "Deploy website to GitHub Pages"

# 5. Push
git push origin gh-pages
```

Then in GitHub repo settings:
- Settings → Pages
- Source: Select `gh-pages` branch
- Your site will be live at: `https://username.github.io/pivalue.world/`

### Option 2: Vercel (Recommended for Production)

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Deploy:
```bash
cd website
vercel --prod
```

3. Follow the prompts
4. Done! You get a free URL

### Option 3: Netlify

1. Drag and drop the `website` folder to [Netlify Drop](https://app.netlify.com/drop)
2. Or connect your GitHub repo
3. Automatic deployments on every push!

### Option 4: Traditional Hosting

Upload the `website` folder contents to any web server:
- Apache/Nginx
- Shared hosting
- AWS S3 + CloudFront

Just serve static files!

---

## GitHub Integration

### Setup GitHub Webhook (for auto-increment counter)

1. Go to your GitHub repo
2. Settings → Webhooks → Add webhook
3. Configuration:
   - **Payload URL**: Your Supabase Edge Function URL (need to create)
   - **Content type**: application/json
   - **Events**: Pull requests (merge events)
4. Save

### Create Supabase Edge Function

```bash
# Install Supabase CLI
npm install -g supabase

# Login
supabase login

# Link to your project
supabase link --project-ref your-project-ref

# Create function
supabase functions new increment-counter
```

Edit `supabase/functions/increment-counter/index.ts`:

```typescript
import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

serve(async (req) => {
  const supabase = createClient(
    Deno.env.get('SUPABASE_URL') ?? '',
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
  )
  
  // Increment counter
  const { data, error } = await supabase.rpc('increment_pi_counter')
  
  if (error) {
    return new Response(JSON.stringify({ error }), { status: 500 })
  }
  
  return new Response(JSON.stringify({ success: true, data }))
})
```

Deploy:
```bash
supabase functions deploy increment-counter
```

---

## Environment Variables

Create a `.env` file (DO NOT commit to Git):

```env
# Supabase
PIVALUE_SUPABASE_URL=https://your-project.supabase.co
PIVALUE_SUPABASE_KEY=your-anon-key

# GitHub (if using OAuth)
GITHUB_CLIENT_ID=your-client-id
GITHUB_CLIENT_SECRET=your-client-secret

# Optional: For certificate generation
CERTIFICATE_WIDTH=297
CERTIFICATE_HEIGHT=210
```

---

## Troubleshooting

### Python Script Issues

**Problem**: "ModuleNotFoundError: No module named 'decimal'"
- **Solution**: This is a built-in module. Check your Python installation.

**Problem**: Script runs but shows no output
- **Solution**: Make sure you're running in a terminal, not double-clicking the file.

### Website Issues

**Problem**: "Supabase not configured"
- **Solution**: Check `website/js/supabase.js` has correct credentials

**Problem**: Search doesn't work
- **Solution**: Verify Supabase tables are created and RLS policies are set

**Problem**: Certificate download fails
- **Solution**: Ensure html2canvas and jsPDF libraries are loaded

### Database Issues

**Problem**: "relation does not exist"
- **Solution**: Run the SQL schema in Supabase

**Problem**: Can't insert data
- **Solution**: Check RLS policies. You may need to disable them for testing or configure authentication.

### Deployment Issues

**Problem**: Website shows blank page
- **Solution**: Check browser console for errors. Verify file paths are correct.

**Problem**: CSS not loading
- **Solution**: Check path to CSS file. Should be `css/style.css` relative to HTML.

---

## Testing Checklist

Before going live, test:

- [ ] Python script runs successfully
- [ ] Generates result file
- [ ] Verification script works
- [ ] Website loads properly
- [ ] Search finds submissions
- [ ] Certificate generates correctly
- [ ] Mobile responsive design works
- [ ] All links work
- [ ] Forms submit correctly
- [ ] Database queries work

---

## Security Checklist

- [ ] Supabase RLS enabled
- [ ] API keys not exposed in client code
- [ ] Input validation on all forms
- [ ] Rate limiting configured
- [ ] CORS properly set
- [ ] No sensitive data in logs
- [ ] Regular backups enabled

---

## Support

Need help?

- **Documentation**: See README.md
- **Issues**: Create GitHub issue
- **Email**: support@pivalue.world
- **Discussions**: GitHub Discussions tab

---

## Next Steps

After setup:

1. ✅ Test everything locally
2. ✅ Deploy to staging environment
3. ✅ Test with real users
4. ✅ Deploy to production
5. ✅ Monitor and maintain

Good luck! 🚀

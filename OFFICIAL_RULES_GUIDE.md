# 🥧 Pi Value World - Official Rules & Guidelines

**Domain:** https://pivalue.iths.online  
**Created by:** Harinand Sindukumar  
**Contact:** harinand@iths.online | https://iths.online

---

## 📜 Table of Contents

1. [Official Challenge Rules](#official-challenge-rules)
2. [Code of Conduct](#code-of-conduct)
3. [Submission Guidelines](#submission-guidelines)
4. [Verification Process](#verification-process)
5. [Certificate System](#certificate-system)
6. [Security Policies](#security-policies)
7. [Privacy Policy](#privacy-policy)
8. [Copyright & License](#copyright--license)
9. [Enforcement](#enforcement)
10. [Changes to Rules](#changes-to-rules)

---

## 🎯 Official Challenge Rules

### Eligibility

✅ **Who Can Participate:**
- Anyone with a GitHub account
- All ages and skill levels welcome
- Free to participate
- Must use your own computer hardware

❌ **Who Cannot Participate:**
- Users creating multiple accounts to bypass limits
- Users who have been banned for cheating
- Automated bots or scripts

### Time Limits

Choose one time limit per attempt:
- **2 minutes** - Quick challenge
- **5 minutes** - Standard challenge
- **10 minutes** - Extended challenge

**Restrictions:**
- One submission per time limit per user
- Can participate multiple times with different time limits
- Early termination allowed (results may vary)

### Calculation Requirements

**Must Use:**
- Official `calculation.py` script from this repository
- Unmodified script (no changes to code)
- Python 3.6 or higher
- Your own computer hardware

**Must Not:**
- Modify the calculation script
- Use automated scripts or macros
- Run multiple instances simultaneously
- Use cloud computing services

---

## 🤝 Code of Conduct

### Our Pledge

We pledge to make participation in Pi Value World a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity, level of experience, nationality, personal appearance, race, religion, or sexual identity.

### Expected Behavior

✅ **Always:**
- Be respectful and inclusive
- Welcome newcomers and help them learn
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others
- Have fun and enjoy the challenge!

❌ **Never:**
- Trolling, insulting comments, or personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other unethical or unprofessional conduct
- Cheating or attempting to circumvent rules

---

## 📋 Submission Guidelines

### How to Submit

1. **Run Calculation**
   ```bash
   python piclalculation.py
   # Follow prompts
   # Save your verification code and submission ID
   ```

2. **Prepare Submission File**
   - The script saves a JSON file (e.g., `pi_result_yourusername.json`).
   - Verify `github_username`, `submission_id`, and `verification_code` are correct.

3. **Add to Verification List
   - Add your result JSON to the repository verification list path (e.g., `verification_list/`).
   - Include a short README update in your PR describing the run.

4. **Create Pull Request**
   - Fork the repository.
   - Commit your submission file.
   - Open a PR titled `feat: add submission for <username>`.

5. **Automatic Scan & Verification**
   - Once merged, the web system scans the verification list.
   - It checks Submission ID + Verification Code and marks the record as verified.
   - Your certificate is generated automatically.

6. **Approval / Certificate**
   - You may still receive manual review details via PR comments.
   - Verified entries appear in the search page within minutes.

### What to Include

**Required Information:**
- Valid GitHub username
- Correct verification code
- Correct submission ID
- Accurate calculation results

**Optional:**
- Screenshot of calculation process
- Additional notes or comments

---

## 🔍 Verification Process

### Review Steps

1. **Automated Checks**
   - Code format validation
   - Duplicate detection
   - Basic anti-cheat verification

2. **Manual Review**
   - Maintainer reviews submission
   - Checks calculation authenticity
   - Verifies timing is reasonable
   - Confirms no script modifications

3. **Approval**
   - Submission marked as "Verified"
   - Certificate automatically generated
   - Pi counter increments (3.14 → 3.15)
   - Certificate available for download

4. **Rejection** (if needed)
   - Reason provided to user
   - Can resubmit after fixing issues
   - Appeals process available

### Timeline

- **Review Time:** 1-3 business days
- **Certificate Generation:** Immediate after approval
- **Counter Increment:** Automatic on approval

---

## 🎓 Certificate System

### Certificate Contents

Every certificate includes:

✅ **User Information:**
- GitHub username (@username)
- Time limit chosen (2/5/10 minutes)
- Number of calculations performed
- Precision digits achieved

✅ **Verification Details:**
- 16-character verification code
- 12-character submission ID
- Verification date

✅ **Official Branding:**
- Pi Value World logo
- Professional yellow/black/white design
- Official seal and signature
- Website URL: https://pivalue.iths.online

### Certificate Formats

**Available Formats:**
1. **PNG Image** - High quality (300 DPI, A4 size)
2. **PDF Document** - Print-ready format
3. **Web Link** - Shareable URL for profiles

**Usage Rights:**
- ✅ Personal use encouraged
- ✅ Share on social media
- ✅ Add to GitHub profile
- ✅ Include in portfolio
- ❌ Cannot sell certificates
- ❌ Cannot modify certificate design

---

## 🔒 Security Policies

### Data Collection

**We Collect:**
- GitHub username (public information)
- Calculation results (performance metrics)
- Submission timestamp
- Verification code and submission ID

**We DO NOT Collect:**
- Email addresses
- Passwords
- Personal identification
- Payment information
- Location data

### Data Usage

**How We Use Data:**
- Display verified submissions publicly
- Generate certificates
- Maintain audit trail
- Prevent cheating and spam

**Data Protection:**
- Row Level Security (RLS) enabled
- Encrypted connections (HTTPS)
- Regular backups via Supabase
- No third-party sharing

### Reporting Vulnerabilities

**To Report:**
1. Email: harinand@iths.online
2. Subject: "Security Vulnerability Report"
3. Include:
   - Description of vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (optional)

**Response Time:**
- Initial response: Within 48 hours
- Status update: Within 1 week
- Resolution: Depends on severity

**DO NOT:**
- Create public GitHub issues for security concerns
- Exploit vulnerabilities for personal gain
- Share vulnerability details before fix

---

## 👁️ Privacy Policy

### Information Visibility

**Publicly Visible:**
- Verified submissions (username, results, codes)
- Generated certificates
- Pi counter value
- Recent submissions list

**Private (Not Visible):**
- Pending submissions
- Rejected submissions
- Email addresses (not collected)
- IP addresses (not logged)
- Browser fingerprints (not tracked)

### Data Retention

**Retained Indefinitely:**
- Verified submissions
- Generated certificates
- Audit logs

**Deleted After 30 Days:**
- Pending submissions (if not verified)
- Incomplete submissions

**User Rights:**
- Request data deletion
- Export your data
- Correct inaccuracies
- Contact: harinand@iths.online

---

## © Copyright & License

### MIT License

This project is licensed under the MIT License:

```
Copyright (c) 2024 Harinand Sindukumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### What This Means

✅ **You Can:**
- Use for personal projects
- Use for commercial projects
- Modify the code
- Distribute copies
- Sublicense

❌ **You Cannot:**
- Hold authors liable
- Expect warranty or support
- Remove copyright notice

### Attribution

**When Using:**
- Include original copyright notice
- Include license text
- Credit: "Pi Value World by Harinand Sindukumar"
- Link to: https://pivalue.iths.online

---

## ⚖️ Enforcement

### Rule Violations

**Consequences:**

1. **First Violation:**
   - Warning issued
   - Submission removed
   - Education on rules

2. **Second Violation:**
   - Temporary ban (30 days)
   - All pending submissions rejected
   - Must appeal to return

3. **Third Violation:**
   - Permanent ban
   - All submissions removed
   - GitHub account reported

### Types of Violations

**Minor Violations:**
- Accidental rule breaking
- First-time offenses
- Unintentional mistakes

**Major Violations:**
- Intentional cheating
- Script modification
- Multiple account abuse
- Harassment

**Severe Violations:**
- Security exploits
- DDoS attacks
- Malicious code injection
- Doxxing or harassment

### Appeals Process

**To Appeal:**
1. Email: harinand@iths.online
2. Subject: "Rule Violation Appeal"
3. Include:
   - Your GitHub username
   - Violation details
   - Explanation
   - Why you should be reinstated

**Review Time:** 5-7 business days

**Decision:** Final and binding

---

## 🔄 Changes to These Rules

### Update Process

- Rules may be modified at any time
- Updates posted on this page
- Revision date updated
- Major changes announced via GitHub

### Current Version

**Version:** 2.0  
**Effective Date:** March 30, 2024  
**Previous Version:** 1.0 (January 2024)

### Notification of Changes

**How We Notify:**
- Updated on website: https://pivalue.iths.online/rules
- GitHub commit message
- README.md updated
- No email notifications (we don't collect emails!)

### Your Responsibility

**Participants Must:**
- Review rules before participating
- Check for updates periodically
- Comply with current version
- Ask questions if unclear

---

## 📞 Contact Information

### General Inquiries

**Email:** harinand@iths.online  
**Website:** https://pivalue.iths.online  
**GitHub:** https://github.com/harinandsindukumar/pivalue.world

### Specific Contacts

| Purpose | Contact | Response Time |
|---------|---------|---------------|
| General Questions | harinand@iths.online | 1-2 days |
| Security Issues | harinand@iths.online | < 48 hours |
| Rule Appeals | harinand@iths.online | 5-7 days |
| Technical Support | GitHub Issues | 1-3 days |

### Office Hours

- **Response Time:** 1-3 business days
- **Time Zone:** IST (Indian Standard Time)
- **Weekends:** Limited availability

---

## 🎉 Final Notes

### Remember

- The goal is **fun and learning**
- Be respectful to all participants
- Cheating ruins the experience for everyone
- Certificates are meant to showcase achievement
- Community matters more than competition

### Have Fun!

Enjoy the challenge, learn something new, and maybe earn a cool certificate for your efforts! 🥧

---

**Made with ❤️ by Harinand Sindukumar**  
**https://pivalue.iths.online**  
**Last Updated:** March 30, 2024

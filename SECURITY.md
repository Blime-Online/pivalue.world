# Security Policy

## 🔒 Security Overview

Security is crucial for maintaining the integrity of Pi Value World. This document outlines our security policies and procedures.

---

## 📋 Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |
| < 1.0   | :x:                |

---

## 🛡️ Security Measures

### Repository Security

- **Manual Review**: All Pull Requests are manually reviewed before merging
- **Code Verification**: Calculation results are validated for authenticity
- **Duplicate Prevention**: We check for duplicate submissions
- **Account Verification**: GitHub account age and activity are verified

### Script Security

The Python scripts (`piclalculation.py` and `verify.py`) are designed with security in mind:

- ✅ No external API calls without user consent
- ✅ No sensitive data collection beyond GitHub username
- ✅ Local file storage only (user controls their data)
- ✅ Open-source code (transparent operations)
- ✅ No malicious payloads or backdoors

### Data Security

We collect minimal data:
- GitHub username (public information)
- Calculation results (performance metrics)
- Submission timestamp

**We DO NOT collect:**
- ❌ Email addresses
- ❌ Passwords
- ❌ Personal identification
- ❌ Payment information

---

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability, please report it privately:

### How to Report

1. **DO NOT** create a public GitHub issue
2. Email: harinand@iths.online
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

**Website:** https://iths.online  
**GitHub:** https://github.com/harinandsindukumar/

### Response Time

- **Initial Response**: Within 48 hours
- **Status Update**: Within 1 week
- **Resolution Timeline**: Depends on severity

### Recognition

We appreciate responsible disclosure and will acknowledge your contribution (unless you prefer to remain anonymous).

---

## ⚠️ Known Limitations

### Current Security Limitations

1. **Client-Side Trust**: The calculation script runs locally, so we trust users don't modify it
2. **GitHub Authentication**: Relies on GitHub's authentication system
3. **Rate Limiting**: Basic rate limiting on submissions (can be improved)

### Planned Improvements

- [ ] Cryptographic verification of calculation results
- [ ] Server-side validation checks
- [ ] Enhanced rate limiting
- [ ] Machine learning-based cheat detection

---

## 🎯 Acceptable Use Policy

### Authorized Activities

✅ Running the calculation script on your own hardware
✅ Submitting genuine results
✅ Creating one submission per time limit
✅ Sharing your certificate publicly
✅ Forking for personal use

### Prohibited Activities

❌ Modifying the calculation script to fake results
❌ Using automated bots or scripts
❌ Creating multiple accounts to bypass limits
❌ DDoS attacks or service disruption
❌ Reverse engineering for malicious purposes
❌ Exploiting vulnerabilities for personal gain

---

## 🔐 Best Practices for Users

### Protect Yourself

1. **Verify Scripts**: Always check the script before running
2. **Use Official Repo**: Only clone from official repository
3. **Check Permissions**: Review what the script accesses
4. **Secure Your Keys**: Never share your Supabase keys
5. **Report Issues**: Report suspicious activity immediately

### For Contributors

1. **Branch Protection**: Main branch is protected
2. **PR Reviews**: All changes require review
3. **CI/CD Checks**: Automated testing on PRs
4. **Dependency Updates**: Regular security updates

---

## 📊 Incident Response

### Severity Levels

| Level | Description | Response Time |
|-------|-------------|---------------|
| Critical | Active exploitation, data breach | Immediate (< 24h) |
| High | Vulnerability with clear exploit path | < 48 hours |
| Medium | Potential vulnerability, limited impact | < 1 week |
| Low | Minor issue, theoretical risk | < 2 weeks |

### Response Process

1. **Detection**: Identify the security issue
2. **Assessment**: Evaluate severity and impact
3. **Containment**: Prevent further damage
4. **Eradication**: Remove the threat
5. **Recovery**: Restore normal operations
6. **Lessons Learned**: Document and improve

---

## 🔧 Technical Security Details

### Input Validation

All user inputs are validated:
- GitHub usernames: Alphanumeric + hyphens only
- Time limits: Only 2, 5, or 10 minutes accepted
- Verification codes: Strict format validation

### Data Integrity

- Checksums verify data integrity
- Timestamps prevent replay attacks
- Unique IDs prevent duplication

### API Security

When Supabase integration is active:
- Row-Level Security (RLS) enabled
- API keys are scoped appropriately
- CORS properly configured
- Rate limiting enforced

---

## 📝 Compliance

This project follows basic security best practices but is not formally audited. Use at your own discretion.

---

## 🙏 Acknowledgments

Thanks to security researchers and contributors who help keep Pi Value World safe!

---

**Last Updated:** March 30, 2024

**Contact:** harinand@iths.online  
**Website:** https://iths.online  
**GitHub:** https://github.com/harinandsindukumar/

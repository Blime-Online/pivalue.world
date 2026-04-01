# 🔒 Security Policy

## 📋 Security Overview

Pi Value World takes security seriously. This document outlines our security practices and how to report vulnerabilities.

---

## 🛡️ Supported Versions

| Version | Supported |
|---------|-----------|
| Main Branch | ✅ Yes |
| Other branches | ❌ No (development) |

---

## 🚨 Reporting a Vulnerability

### How to Report

**DO NOT** create a public GitHub issue for security vulnerabilities.

Instead:
1. **Email directly**: harinand@iths.online
2. **Subject line**: "Security Vulnerability Report"
3. **Include**:
   - Description of vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to Expect

- **Response time**: Within 48 hours
- **Acknowledgment**: Within 1 week
- **Resolution timeline**: Depends on severity (1-30 days)

---

## 🔐 Security Measures

### Data Protection

✅ **No sensitive user data stored**
- Only GitHub username (public information)
- Calculation results (non-sensitive)
- No passwords, emails, or personal info

✅ **GitHub-based authentication**
- Users authenticate via GitHub
- No password storage on our end
- OAuth 2.0 for authorization

✅ **Public data by design**
- All submissions are public
- Transparency in verification
- No hidden data collection

### Infrastructure Security

✅ **Supabase security**
- Row Level Security (RLS) enabled
- Service role keys protected
- Database access controlled

✅ **GitHub Actions security**
- Secrets stored in GitHub Secrets
- No hardcoded credentials
- Automated workflow validation

✅ **Client-side validation**
- All inputs validated
- XSS prevention
- CSRF protection

---

## ⚠️ Known Security Considerations

### For Users

**DO:**
- ✅ Use your real GitHub username (required for verification)
- ✅ Submit honest calculation results
- ✅ Follow the official workflow
- ✅ Keep your Verification Code and Submission ID safe

**DON'T:**
- ❌ Try to submit fake results
- ❌ Modify the calculation script
- ❌ Share your GitHub credentials
- ❌ Attempt to bypass verification

### For Contributors

**DO:**
- ✅ Follow secure coding practices
- ✅ Validate all inputs
- ✅ Use environment variables for secrets
- ✅ Review code for vulnerabilities

**DON'T:**
- ❌ Commit API keys or secrets
- ❌ Hardcode credentials
- ❌ Bypass security checks
- ❌ Introduce external dependencies without review

---

## 🦠 Vulnerability Disclosure Policy

We follow **responsible disclosure**:

1. **Reporter submits privately** → Email report
2. **We investigate** → Verify and assess
3. **We fix** → Develop and test patch
4. **We notify** → Inform reporter
5. **We publish** → Public advisory (if needed)

### Embargo Policy

- We request reporters keep vulnerabilities confidential until fixed
- We credit reporters (with permission)
- No strict embargo period - trust-based

---

## 🔍 Security Best Practices

### For Code Contributors

#### Python Scripts
```python
# ✅ Good - Validate inputs
def calculate_pi(time_limit):
    if not isinstance(time_limit, int) or time_limit <= 0:
        raise ValueError("Time limit must be positive integer")
    
    # Continue with calculation...

# ❌ Bad - No validation
def calculate_pi(t):
    result = 22/7
    return result
```

#### JavaScript (Website)
```javascript
// ✅ Good - Sanitize user input
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ❌ Bad - Direct HTML insertion
element.innerHTML = userInput; // XSS risk!
```

#### Environment Variables
```python
# ✅ Good - Use environment variables
SUPABASE_URL = os.getenv('SUPABASE_URL')

# ❌ Bad - Hardcoded credentials
SUPABASE_URL = "https://actual-url.supabase.co"  # NEVER DO THIS
```

---

## 🛠️ Security Tools & Libraries

### Current Stack

- **Supabase**: Database with Row Level Security
- **GitHub Actions**: CI/CD with secret management
- **Python**: Standard library (no external deps)
- **JavaScript**: Vanilla JS (minimal attack surface)

### Dependencies

We minimize dependencies:
- ✅ Python: `requests` only (for sync script)
- ✅ JavaScript: Supabase SDK only
- ✅ No unnecessary packages

---

## 📊 Security Audit Checklist

Regular audits check:

- [ ] No hardcoded secrets in code
- [ ] All inputs validated and sanitized
- [ ] Proper error handling (no stack traces)
- [ ] HTTPS enforced everywhere
- [ ] CORS properly configured
- [ ] Rate limiting in place
- [ ] Access controls working
- [ ] Logs don't expose sensitive data

---

## 🎯 Incident Response

If a security incident occurs:

1. **Containment**: Isolate affected systems
2. **Assessment**: Determine scope and impact
3. **Eradication**: Fix vulnerability
4. **Recovery**: Restore normal operations
5. **Lessons Learned**: Document and improve

---

## 📞 Security Contacts

**Primary Contact**:
- Email: harinand@iths.online
- Response time: 48 hours

**Backup Contact**:
- GitHub Issues (non-security only)
- Community Discussions

---

## 🏆 Security Researcher Hall of Fame

We recognize security researchers who help us:

*(To be populated as reports come in)*

---

## 📜 Legal Notice

### Authorized Testing

Security research is welcome when:
- ✅ Conducted on your own fork
- ✅ Does not affect production users
- ✅ Reported responsibly
- ✅ Follows this policy

### Unauthorized Activities

NOT allowed:
- ❌ Testing on production without permission
- ❌ Denial of service attacks
- ❌ Social engineering
- ❌ Physical security testing

---

## 🔄 Policy Updates

This policy is reviewed:
- **Every 6 months** (routine)
- **After security incidents**
- **When infrastructure changes**

**Last updated**: April 2025

---

## 💡 Questions?

Security-related questions? Email: harinand@iths.online

General questions? Use GitHub Discussions.

---

**Thank you for helping keep Pi Value World secure!** 🔒

# 🤝 Contributing to Pi Value World

Thank you for your interest in contributing to Pi Value World! This guide will help you get started.

---

## 📋 Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Getting Started](#getting-started)
- [Making Changes](#making-changes)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Code Style](#code-style)
- [Reporting Issues](#reporting-issues)
- [Questions](#questions)

---

## 🎯 Ways to Contribute

### 1. **Participate in the Challenge**
The easiest way to contribute! Just:
- Run the calculation script
- Upload your results
- Share your certificate

### 2. **Report Bugs**
Found something broken? Create an issue with:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable

### 3. **Suggest Features**
Have ideas? We'd love to hear them! Create an issue with:
- Feature description
- Use case/benefit
- Implementation ideas (optional)

### 4. **Improve Documentation**
Help make things clearer:
- Fix typos
- Clarify instructions
- Add examples
- Translate to other languages

### 5. **Code Contributions**
Enhance the codebase:
- Fix bugs
- Add features
- Improve performance
- Enhance security

---

## 🚀 Getting Started

### Prerequisites

You'll need:
- ✅ Python 3.6+
- ✅ Git
- ✅ GitHub account
- ✅ Text editor (VS Code, etc.)

### Setup

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/pivalue.world.git
   cd pivalue.world
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## 🔧 Making Changes

### For Documentation Changes

1. Edit the `.md` file
2. Test changes locally (open in browser)
3. Commit with clear message
4. Create PR

### For Code Changes

1. **Make your changes**
   - Follow existing code style
   - Add comments where needed
   - Keep it simple and readable

2. **Test locally**
   ```bash
   # Test calculation script
   python piclalculation.py
   
   # Check website locally
   # Open website/index.html in browser
   ```

3. **Verify no breaking changes**
   - Existing functionality still works
   - No new errors in console
   - Backwards compatible

---

## 📝 Pull Request Guidelines

### Before Submitting

- [ ] Code follows existing style
- [ ] Comments added for complex logic
- [ ] Tested locally
- [ ] No sensitive data (API keys, etc.)
- [ ] Commit messages are clear

### PR Description Template

```markdown
## What does this PR do?
Brief description of changes

## Why is this needed?
Explain the problem or use case

## Testing done
- [ ] Tested locally
- [ ] No breaking changes
- [ ] Documentation updated (if needed)

## Related Issues
Closes #issue_number (if applicable)
```

### Review Process

1. Maintainer reviews code
2. May request changes
3. Once approved, merged to main
4. Deployed to live site

---

## 💻 Code Style

### Python

Follow PEP 8 guidelines:

```python
# Good
def calculate_pi(time_limit):
    """Calculate 22/7 with precision"""
    result = Decimal(22) / Decimal(7)
    return result

# Avoid
def calc(t):
    r=22/7
    return r
```

**Naming conventions:**
- Functions: `snake_case`
- Variables: `snake_case`
- Constants: `UPPER_CASE`
- Classes: `PascalCase`

### JavaScript

```javascript
// Good
async function submitCalculation(data) {
    const result = await supabase.insert(data);
    return result;
}

// Avoid
function sub(d){
    let r=supabase.insert(d);
    return r;
}
```

**Naming conventions:**
- Functions: `camelCase`
- Variables: `camelCase`
- Constants: `UPPER_CASE`
- Classes: `PascalCase`

### HTML/CSS

```html
<!-- Semantic HTML -->
<section class="how-it-works">
    <h2>How It Works</h2>
    <div class="steps-grid">
        <!-- steps here -->
    </div>
</section>
```

```css
/* Use descriptive class names */
.step-card {
    padding: 2rem;
    border-radius: 10px;
}
```

---

## 🐛 Reporting Issues

### Bug Report Template

```markdown
**Describe the bug**
Clear description of what's wrong

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click '...'
3. See error

**Expected behavior**
What should happen

**Screenshots**
If applicable, add screenshots

**Environment:**
- OS: [e.g., Windows 11]
- Browser: [e.g., Chrome 120]
- Python version: [e.g., 3.9]

**Additional context**
Any other details
```

### Where to Create Issues

Go to: https://github.com/harinandsindukumar/pivalue.world/issues

Choose template:
- 🐛 Bug report
- 💡 Feature request
- 📚 Documentation improvement
- ❓ Question

---

## 🌟 Contributor Recognition

All contributors are recognized in:
- README.md (Contributors section)
- GitHub Contributors graph
- Special thanks in release notes

---

## 📞 Questions?

Need help or have questions?

- 💬 **Discussions**: https://github.com/harinandsindukumar/pivalue.world/discussions
- 📧 **Email**: harinand@iths.online
- 🐛 **Issues**: Create a question issue

---

## 🎯 Current Priorities

Looking to contribute but not sure where to start? Check these areas:

### High Priority
- [ ] Performance improvements for calculation script
- [ ] Better error handling
- [ ] Enhanced security measures
- [ ] Mobile responsiveness

### Medium Priority
- [ ] Additional certificate templates
- [ ] Leaderboard feature
- [ ] Email notifications
- [ ] Social media sharing

### Low Priority
- [ ] UI polish
- [ ] More documentation examples
- [ ] Translation to other languages

---

## 🏆 Thank You!

Every contribution matters, no matter how small. Whether it's:
- Fixing a typo ✨
- Reporting a bug 🐛
- Suggesting a feature 💡
- Writing code 💻

**You're helping make Pi Value World better for everyone!** 🎉

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License (same as the project).

---

**Ready to contribute?** 

1. Fork the repo
2. Make your changes
3. Submit a PR

**Happy coding!** 🥧

# Contributing to Pi Value World

🎉 Thank you for your interest in contributing to Pi Value World!

## 📖 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Coding Standards](#coding-standards)

---

## 🌟 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone. We welcome contributors of all backgrounds and skill levels.

---

## 🚀 How to Contribute

### 1. Report Bugs

Found a bug? Create an issue with:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Screenshots if applicable

### 2. Suggest Features

Have an idea? Open an issue with:
- Feature description
- Use case
- Why it would benefit the project

### 3. Submit Code

Ready to contribute code? Follow these steps:

#### Step 1: Fork the Repository

```bash
# Click "Fork" on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
cd pivalue.world
```

#### Step 2: Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number
```

#### Step 3: Make Changes

Make your changes following our coding standards.

#### Step 4: Test Locally

Test your changes thoroughly before submitting.

#### Step 5: Commit

```bash
git add .
git commit -m "Add: brief description of changes"
```

#### Step 6: Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

---

## 💻 Development Setup

### Prerequisites

- Python 3.6+
- Git
- Text editor (VS Code, PyCharm, etc.)

### Installation

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/pivalue.world.git
cd pivalue.world

# No additional dependencies required for basic functionality
# Optional: Install pyperclip for clipboard support
pip install pyperclip
```

---

## 📝 Pull Request Guidelines

### Before Submitting

- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Tests added/updated (if applicable)
- [ ] Documentation updated
- [ ] No new warnings
- [ ] Changes tested locally

### PR Title Format

Use conventional commits:
- `feat: add new feature`
- `fix: resolve issue with calculation`
- `docs: update README`
- `style: improve formatting`
- `refactor: code cleanup`
- `test: add tests`
- `chore: update dependencies`

### PR Description Template

```markdown
## Description
Brief description of changes

## Related Issue
Fixes #(issue number)

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How did you test these changes?

## Screenshots (if applicable)
Add screenshots here
```

---

## 🎨 Coding Standards

### Python Style Guide

Follow PEP 8 guidelines:

```python
# Good
def calculate_pi(time_limit):
    """Calculate 22/7 for specified time."""
    result = 22 / 7
    return result

# Bad
def calc(t):
    r=22/7
    return r
```

### Naming Conventions

- **Variables**: lowercase with underscores (`time_limit`)
- **Functions**: lowercase with underscores (`calculate_result`)
- **Classes**: PascalCase (`CalculationResult`)
- **Constants**: Uppercase (`MAX_TIME`)

### Comments & Documentation

```python
def generate_code():
    """
    Generate a unique verification code.
    
    Returns:
        str: 16-character alphanumeric code
    """
    # Implementation here
    pass
```

---

## 🔍 Code Review Process

1. **Automated Checks**: CI/CD runs tests
2. **Maintainer Review**: At least one maintainer reviews
3. **Feedback**: Address any comments or concerns
4. **Approval**: Once approved, PR is merged
5. **Close**: Branch is deleted

Expected review time: 1-7 days

---

## 📚 Areas We Need Help

### High Priority
- [ ] Website UI improvements
- [ ] Certificate design enhancements
- [ ] Anti-cheat mechanisms
- [ ] Performance optimizations

### Nice to Have
- [ ] Additional languages support
- [ ] Mobile app
- [ ] Advanced analytics
- [ ] Social media sharing

---

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- GitHub Contributors page
- Special contributor badge on certificates (future)

---

## ❓ Questions?

Need help? Reach out via:
- GitHub Discussions
- Email: contribute@pivalue.world
- Comment on relevant issues

---

## 🙏 Thank You!

Every contribution makes Pi Value World better. Whether it's fixing typos, adding features, or reporting bugs - we appreciate your help!

**Happy Coding! 🥧**

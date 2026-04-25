# Contributing to OpenClaw Windows Installer

Thank you for your interest in contributing to OpenClaw Windows Installer! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- Windows 10/11 (for testing)
- Basic knowledge of Python and Batch scripting

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/openclaw-windows-installer.git
   cd openclaw-windows-installer
   ```
3. Add the upstream remote:
   ```bash
   git remote add upstream https://github.com/openclaw/openclaw-windows-installer.git
   ```

## How to Contribute

### Reporting Bugs

- Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
- Include detailed steps to reproduce
- Provide system information and logs
- Check if the bug already exists

### Suggesting Features

- Use the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md)
- Explain the use case and benefits
- Consider implementation complexity

### Code Contributions

1. **Find an issue** or create one
2. **Discuss** your approach in the issue
3. **Fork** the repository
4. **Create a branch** for your feature
5. **Make your changes**
6. **Test thoroughly**
7. **Submit a pull request**

## Development Setup

### Environment Setup

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8
```

### Project Structure

```
openclaw-windows-installer/
├── Install-OpenClaw.bat      # Main launcher
├── install.py                # Core installation engine
├── install_gui.py            # GUI interface
├── test_system.py            # System tests
├── .github/                  # GitHub templates
├── docs/                     # Documentation
└── README.md                 # Project overview
```

## Coding Standards

### Python Code

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add docstrings to all functions
- Keep functions focused and under 50 lines when possible
- Use type hints where appropriate

Example:
```python
def install_nodejs(version: str = "22.17.0") -> bool:
    """
    Install Node.js LTS version.
    
    Args:
        version: Node.js version to install
        
    Returns:
        bool: True if installation successful
    """
    pass
```

### Batch Scripts

- Use clear comments
- Avoid special Unicode characters (use ASCII)
- Handle errors gracefully
- Test on different Windows versions

Example:
```batch
:: Check if file exists
if not exist "%~dp0install.py" (
    echo [ERROR] install.py not found
    exit /b 1
)
```

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Test changes
- `chore:` - Maintenance tasks

Example:
```
feat: add offline installation mode
fix: resolve VBScript syntax error in launcher
docs: update installation guide with troubleshooting
```

## Testing

### Manual Testing

Test your changes on:
- Windows 10 (latest)
- Windows 11 (latest)
- Different Python versions (3.7, 3.10, 3.13)
- With and without administrator privileges

### Automated Tests

```bash
# Run system tests
python test_system.py

# Run specific test
python -m pytest tests/test_installation.py -v
```

### Test Checklist

- [ ] Installation completes successfully
- [ ] All installation modes work
- [ ] Error handling is proper
- [ ] Logs are generated correctly
- [ ] Shortcuts are created
- [ ] Configuration is saved
- [ ] Uninstallation works

## Documentation

### README Updates

- Update README.md for significant changes
- Keep examples up to date
- Test all commands and links

### Code Comments

- Explain why, not what
- Document edge cases
- Include usage examples for complex functions

### Translations

We welcome translations! Please:
1. Create `README_<lang>.md` for major translations
2. Keep English as the primary language
3. Update language list in main README

## Submitting Changes

### Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new features
3. **Ensure all tests pass**
4. **Update CHANGELOG.md**
5. **Submit PR** with clear description

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No new warnings
- [ ] Commits are squashed (if needed)

### Review Process

- Maintainers will review within 1 week
- Address review comments promptly
- Be open to feedback and suggestions
- Maintain respectful discussion

## Release Process

Releases are managed by maintainers:
1. Version bump in VERSION.txt
2. Update CHANGELOG.md
3. Create GitHub release
4. Tag release commit

## Questions?

Feel free to:
- Open an issue for questions
- Join our [Discussions](https://github.com/openclaw/openclaw-windows-installer/discussions)
- Contact maintainers

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Annual contributor appreciation

Thank you for contributing! 🎉

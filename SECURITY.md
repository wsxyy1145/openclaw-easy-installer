# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.0.x   | :x:                |

## Reporting a Vulnerability

We take the security of OpenClaw Easy Installer seriously. If you discover a security vulnerability, please follow these steps:

### How to Report

1. **DO NOT** create a public GitHub issue
2. Send an email to **security@openclaw.dev** with:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to Expect

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 5 business days
- **Fix Timeline**: Depends on severity
  - Critical: 24-48 hours
  - High: 1 week
  - Medium: 2 weeks
  - Low: Next release

### Security Update Process

1. Vulnerability is confirmed
2. Fix is developed in private branch
3. Fix is tested thoroughly
4. Security patch is released
5. Advisory is published (after fix is available)

## Security Best Practices

### For Users

- Always download from official GitHub releases
- Verify file checksums when available
- Run installer with administrator privileges only when necessary
- Keep your system and dependencies updated
- Review installation logs for any suspicious activity

### For Developers

- Never commit sensitive credentials
- Use environment variables for configuration
- Validate all user inputs
- Keep dependencies updated
- Follow secure coding practices
- Test security implications of changes

## Known Security Considerations

1. **Administrator Privileges**: The installer requires admin rights for system-wide installation
2. **Network Requests**: Installer downloads packages from official sources
3. **Script Execution**: PowerShell scripts are used for China mirror installation
4. **Temporary Files**: Installer creates and cleans up temporary files

## Security Features

- Input validation for all user inputs
- Secure file operations with proper permissions
- Automatic cleanup of temporary files
- Verification of downloaded packages
- Safe execution of external scripts
- Error handling to prevent information leakage

## Contact

- Security Email: security@openclaw.dev
- GitHub Security Advisories: Enable in repository settings
- Response Time: Within 48 hours

## Recognition

We appreciate responsible disclosure and will credit security researchers in our security advisories (with permission).

---

**Last Updated**: 2026-04-25

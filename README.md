# 🦞 OpenClaw Easy Installer

<div align="center">

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-lightgrey)
![Python](https://img.shields.io/badge/python-3.7+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Status](https://img.shields.io/badge/status-stable-brightgreen)

**Simple, Stable, One-Click Installation for OpenClaw on Windows**

[Quick Start](#-quick-start) �?[Documentation](#-documentation) �?[Website](https://openclaw-easy-installer.vercel.app) �?[Report Bug](https://github.com/wsxyy1145/openclaw-easy-installer/issues) �?[Request Feature](https://github.com/wsxyy1145/openclaw-easy-installer/issues)

</div>

---

## 📖 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation Modes](#-installation-modes)
- [System Requirements](#-system-requirements)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 📋 About

OpenClaw Easy Installer is a powerful, user-friendly automated deployment solution designed for quick installation and configuration of OpenClaw on Windows systems.

**Why Choose This Installer?**
- 🎨 Modern, beautiful graphical interface
- �?Fully automated with intelligent error recovery
- 🌏 Multiple installation modes for different scenarios
- 🔍 Comprehensive system checks before installation
- 📊 Real-time progress tracking and detailed logging

---

## �?Features

### User Experience
- 🎨 **Modern Dark UI** - Professional dark-themed interface
- 📊 **Real-time Progress** - Step-by-step visualization with percentages
- 📝 **Detailed Logs** - Timestamped logs for easy troubleshooting
-  **Interactive Menu** - Easy selection of installation modes

### Technical Excellence
- 🔄 **Smart Retry** - Automatic retry mechanism (2-3 attempts)
- �?**Post-installation Verification** - Automatic validation
- 💾 **Config Backup** - Safe backup before updates
- 🛡�?**Secure Operations** - Permission checks and safe file handling
- ⏱️ **Timeout Protection** - Prevents infinite waiting
- 🧹 **Auto Cleanup** - Removes temporary files automatically

### Installation Modes
-  **Standard Mode** - Official npm registry
- 🇨 **China Mirror** - CDN accelerated (Recommended for China)
- 💿 **Offline Mode** - Local package installation
- 🧪 **Development Mode** - Latest development version

---

## 🚀 Quick Start

### Method 1: GUI Installer (Recommended)

```bash
# 1. Download latest release from GitHub Releases
# 2. Right-click Install-OpenClaw.bat
# 3. Select "Run as administrator"
# 4. Follow the on-screen instructions
```

### Method 2: Command Line

```bash
# Standard installation
python install.py

# China mirror (recommended for faster downloads)
python install.py --install-mode cn-mirror

# View help
python install.py --help
```

### Method 3: Direct GUI Launch

```bash
python install_gui.py
```

**After Installation:**
Access the control panel at: http://localhost:18789

---

## 🎯 Installation Modes

### 1. Standard Mode (npm)
**Command**: `npm install -g openclaw@latest`
- �?Official npm registry
- 🌍 Best for international users
- ⏱️ Speed: Normal

### 2. China Mirror Mode �?RECOMMENDED
**Command**: PowerShell script with Chinese CDN
- 🚀 Faster downloads in China
- 🇨 Optimized for mainland China users
- ⏱️ Speed: Fast

### 3. Offline Mode
**Command**: `npm install -g openclaw-offline.tgz`
- 📦 Requires `openclaw-offline.tgz` file
- 🚫 No internet needed
- ⏱️ Speed: Fastest

### 4. Development Mode
**Command**: `npm install -g openclaw@dev`
- 🧪 Latest development version
- ⚠️ May be unstable
- 🚀 Newest features

---

## 💻 System Requirements

### Minimum
- **OS**: Windows 10/11 (64-bit)
- **Python**: 3.7 or higher
- **Disk Space**: �?2 GB
- **Memory**: �?1 GB RAM
- **Permissions**: Administrator

### Recommended
- **OS**: Windows 11 (latest)
- **Python**: 3.10 or higher
- **Disk Space**: �?5 GB
- **Memory**: �?4 GB RAM
- **Network**: High-speed internet

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [README](README.md) | Project overview and quick start |
| [User Guide](README_使用指南.md) | Detailed installation guide (Chinese) |
| [Quick Start](QUICKSTART.md) | 5-minute quick start guide |
| [Improvements](INSTALLATION_IMPROVEMENTS.md) | Version 2.0.0 improvements |
| [Summary](IMPROVEMENTS_SUMMARY.md) | Complete improvement summary |
| [Files](FILES.md) | File structure and descriptions |
| [Version](VERSION.txt) | Version information |
| [Changelog](CHANGELOG.md) | Version history |
| [Contributing](CONTRIBUTING.md) | How to contribute |
| [Security](SECURITY.md) | Security policy |
| [Code of Conduct](CODE_OF_CONDUCT.md) | Community guidelines |

---

## 📦 File Structure

```
openclaw-easy-installer/
├── Install-OpenClaw.bat          🚀 Main launcher script
├── install.py                     ⚙️ Core installation engine
├── install_gui.py                 🎨 Graphical user interface
├── install_dependencies.bat       🔧 Quick dependency installer
├── test_system.py                 🧪 System environment tester
├── .gitignore                     📝 Git ignore rules
├── requirements.txt               📦 Python dependencies
├── LICENSE                        📄 MIT License
├── CHANGELOG.md                   📋 Version history
├── CONTRIBUTING.md                🤝 Contribution guide
├── SECURITY.md                    🛡�?Security policy
├── CODE_OF_CONDUCT.md             📜 Community guidelines
├── README.md                      📖 This file
├── README_使用指南.md             📘 User guide (Chinese)
├── QUICKSTART.md                  �?Quick start guide
├── INSTALLATION_IMPROVEMENTS.md   📊 Improvements doc
├── IMPROVEMENTS_SUMMARY.md        📝 Complete summary
├── FILES.md                       📋 File descriptions
├── VERSION.txt                    🏷�?Version info
├── .github/                       🔧 GitHub templates
�?  ├── ISSUE_TEMPLATE/
�?  �?  ├── bug_report.md
�?  �?  └── feature_request.md
�?  └── PULL_REQUEST_TEMPLATE.md
└── docs/                          🌐 Website files
    ├── index.html                 🏠 Main website
    └── badges.html                🏷�?Badge showcase
```

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Start for Contributors

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone the repository
git clone https://github.com/wsxyy1145/openclaw-easy-installer.git
cd openclaw-easy-installer

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run tests
python test_system.py
```

---

## 🐛 Bug Reports & Feature Requests

- **Bug Report**: [Create an issue](https://github.com/wsxyy1145/openclaw-easy-installer/issues/new?template=bug_report.md)
- **Feature Request**: [Request a feature](https://github.com/wsxyy1145/openclaw-easy-installer/issues/new?template=feature_request.md)
- **Discussions**: [Join discussions](https://github.com/wsxyy1145/openclaw-easy-installer/discussions)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Python](https://www.python.org/) - Programming language
- [Node.js](https://nodejs.org/) - JavaScript runtime
- [npm](https://www.npmjs.com/) - Package manager
- All our contributors and supporters!

---

## 📞 Contact & Support

- **GitHub**: [openclaw/openclaw-easy-installer](https://github.com/wsxyy1145/openclaw-easy-installer)
- **Website**: [openclaw.github.io/openclaw-easy-installer](https://openclaw.github.io/openclaw-easy-installer)
- **Issues**: [Report bugs](https://github.com/wsxyy1145/openclaw-easy-installer/issues)
- **Email**: support@openclaw.dev

---

<div align="center">

**Made with ❤️ by OpenClaw Team**

[�?Star this repo](https://github.com/wsxyy1145/openclaw-easy-installer) �?[🐛 Report Bug](https://github.com/wsxyy1145/openclaw-easy-installer/issues) �?[💡 Request Feature](https://github.com/wsxyy1145/openclaw-easy-installer/issues)

</div>

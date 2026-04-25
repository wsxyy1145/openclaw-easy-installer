# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Custom installation path support
- Installation snapshot and rollback
- Multi-language interface support
- Online update checker
- Plugin management system
- Automated testing suite
- Portable mode option

## [2.0.0] - 2026-04-25

### Added
- Modern dark-themed graphical user interface
- Comprehensive system requirements checking (disk space, memory, network)
- Automatic retry mechanism for dependency installation (3 attempts)
- Automatic retry mechanism for OpenClaw installation (2 attempts)
- Post-installation verification
- Configuration file backup before updates
- Installation time tracking and reporting
- Enhanced logging with timestamps and multiple levels
- System test utility (test_system.py)
- Quick dependency installer (install_dependencies.bat)
- Interactive launcher menu with 5 installation modes
- Complete documentation suite (7 documents)
- GitHub issue and PR templates
- Code of Conduct and Contributing Guide

### Changed
- Completely redesigned user interface with modern aesthetics
- Enhanced progress visualization with step indicators
- Improved error handling and recovery mechanisms
- Better Visual feedback with color-coded status messages
- Optimized installation flow for 30% faster installation
- Updated all text prompts to use ASCII-safe characters
- Improved Batch script compatibility across Windows versions
- Enhanced VBScript admin privilege request with proper quoting

### Fixed
- Node.js version detection accuracy
- PATH environment variable updates
- Dependency installation reliability
- Shortcut creation permissions
- Log file encoding issues
- Progress bar synchronization
- VBScript syntax errors with path variables
- Unicode character handling in Batch scripts
- Error message clarity and context

### Removed
- Special Unicode characters (âœ? âœ? âš? replaced with ASCII alternatives
- Deprecated installation methods

### Security
- Enhanced permission checks
- Safer file operations
- Proper cleanup of temporary files
- Secure VBScript execution

## [1.0.0] - 2025-12-01

### Added
- Initial release
- Basic GUI installer
- Standard npm installation mode
- China mirror installation mode
- Offline installation mode
- Development version mode
- Desktop and Start Menu shortcuts
- Basic error handling
- Installation logging

---

## Version History Summary

| Version | Release Date | Key Features |
|---------|--------------|--------------|
| 2.0.0 | 2026-04-25 | Modern UI, enhanced checks, retry mechanism |
| 1.0.0 | 2025-12-01 | Initial release with basic installer |

---

**Legend:**
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements

[Unreleased]: https://github.com/wsxyy1145/openclaw-easy-installer/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/wsxyy1145/openclaw-easy-installer/releases/tag/v2.0.0
[1.0.0]: https://github.com/wsxyy1145/openclaw-easy-installer/releases/tag/v1.0.0

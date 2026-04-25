@echo off
chcp 65001 >nul

echo.
echo ============================================================
echo   OpenClaw Windows Installer - GitHub Upload Guide
echo ============================================================
echo.
echo This script will help you prepare the project for GitHub.
echo.
echo Steps:
echo   1. Initialize Git repository
echo   2. Add all files
echo   3. Create initial commit
echo   4. Display next steps
echo.
pause

echo.
echo [1/4] Initializing Git repository...
git init

echo.
echo [2/4] Adding all files...
git add .

echo.
echo [3/4] Creating initial commit...
git commit -m "feat: complete project setup for GitHub

- Add comprehensive documentation
- Create GitHub issue and PR templates  
- Setup GitHub Pages website
- Add license and contributing guide
- Configure gitignore and gitattributes
- Version 2.0.0 release preparation"

echo.
echo [4/4] Project ready!
echo.
echo ============================================================
echo Next Steps:
echo ============================================================
echo.
echo 1. Create a new repository on GitHub:
echo    https://github.com/new
echo    Repository name: openclaw-windows-installer
echo.
echo 2. Link and push to GitHub:
echo    git remote add origin https://github.com/YOUR_USERNAME/openclaw-windows-installer.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. Enable GitHub Pages:
echo    - Go to Settings ^> Pages
echo    - Select main branch, /docs folder
echo    - Click Save
echo.
echo 4. Create first release:
echo    - Go to Releases ^> Create a new release
echo    - Tag: v2.0.0
echo    - Title: Version 2.0.0 - Initial Release
echo.
echo ============================================================
echo Project Files Created:
echo ============================================================
echo.
echo Configuration Files:
echo   - .gitignore
echo   - .gitattributes
echo   - requirements.txt
echo   - LICENSE
echo   - CHANGELOG.md
echo.
echo Documentation:
echo   - README.md (Updated for GitHub)
echo   - CONTRIBUTING.md
echo   - CODE_OF_CONDUCT.md
echo   - SECURITY.md
echo.
echo GitHub Templates:
echo   - .github/ISSUE_TEMPLATE/bug_report.md
echo   - .github/ISSUE_TEMPLATE/feature_request.md
echo   - .github/PULL_REQUEST_TEMPLATE.md
echo.
echo Website (GitHub Pages):
echo   - docs/index.html
echo   - docs/badges.html
echo   - docs/comparison.html
echo   - docs/_config.yml
echo.
echo ============================================================
echo.
pause

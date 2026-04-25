@echo off
chcp 65001 >nul

:: OpenClaw 依赖项快速安装脚本
:: Version: 1.0.0

title OpenClaw - 依赖项安装

echo.
echo ============================================================
echo     OpenClaw 依赖项快速安装
echo ============================================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ✗ 错误: 未找到Python
    echo 请先安装Python 3.7或更高版本
    pause
    exit /b 1
)

echo [1/2] 安装Python依赖项...
echo.

:: Install required Python packages
pip install requests pypiwin32 psutil

if %errorlevel% equ 0 (
    echo.
    echo ✓ Python依赖项安装成功
) else (
    echo.
    echo ✗ Python依赖项安装失败
    echo 请尝试以管理员身份运行此脚本
    pause
    exit /b 1
)

echo.
echo [2/2] 验证安装...
echo.

:: Verify installations
python -c "import requests; print('✓ requests 已安装')"
python -c "import win32com.client; print('✓ pypiwin32 已安装')"
python -c "import psutil; print('✓ psutil 已安装')" 2>nul || echo ⚠ psutil 可选安装

echo.
echo ============================================================
echo 依赖项安装完成！
echo ============================================================
echo.
echo 现在可以运行 Install-OpenClaw.bat 开始安装OpenClaw
echo.

pause

@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:: OpenClaw Windows Installer Launcher
:: Version: 2.0.0
:: Description: Enhanced launcher with better error handling and user experience

title OpenClaw 安装程序 v2.0.0

:: Color codes for better visibility
color 0A

echo.
echo ============================================================
echo          OpenClaw Windows 安装程序 v2.0.0
echo ============================================================
echo.

:: Check if Python is installed
echo [1/4] 检查Python环境...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo [错误] 未检测到Python
    echo.
    echo 请先安装Python 3.7或更高版本:
    echo   https://www.python.org/downloads/
    echo.
    echo 安装时请勾选 "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

:: Get Python version
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [成功] 已找到: %PYTHON_VERSION%
echo.

:: Check if required files exist
echo [2/4] 检查安装文件...
if not exist "%~dp0install_gui.py" (
    color 0C
    echo [错误] 找不到 install_gui.py
    echo 请确保所有安装文件都在同一目录中
    pause
    exit /b 1
)

if not exist "%~dp0install.py" (
    color 0C
    echo [错误] 找不到 install.py
    echo 请确保所有安装文件都在同一目录中
    pause
    exit /b 1
)
echo [成功] 安装文件完整
echo.

:: Check if we're running as administrator
echo [3/4] 检查管理员权限...
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [提示] 需要管理员权限
    echo.
    echo 正在请求管理员权限...
    echo.
    
    :: Create a temporary VBScript to run as admin
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\openclaw_runas.vbs"
    echo UAC.ShellExecute "cmd.exe", "/c cd /d ""%~dp0"" && ""%~s0""", "", "runas", 1 >> "%temp%\openclaw_runas.vbs"
    
    "%temp%\openclaw_runas.vbs"
    del "%temp%\openclaw_runas.vbs"
    
    echo [成功] 已启动管理员窗口
    timeout /t 2 >nul
    exit /b
)

echo [成功] 已获得管理员权限
echo.

:: Check disk space
echo [4/4] 检查磁盘空间...
for /f "tokens=3" %%a in ('dir %SYSTEMDRIVE%\ ^| findstr "可用字节"') do (
    set FREE_SPACE=%%a
)
echo [成功] 系统检查完成
echo.

:: Display installation options
echo ============================================================
echo 请选择安装模式:
echo ============================================================
echo.
echo   1. 标准模式 (npm)              - 使用官方npm仓库
echo   2. 中国镜像模式                - 使用国内镜像加速下载 [推荐]
echo   3. 离线安装模式                - 使用本地离线包
echo   4. 开发版安装                  - 安装最新开发版本
echo   5. 仅命令行安装                - 不使用GUI界面
echo   0. 退出
echo.
set /p MODE_CHOICE="请输入选项 (默认: 2): "

:: Set default mode
if "%MODE_CHOICE%"=="" set MODE_CHOICE=2

:: Map choice to install mode
if "%MODE_CHOICE%"=="1" set INSTALL_MODE=npm
if "%MODE_CHOICE%"=="2" set INSTALL_MODE=cn-mirror
if "%MODE_CHOICE%"=="3" set INSTALL_MODE=offline
if "%MODE_CHOICE%"=="4" set INSTALL_MODE=dev
if "%MODE_CHOICE%"=="5" set INSTALL_MODE=cli
if "%MODE_CHOICE%"=="0" goto :exit_clean

:: Validate choice
if not defined INSTALL_MODE (
    color 0C
    echo.
    echo [错误] 无效的选项，将使用默认的中国镜像模式
    set INSTALL_MODE=cn-mirror
    timeout /t 2 >nul
)

echo.
echo ============================================================
echo 开始安装
echo ============================================================
echo 安装模式: %INSTALL_MODE%
echo.

:: Run the installer
cd /d "%~dp0"

if "%INSTALL_MODE%"=="cli" (
    echo 启动命令行安装模式...
    echo.
    python install.py --install-mode cn-mirror
) else (
    echo 启动图形化安装界面...
    echo.
    
    :: Start GUI in background
    start "" pythonw install_gui.py
    
    echo [成功] 安装界面已启动
    echo.
    echo 提示: 
    echo   - 如果界面未显示，请检查任务栏
    echo   - 安装过程请勿关闭此窗口
    echo   - 安装日志位于: %%APPDATA%%\OpenClaw\install.log
    echo.
)

echo.
echo ============================================================
echo 安装程序已启动
echo ============================================================
echo.

:exit_clean
echo.
echo 感谢使用 OpenClaw!
echo.
timeout /t 3 >nul
exit /b

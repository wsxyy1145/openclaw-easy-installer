@echo off
REM ========================================
REM Cloudflare Pages 部署脚本
REM ========================================

echo.
echo ========================================
echo   Cloudflare Pages 部署工具
echo ========================================
echo.

REM 检查 Node.js
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Node.js
    echo.
    echo 请先安装 Node.js: https://nodejs.org/
    echo.
    pause
    exit /b 1
)

echo [成功] Node.js 已安装
echo.

REM 检查 Wrangler
where wrangler >nul 2>nul
if %errorlevel% neq 0 (
    echo [提示] 未检测到 Wrangler CLI
    echo.
    set /p install_wrangler="是否安装 Wrangler? (Y/N): "
    if /i "%install_wrangler%"=="Y" (
        echo.
        echo 正在安装 Wrangler...
        npm install -g wrangler
        if %errorlevel% neq 0 (
            echo.
            echo [错误] Wrangler 安装失败
            pause
            exit /b 1
        )
        echo [成功] Wrangler 安装完成
    ) else (
        echo.
        echo 请手动安装 Wrangler: npm install -g wrangler
        pause
        exit /b 0
    )
) else (
    echo [成功] Wrangler 已安装
)

echo.
echo ========================================
echo   部署准备
echo ========================================
echo.

REM 显示项目信息
echo 项目名称: openclaw-easy-installer
echo 部署目录: public
echo GitHub: https://github.com/wsxyy1145/openclaw-easy-installer
echo.

REM 检查 public 目录
if not exist "public\index.html" (
    echo [错误] 找不到 public/index.html
    echo.
    echo 请确保 public 目录包含所有网站文件
    pause
    exit /b 1
)

echo [成功] 找到 public/index.html
echo.

REM 显示文件列表
echo 将要部署的文件:
dir /b public\*.* 2>nul
echo.

set /p confirm_deploy="确认部署到 Cloudflare Pages? (Y/N): "
if /i not "%confirm_deploy%"=="Y" (
    echo.
    echo 部署已取消
    pause
    exit /b 0
)

echo.
echo ========================================
echo   开始部署
echo ========================================
echo.

REM 检查是否已登录
wrangler whoami >nul 2>nul
if %errorlevel% neq 0 (
    echo [提示] 需要先登录 Cloudflare
    echo.
    echo 即将打开浏览器进行登录...
    wrangler login
    if %errorlevel% neq 0 (
        echo.
        echo [错误] 登录失败
        pause
        exit /b 1
    )
    echo [成功] 登录成功
    echo.
)

REM 执行部署
echo 正在部署到 Cloudflare Pages...
echo.
wrangler pages deploy public --project-name=openclaw-easy-installer

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo   部署成功！
    echo ========================================
    echo.
    echo 访问地址: https://openclaw-easy-installer.pages.dev
    echo.
    echo 下一步:
    echo 1. 在 Cloudflare Dashboard 配置自定义域名
    echo 2. 查看部署详情和日志
    echo 3. 分享您的网站链接
    echo.
) else (
    echo.
    echo ========================================
    echo   部署失败
    echo ========================================
    echo.
    echo 请检查:
    echo 1. Cloudflare 账号是否正确登录
    echo 2. 网络连接是否正常
    echo 3. 查看上面的错误信息
    echo.
)

pause

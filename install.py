#!/usr/bin/env python3
# OpenClaw Windows Installer
# Version: 2.0.0
# Description: Enhanced one-click deployment tool for OpenClaw on Windows systems

import os
import sys
import subprocess
import json
import time
import logging
import platform
import ctypes
import shutil
from datetime import datetime
from pathlib import Path

# Check and install dependencies
def install_dependencies():
    """Install required dependencies with retry mechanism"""
    logger.info("=" * 60)
    logger.info("步骤 1/5: 检查并安装依赖项")
    logger.info("=" * 60)
    
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(1, max_retries + 1):
        try:
            # Try to import required modules
            import requests
            from win32com.client import Dispatch
            logger.info(f"✓ 所有依赖项已就绪 (尝试 {attempt}/{max_retries})")
            return True
        except ImportError as e:
            logger.warning(f"缺少依赖项: {str(e)}")
            if attempt < max_retries:
                logger.info(f"正在安装依赖项... (尝试 {attempt}/{max_retries})")
                try:
                    result = subprocess.run(
                        [sys.executable, "-m", "pip", "install", "requests", "pypiwin32"],
                        check=True,
                        capture_output=True,
                        text=True,
                        timeout=300
                    )
                    if result.returncode == 0:
                        logger.info("✓ 依赖项安装成功")
                        return True
                    else:
                        logger.error(f"依赖项安装失败: {result.stderr}")
                except subprocess.TimeoutExpired:
                    logger.error("依赖项安装超时")
                except Exception as install_error:
                    logger.error(f"依赖项安装出错: {str(install_error)}")
                
                if attempt < max_retries:
                    logger.info(f"等待 {retry_delay} 秒后重试...")
                    time.sleep(retry_delay)
            else:
                logger.error(f"依赖项安装失败，已达到最大重试次数 ({max_retries})")
                return False
    
    return False

# Constants
NODE_VERSION = "22.17.0"
NODE_DOWNLOAD_URL = f"https://nodejs.org/dist/v{NODE_VERSION}/node-v{NODE_VERSION}-x64.msi"
CN_MIRROR_SCRIPT_URL = "https://open-claw.org.cn/install-cn.ps1"
DEFAULT_INSTALL_PATH = os.path.join(os.environ.get('PROGRAMFILES', ''), 'OpenClaw')

# Setup logging
def setup_logging():
    log_dir = os.path.join(os.environ.get('APPDATA', ''), 'OpenClaw')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'install.log')
    
    # Create formatter
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler with colored output support
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    return logging.getLogger(__name__)

logger = setup_logging()

def is_admin():
    """Check if the script is running as administrator"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def check_system_requirements():
    """Comprehensive system requirements check"""
    logger.info("=" * 60)
    logger.info("系统要求检查")
    logger.info("=" * 60)
    
    requirements_met = True
    
    # Check Windows version
    logger.info("\n[1/4] 检查操作系统版本...")
    if not check_windows_version():
        requirements_met = False
    
    # Check available disk space
    logger.info("\n[2/4] 检查磁盘空间...")
    if not check_disk_space():
        requirements_met = False
    
    # Check memory
    logger.info("\n[3/4] 检查系统内存...")
    if not check_memory():
        requirements_met = False
    
    # Check network connectivity
    logger.info("\n[4/4] 检查网络连接...")
    if not check_network():
        logger.warning("⚠ 网络连接可能存在问题，但将继续安装")
    
    if requirements_met:
        logger.info("\n✓ 所有系统要求检查通过")
    else:
        logger.error("\n✗ 部分系统要求未满足")
    
    return requirements_met

def check_windows_version():
    """Check if Windows version is supported"""
    try:
        os_version = platform.version()
        os_name = platform.system()
        
        logger.info(f"  操作系统: {os_name}")
        logger.info(f"  版本号: {os_version}")
        
        # Check if Windows 10 or 11
        version_parts = os_version.split('.')
        if len(version_parts) >= 2:
            major = int(version_parts[0])
            if major >= 10:
                logger.info(f"  ✓ Windows 版本兼容 (Windows {major})")
                return True
            else:
                logger.error(f"  ✗ 不支持的Windows版本 (需要 Windows 10 或更高)")
                return False
        else:
            logger.error("  ✗ 无法确定Windows版本")
            return False
    except Exception as e:
        logger.error(f"  ✗ 检查Windows版本时出错: {str(e)}")
        return False

def check_disk_space(required_mb=2048):
    """Check if there's enough disk space"""
    try:
        drive = os.environ.get('SYSTEMDRIVE', 'C:')
        total, used, free = shutil.disk_usage(drive)
        free_mb = free // (1024 * 1024)
        
        logger.info(f"  可用磁盘空间: {free_mb} MB")
        logger.info(f"  所需空间: {required_mb} MB")
        
        if free_mb >= required_mb:
            logger.info(f"  ✓ 磁盘空间充足")
            return True
        else:
            logger.error(f"  ✗ 磁盘空间不足 (需要至少 {required_mb} MB)")
            return False
    except Exception as e:
        logger.error(f"  ✗ 检查磁盘空间时出错: {str(e)}")
        return False

def check_memory(required_mb=1024):
    """Check if there's enough memory"""
    try:
        import psutil
        available_mb = psutil.virtual_memory().available // (1024 * 1024)
        
        logger.info(f"  可用内存: {available_mb} MB")
        logger.info(f"  所需内存: {required_mb} MB")
        
        if available_mb >= required_mb:
            logger.info(f"  ✓ 内存充足")
            return True
        else:
            logger.warning(f"  ⚠ 内存较少 (建议至少 {required_mb} MB)")
            return True  # Warning but continue
    except ImportError:
        logger.info("  ⚠ 无法检查内存 (未安装psutil)")
        return True
    except Exception as e:
        logger.error(f"  ✗ 检查内存时出错: {str(e)}")
        return False

def check_network():
    """Check network connectivity"""
    try:
        import requests
        response = requests.get('https://www.baidu.com', timeout=5)
        if response.status_code == 200:
            logger.info("  ✓ 网络连接正常")
            return True
        else:
            logger.warning(f"  ⚠ 网络连接异常 (状态码: {response.status_code})")
            return False
    except Exception as e:
        logger.warning(f"  ⚠ 网络连接测试失败: {str(e)}")
        return False

def check_nodejs():
    """Check if Node.js is installed and version is sufficient"""
    logger.info("\n检查Node.js安装状态...")
    
    try:
        result = subprocess.run(['node', '-v'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            node_version = result.stdout.strip()
            logger.info(f"检测到Node.js版本: {node_version}")
            
            # Parse version
            if node_version.startswith('v'):
                version = node_version[1:]
                version_parts = version.split('.')
                if len(version_parts) >= 3:
                    major = int(version_parts[0])
                    
                    if major >= 22:
                        logger.info("✓ Node.js版本检查通过 (>= 22.0.0)")
                        return True
                    else:
                        logger.warning(f"Node.js版本过旧 (当前: {major}.x.x, 需要: 22.x.x)")
                        return False
                else:
                    logger.warning("Node.js版本格式无法识别")
                    return False
            else:
                logger.warning("Node.js版本格式异常")
                return False
        else:
            logger.info("Node.js未安装")
            return False
    except FileNotFoundError:
        logger.info("Node.js未找到")
        return False
    except Exception as e:
        logger.warning(f"检查Node.js时出错: {str(e)}")
        return False

def install_nodejs():
    """Install Node.js LTS with progress tracking"""
    logger.info("\n" + "=" * 60)
    logger.info("安装Node.js LTS")
    logger.info("=" * 60)
    
    try:
        import requests
        
        node_installer_path = os.path.join(os.environ.get('TEMP', ''), f'node-v{NODE_VERSION}-x64.msi')
        
        # Download Node.js with progress
        logger.info(f"\n正在下载 Node.js v{NODE_VERSION}...")
        logger.info(f"下载地址: {NODE_DOWNLOAD_URL}")
        
        response = requests.get(NODE_DOWNLOAD_URL, stream=True, timeout=300)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(node_installer_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    progress = (downloaded / total_size) * 100
                    if int(progress) % 10 == 0:
                        logger.info(f"下载进度: {int(progress)}%")
        
        logger.info("✓ 下载完成")
        
        # Install Node.js
        logger.info("\n正在安装Node.js...")
        install_log = os.path.join(os.environ.get('TEMP', ''), 'node-install.log')
        
        result = subprocess.run(
            ['msiexec.exe', '/i', node_installer_path, '/qn', f'/L*v', install_log],
            capture_output=True,
            text=True,
            timeout=600
        )
        
        if result.returncode == 0:
            logger.info("✓ Node.js安装命令执行成功")
            
            # Update PATH
            node_path = os.path.join(os.environ.get('PROGRAMFILES', ''), 'nodejs')
            os.environ['PATH'] = os.environ.get('PATH', '') + ';' + node_path
            
            # Verify installation
            time.sleep(2)
            if check_nodejs():
                logger.info("✓ Node.js安装并验证成功")
                return True
            else:
                logger.error("Node.js安装后验证失败")
                return False
        else:
            logger.error(f"Node.js安装失败 (返回码: {result.returncode})")
            if result.stderr:
                logger.error(f"错误信息: {result.stderr}")
            return False
            
    except Exception as e:
        logger.error(f"Node.js安装过程中出错: {str(e)}")
        return False
    finally:
        # Clean up installer
        node_installer_path = os.path.join(os.environ.get('TEMP', ''), f'node-v{NODE_VERSION}-x64.msi')
        if os.path.exists(node_installer_path):
            try:
                os.remove(node_installer_path)
                logger.info("已清理临时安装文件")
            except:
                pass

def install_openclaw_npm():
    """Install OpenClaw via npm with retry and verification"""
    logger.info("\n" + "=" * 60)
    logger.info("通过npm安装OpenClaw")
    logger.info("=" * 60)
    
    max_retries = 2
    
    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"\n安装尝试 {attempt}/{max_retries}")
            logger.info("执行: npm install -g openclaw@latest")
            
            result = subprocess.run(
                ['npm', 'install', '-g', 'openclaw@latest'],
                capture_output=True,
                text=True,
                timeout=600
            )
            
            if result.stdout:
                for line in result.stdout.split('\n'):
                    if line.strip():
                        logger.info(f"  {line}")
            
            if result.stderr:
                for line in result.stderr.split('\n'):
                    if line.strip() and 'warn' not in line.lower():
                        logger.error(f"  {line}")
            
            if result.returncode == 0:
                logger.info("✓ OpenClaw安装成功")
                
                # Verify installation
                if verify_openclaw_installation():
                    return True
                else:
                    logger.warning("安装验证失败，将重试")
            else:
                logger.error(f"✗ OpenClaw安装失败 (返回码: {result.returncode})")
                
        except subprocess.TimeoutExpired:
            logger.error("安装超时")
        except Exception as e:
            logger.error(f"安装过程出错: {str(e)}")
        
        if attempt < max_retries:
            logger.info(f"\n等待5秒后重试...")
            time.sleep(5)
    
    logger.error("✗ OpenClaw安装失败，已达到最大重试次数")
    return False

def install_openclaw_cn_mirror():
    """Install OpenClaw via Chinese mirror"""
    logger.info("\n" + "=" * 60)
    logger.info("通过中国镜像安装OpenClaw")
    logger.info("=" * 60)
    
    try:
        import requests
        
        install_script_path = os.path.join(os.environ.get('TEMP', ''), 'install-cn.ps1')
        
        logger.info(f"\n下载安装脚本...")
        logger.info(f"下载地址: {CN_MIRROR_SCRIPT_URL}")
        
        response = requests.get(CN_MIRROR_SCRIPT_URL, timeout=60)
        response.raise_for_status()
        
        with open(install_script_path, 'wb') as f:
            f.write(response.content)
        
        logger.info("✓ 下载完成")
        
        logger.info("\n运行安装脚本...")
        result = subprocess.run(
            ['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', install_script_path],
            capture_output=True,
            text=True,
            timeout=600
        )
        
        if result.stdout:
            for line in result.stdout.split('\n'):
                if line.strip():
                    logger.info(f"  {line}")
        
        if result.stderr:
            for line in result.stderr.split('\n'):
                if line.strip():
                    logger.error(f"  {line}")
        
        if result.returncode == 0:
            logger.info("✓ 通过中国镜像安装成功")
            
            if verify_openclaw_installation():
                return True
            else:
                logger.warning("安装验证失败")
                return False
        else:
            logger.error(f"✗ 安装失败 (返回码: {result.returncode})")
            return False
            
    except Exception as e:
        logger.error(f"安装过程出错: {str(e)}")
        return False
    finally:
        # Clean up
        install_script_path = os.path.join(os.environ.get('TEMP', ''), 'install-cn.ps1')
        if os.path.exists(install_script_path):
            try:
                os.remove(install_script_path)
                logger.info("已清理临时文件")
            except:
                pass

def install_openclaw_offline():
    """Install OpenClaw from offline package"""
    logger.info("\n" + "=" * 60)
    logger.info("通过离线包安装OpenClaw")
    logger.info("=" * 60)
    
    try:
        # Check for offline package
        offline_package = os.path.join(os.getcwd(), 'openclaw-offline.tgz')
        
        if not os.path.exists(offline_package):
            logger.error(f"✗ 离线包不存在: {offline_package}")
            logger.error("请确保 openclaw-offline.tgz 文件位于当前目录中")
            return False
        
        logger.info(f"使用离线包: {offline_package}")
        logger.info(f"文件大小: {os.path.getsize(offline_package) / (1024*1024):.2f} MB")
        
        logger.info("\n执行: npm install -g openclaw-offline.tgz")
        result = subprocess.run(
            ['npm', 'install', '-g', offline_package],
            capture_output=True,
            text=True,
            timeout=600
        )
        
        if result.stdout:
            for line in result.stdout.split('\n'):
                if line.strip():
                    logger.info(f"  {line}")
        
        if result.stderr:
            for line in result.stderr.split('\n'):
                if line.strip():
                    logger.error(f"  {line}")
        
        if result.returncode == 0:
            logger.info("✓ 离线安装成功")
            
            if verify_openclaw_installation():
                return True
            else:
                return False
        else:
            logger.error(f"✗ 离线安装失败 (返回码: {result.returncode})")
            return False
            
    except Exception as e:
        logger.error(f"离线安装过程出错: {str(e)}")
        return False

def install_openclaw_dev():
    """Install OpenClaw development version"""
    logger.info("\n" + "=" * 60)
    logger.info("安装OpenClaw开发版")
    logger.info("=" * 60)
    
    try:
        logger.info("\n执行: npm install -g openclaw@dev")
        result = subprocess.run(
            ['npm', 'install', '-g', 'openclaw@dev'],
            capture_output=True,
            text=True,
            timeout=600
        )
        
        if result.stdout:
            for line in result.stdout.split('\n'):
                if line.strip():
                    logger.info(f"  {line}")
        
        if result.stderr:
            for line in result.stderr.split('\n'):
                if line.strip():
                    logger.error(f"  {line}")
        
        if result.returncode == 0:
            logger.info("✓ 开发版安装成功")
            
            if verify_openclaw_installation():
                return True
            else:
                return False
        else:
            logger.error(f"✗ 开发版安装失败 (返回码: {result.returncode})")
            return False
            
    except Exception as e:
        logger.error(f"开发版安装过程出错: {str(e)}")
        return False

def verify_openclaw_installation():
    """Verify that OpenClaw was installed correctly"""
    logger.info("\n验证OpenClaw安装...")
    
    try:
        # Check if openclaw command exists
        result = subprocess.run(['openclaw', '--version'], capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            version = result.stdout.strip()
            logger.info(f"✓ OpenClaw已安装 (版本: {version})")
            return True
        else:
            logger.warning("✗ openclaw命令不可用")
            return False
            
    except FileNotFoundError:
        logger.error("✗ openclaw命令未找到")
        return False
    except Exception as e:
        logger.error(f"验证安装时出错: {str(e)}")
        return False

def configure_openclaw():
    """Configure OpenClaw with enhanced settings"""
    logger.info("\n" + "=" * 60)
    logger.info("配置OpenClaw")
    logger.info("=" * 60)
    
    try:
        config_dir = os.path.join(os.environ.get('APPDATA', ''), 'OpenClaw')
        os.makedirs(config_dir, exist_ok=True)
        
        config_path = os.path.join(config_dir, 'config.json')
        
        # Check if config already exists
        if os.path.exists(config_path):
            logger.info("检测到现有配置文件，创建备份...")
            backup_path = os.path.join(config_dir, f'config.backup.{int(time.time())}.json')
            shutil.copy2(config_path, backup_path)
            logger.info(f"✓ 备份已保存: {backup_path}")
        
        # Create new configuration
        config = {
            "mode": "local",
            "port": 18789,
            "host": "localhost",
            "gateway": True,
            "autoStart": True,
            "logLevel": "info",
            "dataDir": os.path.join(os.environ.get('APPDATA', ''), 'OpenClaw', 'data'),
            "createdAt": datetime.now().isoformat(),
            "version": "2.0.0"
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        logger.info(f"✓ 配置文件已创建: {config_path}")
        logger.info(f"  端口: {config['port']}")
        logger.info(f"  主机: {config['host']}")
        logger.info(f"  自动启动: {config['autoStart']}")
        
        return True
        
    except Exception as e:
        logger.error(f"配置过程出错: {str(e)}")
        return False

def create_desktop_shortcut():
    """Create desktop shortcut with error handling"""
    logger.info("\n创建桌面快捷方式...")
    
    try:
        from win32com.client import Dispatch
        
        shell = Dispatch('WScript.Shell')
        desktop = shell.SpecialFolders("Desktop")
        shortcut_path = os.path.join(desktop, "OpenClaw.lnk")
        
        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.TargetPath = "http://localhost:18789"
        shortcut.Description = "OpenClaw控制面板 - AI开发工具"
        shortcut.IconLocation = r"%SystemRoot%\System32\url.dll,0"
        shortcut.WorkingDirectory = os.getcwd()
        shortcut.Save()
        
        logger.info(f"✓ 桌面快捷方式已创建: {shortcut_path}")
        return True
        
    except Exception as e:
        logger.error(f"创建桌面快捷方式失败: {str(e)}")
        return False

def create_start_menu_shortcut():
    """Create start menu shortcuts"""
    logger.info("\n创建开始菜单快捷方式...")
    
    try:
        from win32com.client import Dispatch
        
        start_menu_path = os.path.join(
            os.environ.get('APPDATA', ''),
            'Microsoft', 'Windows', 'Start Menu', 'Programs', 'OpenClaw'
        )
        os.makedirs(start_menu_path, exist_ok=True)
        
        shell = Dispatch('WScript.Shell')
        
        # Control panel shortcut
        cp_shortcut = shell.CreateShortcut(os.path.join(start_menu_path, "控制面板.lnk"))
        cp_shortcut.TargetPath = "http://localhost:18789"
        cp_shortcut.Description = "打开OpenClaw控制面板"
        cp_shortcut.IconLocation = r"%SystemRoot%\System32\url.dll,0"
        cp_shortcut.Save()
        
        # Documentation shortcut
        doc_shortcut = shell.CreateShortcut(os.path.join(start_menu_path, "文档和帮助.lnk"))
        doc_shortcut.TargetPath = "https://github.com/wsxyy1145/openclaw"
        doc_shortcut.Description = "查看OpenClaw文档"
        doc_shortcut.IconLocation = r"%SystemRoot%\System32\url.dll,0"
        doc_shortcut.Save()
        
        # Uninstall shortcut
        uninstall_shortcut = shell.CreateShortcut(os.path.join(start_menu_path, "卸载OpenClaw.lnk"))
        uninstall_shortcut.TargetPath = "powershell.exe"
        uninstall_shortcut.Arguments = "-ExecutionPolicy Bypass -Command \"npm uninstall -g openclaw\""
        uninstall_shortcut.Description = "卸载OpenClaw"
        uninstall_shortcut.IconLocation = r"%SystemRoot%\System32\shell32.dll,45"
        uninstall_shortcut.WorkingDirectory = os.getcwd()
        uninstall_shortcut.Save()
        
        logger.info(f"✓ 开始菜单快捷方式已创建: {start_menu_path}")
        return True
        
    except Exception as e:
        logger.error(f"创建开始菜单快捷方式失败: {str(e)}")
        return False

def print_summary(success=True):
    """Print installation summary"""
    logger.info("\n" + "=" * 60)
    if success:
        logger.info("安装完成摘要")
        logger.info("=" * 60)
        logger.info("✓ OpenClaw已成功安装！")
        logger.info(f"\n访问地址: http://localhost:18789")
        logger.info(f"配置文件: {os.path.join(os.environ.get('APPDATA', ''), 'OpenClaw', 'config.json')}")
        logger.info(f"安装日志: {os.path.join(os.environ.get('APPDATA', ''), 'OpenClaw', 'install.log')}")
        logger.info("\n下一步:")
        logger.info("  1. 在浏览器中打开 http://localhost:18789")
        logger.info("  2. 按照提示完成初始配置")
        logger.info("  3. 开始使用OpenClaw")
    else:
        logger.info("安装失败摘要")
        logger.info("=" * 60)
        logger.error("✗ OpenClaw安装未完成")
        logger.info(f"\n请查看安装日志获取详细信息:")
        logger.info(f"{os.path.join(os.environ.get('APPDATA', ''), 'OpenClaw', 'install.log')}")
        logger.info("\n常见问题解决:")
        logger.info("  1. 确保以管理员身份运行")
        logger.info("  2. 检查网络连接")
        logger.info("  3. 关闭杀毒软件后重试")
        logger.info("  4. 查看GitHub Issues寻求帮助")
    logger.info("=" * 60)

def install_openclaw(install_mode="npm", no_shortcuts=False):
    """Main installation function with enhanced flow"""
    start_time = time.time()
    
    logger.info("\n" + "=" * 60)
    logger.info("OpenClaw Windows 安装程序 v2.0.0")
    logger.info("=" * 60)
    logger.info(f"安装模式: {install_mode}")
    logger.info(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 60)
    
    # Step 0: Install dependencies
    if not install_dependencies():
        logger.error("依赖项安装失败，终止安装")
        print_summary(False)
        return False
    
    # Step 1: Check system requirements
    if not check_system_requirements():
        logger.warning("系统要求检查未完全通过，但将继续尝试安装")
    
    # Step 2: Check and install Node.js if needed
    if not check_nodejs():
        logger.info("\n需要安装Node.js")
        if not install_nodejs():
            logger.error("Node.js安装失败，终止安装")
            print_summary(False)
            return False
    else:
        logger.info("✓ Node.js已安装，跳过安装步骤")
    
    # Step 3: Install OpenClaw based on mode
    logger.info("\n" + "=" * 60)
    logger.info("安装OpenClaw")
    logger.info("=" * 60)
    
    if install_mode == "cn-mirror":
        if not install_openclaw_cn_mirror():
            print_summary(False)
            return False
    elif install_mode == "offline":
        if not install_openclaw_offline():
            print_summary(False)
            return False
    elif install_mode == "dev":
        if not install_openclaw_dev():
            print_summary(False)
            return False
    else:
        if not install_openclaw_npm():
            print_summary(False)
            return False
    
    # Step 4: Configure OpenClaw
    if not configure_openclaw():
        logger.error("配置失败，但安装可能已完成")
    
    # Step 5: Create shortcuts
    if not no_shortcuts:
        create_desktop_shortcut()
        create_start_menu_shortcut()
    
    # Calculate installation time
    elapsed_time = time.time() - start_time
    logger.info(f"\n总安装时间: {elapsed_time:.2f} 秒")
    
    logger.info("\n" + "=" * 60)
    logger.info("安装成功完成！")
    logger.info("=" * 60)
    
    print_summary(True)
    return True

if __name__ == "__main__":
    # Check if running as administrator
    if not is_admin():
        logger.error("=" * 60)
        logger.error("错误: 请以管理员身份运行此脚本")
        logger.error("=" * 60)
        messagebox.showerror("权限不足", "请以管理员身份运行此程序。\n右键点击 -> 以管理员身份运行")
        sys.exit(1)
    
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(
        description="OpenClaw Windows Installer v2.0.0",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  python install.py                          # 标准安装
  python install.py --install-mode cn-mirror # 使用中国镜像
  python install.py --install-mode offline   # 离线安装
  python install.py --install-mode dev       # 安装开发版
  python install.py --no-shortcuts           # 不创建快捷方式
        """
    )
    parser.add_argument("--silent", action="store_true", help="静默安装模式")
    parser.add_argument("--install-mode", default="npm", 
                       choices=["npm", "cn-mirror", "offline", "dev"],
                       help="安装模式 (默认: npm)")
    parser.add_argument("--no-shortcuts", action="store_true", help="不创建快捷方式")
    args = parser.parse_args()
    
    # Run installation
    try:
        success = install_openclaw(args.install_mode, args.no_shortcuts)
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        logger.warning("\n\n用户中断安装")
        sys.exit(1)
    except Exception as e:
        logger.error(f"\n\n安装过程中发生未预期的错误: {str(e)}")
        logger.exception("详细错误信息:")
        print_summary(False)
        sys.exit(1)

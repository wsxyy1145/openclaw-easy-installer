#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenClaw 安装程序测试脚本
用于验证安装程序的各项功能
"""

import os
import sys
import subprocess
import platform

def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def print_success(message):
    """Print success message"""
    print(f"✓ {message}")

def print_error(message):
    """Print error message"""
    print(f"✗ {message}")

def print_info(message):
    """Print info message"""
    print(f"ℹ {message}")

def test_python_version():
    """Test Python version"""
    print_header("测试 1: Python 版本检查")
    
    version = sys.version_info
    print_info(f"Python 版本: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 7:
        print_success("Python 版本满足要求 (>= 3.7)")
        return True
    else:
        print_error("Python 版本过低 (需要 >= 3.7)")
        return False

def test_dependencies():
    """Test required dependencies"""
    print_header("测试 2: 依赖项检查")
    
    dependencies = {
        'requests': 'HTTP请求库',
        'win32com.client': 'Windows COM接口'
    }
    
    all_installed = True
    
    for module, description in dependencies.items():
        try:
            __import__(module.replace('.', '_') if '.' in module else module)
            print_success(f"{module} - {description}")
        except ImportError:
            print_error(f"{module} - {description} (未安装)")
            all_installed = False
    
    return all_installed

def test_system_info():
    """Test system information"""
    print_header("测试 3: 系统信息")
    
    print_info(f"操作系统: {platform.system()} {platform.release()}")
    print_info(f"版本: {platform.version()}")
    print_info(f"架构: {platform.architecture()[0]}")
    print_info(f"处理器: {platform.processor()}")
    
    # Check disk space
    try:
        import shutil
        total, used, free = shutil.disk_usage(os.environ.get('SYSTEMDRIVE', 'C:'))
        free_gb = free / (1024**3)
        print_info(f"可用磁盘空间: {free_gb:.2f} GB")
        
        if free_gb >= 2:
            print_success("磁盘空间充足 (>= 2GB)")
        else:
            print_error("磁盘空间不足 (< 2GB)")
    except Exception as e:
        print_error(f"无法检查磁盘空间: {e}")

def test_nodejs():
    """Test Node.js installation"""
    print_header("测试 4: Node.js 检查")
    
    try:
        result = subprocess.run(['node', '-v'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            version = result.stdout.strip()
            print_success(f"Node.js 已安装: {version}")
            
            # Check npm
            result_npm = subprocess.run(['npm', '-v'], capture_output=True, text=True, timeout=5)
            if result_npm.returncode == 0:
                npm_version = result_npm.stdout.strip()
                print_success(f"npm 已安装: {npm_version}")
            else:
                print_error("npm 未找到")
        else:
            print_error("Node.js 未安装或无法访问")
    except FileNotFoundError:
        print_error("Node.js 未找到")
    except Exception as e:
        print_error(f"检查Node.js时出错: {e}")

def test_network():
    """Test network connectivity"""
    print_header("测试 5: 网络连接")
    
    try:
        import requests
        response = requests.get('https://www.baidu.com', timeout=5)
        if response.status_code == 200:
            print_success("网络连接正常")
        else:
            print_error(f"网络连接异常 (状态码: {response.status_code})")
    except Exception as e:
        print_error(f"网络连接测试失败: {e}")

def test_install_scripts():
    """Test installation scripts existence"""
    print_header("测试 6: 安装脚本文件")
    
    scripts = ['install.py', 'install_gui.py']
    all_exist = True
    
    for script in scripts:
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script)
        if os.path.exists(script_path):
            size = os.path.getsize(script_path)
            print_success(f"{script} 存在 ({size} bytes)")
        else:
            print_error(f"{script} 不存在")
            all_exist = False
    
    return all_exist

def test_admin_privileges():
    """Test administrator privileges"""
    print_header("测试 7: 管理员权限")
    
    import ctypes
    if ctypes.windll.shell32.IsUserAnAdmin():
        print_success("当前以管理员身份运行")
        return True
    else:
        print_error("未以管理员身份运行")
        print_info("某些功能可能需要管理员权限")
        return False

def run_all_tests():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("  OpenClaw 安装程序 - 系统测试")
    print("=" * 60)
    print(f"\n测试时间: {platform.platform()}")
    print(f"Python: {sys.version.split()[0]}")
    
    results = []
    
    # Run tests
    results.append(("Python版本", test_python_version()))
    results.append(("依赖项", test_dependencies()))
    test_system_info()
    test_nodejs()
    test_network()
    results.append(("安装脚本", test_install_scripts()))
    results.append(("管理员权限", test_admin_privileges()))
    
    # Summary
    print_header("测试结果汇总")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{test_name}: {status}")
    
    print("\n" + "-" * 60)
    print(f"总计: {passed}/{total} 项测试通过")
    
    if passed == total:
        print("\n✓ 所有测试通过！系统已准备好安装OpenClaw")
        return True
    else:
        print(f"\n⚠ {total - passed} 项测试未通过")
        print("建议修复问题后再进行安装")
        return False

if __name__ == "__main__":
    try:
        success = run_all_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n测试被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

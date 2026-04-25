# OpenClaw Windows 安装程序使用指南

## 📋 目录

- [快速开始](#快速开始)
- [系统要求](#系统要求)
- [安装步骤](#安装步骤)
- [安装模式说明](#安装模式说明)
- [常见问题](#常见问题)
- [故障排除](#故障排除)
- [技术支持](#技术支持)

---

## 🚀 快速开始

### 方法一：图形化界面安装（推荐）

1. **下载并解压**安装程序到任意目录
2. **双击运行** `Install-OpenClaw.bat`
3. **选择安装模式**（推荐使用中国镜像模式）
4. **等待安装完成**
5. **访问控制面板** http://localhost:18789

### 方法二：命令行安装

```bash
# 标准安装
python install.py

# 使用中国镜像（推荐国内用户）
python install.py --install-mode cn-mirror

# 离线安装
python install.py --install-mode offline

# 开发版安装
python install.py --install-mode dev
```

---

## 💻 系统要求

### 最低配置

- **操作系统**: Windows 10/11 (64位)
- **Python**: 3.7 或更高版本
- **磁盘空间**: 至少 2 GB 可用空间
- **内存**: 至少 1 GB RAM
- **网络**: 稳定的互联网连接（离线模式除外）
- **权限**: 管理员权限

### 推荐配置

- **操作系统**: Windows 11 最新版
- **Python**: 3.10 或更高版本
- **磁盘空间**: 至少 5 GB 可用空间
- **内存**: 4 GB RAM 或更多
- **网络**: 高速宽带连接

---

## 📦 安装步骤

### 步骤 1: 准备工作

#### 1.1 安装 Python

如果尚未安装 Python，请访问 [Python 官网](https://www.python.org/downloads/) 下载并安装。

**重要提示**: 安装时务必勾选 **"Add Python to PATH"** 选项！

#### 1.2 验证 Python 安装

打开命令提示符（CMD），输入：

```bash
python --version
```

应该显示类似：`Python 3.13.12`

#### 1.3 安装依赖项

运行依赖项安装脚本：

```bash
install_dependencies.bat
```

或者手动安装：

```bash
pip install requests pypiwin32 psutil
```

### 步骤 2: 运行安装程序

#### 方式 A: 使用批处理文件（最简单）

1. 右键点击 `Install-OpenClaw.bat`
2. 选择 **"以管理员身份运行"**
3. 按照屏幕提示操作

#### 方式 B: 使用图形界面

```bash
python install_gui.py
```

#### 方式 C: 使用命令行

```bash
python install.py --install-mode cn-mirror
```

### 步骤 3: 选择安装模式

安装程序提供四种安装模式：

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| **标准模式 (npm)** | 从官方npm仓库安装 | 国际用户，网络良好 |
| **中国镜像模式** ⭐ | 使用国内镜像加速 | 中国大陆用户（推荐） |
| **离线安装模式** | 使用本地离线包 | 无网络环境 |
| **开发版模式** | 安装最新开发版本 | 开发者测试 |

### 步骤 4: 等待安装完成

安装过程包括：

1. ✓ 检查系统环境
2. ✓ 安装或验证 Node.js
3. ✓ 部署 OpenClaw
4. ✓ 配置程序与快捷方式

**预计时间**: 3-10 分钟（取决于网络和电脑性能）

### 步骤 5: 验证安装

安装完成后：

1. 桌面会创建 **OpenClaw** 快捷方式
2. 开始菜单会有 **OpenClaw** 文件夹
3. 浏览器访问: http://localhost:18789

---

## 🔧 安装模式详细说明

### 1. 标准模式 (npm)

**特点**:
- 从 npm 官方仓库下载
- 获取最新稳定版本
- 自动更新支持

**适用**:
- 国际用户
- 网络连接良好的用户
- 需要最新稳定版的用户

**命令**:
```bash
python install.py --install-mode npm
```

### 2. 中国镜像模式 ⭐ 推荐

**特点**:
- 使用国内 CDN 加速
- 下载速度更快
- 适合中国大陆网络环境

**适用**:
- 中国大陆用户
- 网络连接较慢的用户
- 希望快速安装的用户

**命令**:
```bash
python install.py --install-mode cn-mirror
```

### 3. 离线安装模式

**特点**:
- 无需网络连接
- 使用本地安装包
- 适合内网环境

**前提条件**:
- 需要准备 `openclaw-offline.tgz` 文件
- 将该文件放在安装程序同一目录

**适用**:
- 无网络环境
- 企业内网
- 批量部署

**命令**:
```bash
python install.py --install-mode offline
```

### 4. 开发版模式

**特点**:
- 安装最新的开发版本
- 包含最新功能和修复
- 可能不够稳定

**适用**:
- 开发者
- 测试人员
- 想体验新功能的用户

**注意**: 开发版可能存在 bug，不建议生产环境使用

**命令**:
```bash
python install.py --install-mode dev
```

---

## ❓ 常见问题

### Q1: 提示"权限不足"怎么办？

**A**: 必须以管理员身份运行安装程序。

**解决方法**:
1. 右键点击 `Install-OpenClaw.bat`
2. 选择 **"以管理员身份运行"**
3. 在弹出的 UAC 对话框中点击 **"是"**

### Q2: Python 未找到怎么办？

**A**: 需要先安装 Python。

**解决方法**:
1. 访问 https://www.python.org/downloads/
2. 下载最新版本的 Python
3. 安装时**务必勾选** "Add Python to PATH"
4. 重新运行安装程序

### Q3: 依赖项安装失败怎么办？

**A**: 可以手动安装依赖。

**解决方法**:
```bash
pip install requests pypiwin32 psutil
```

如果仍然失败，尝试：
```bash
python -m pip install --upgrade pip
pip install requests pypiwin32 psutil
```

### Q4: Node.js 安装失败怎么办？

**A**: 可以手动安装 Node.js。

**解决方法**:
1. 访问 https://nodejs.org/
2. 下载 LTS 版本（推荐 v22.x）
3. 安装后重启命令提示符
4. 重新运行 OpenClaw 安装程序

验证安装：
```bash
node -v
npm -v
```

### Q5: 安装过程中卡住不动怎么办？

**A**: 可能是网络问题或防火墙阻止。

**解决方法**:
1. 检查网络连接
2. 暂时关闭杀毒软件
3. 允许 Python 和 npm 通过防火墙
4. 尝试使用中国镜像模式
5. 查看日志文件: `%APPDATA%\OpenClaw\install.log`

### Q6: 如何卸载 OpenClaw？

**A**: 有多种卸载方式。

**方法一**: 使用开始菜单
- 开始 → OpenClaw → 卸载OpenClaw

**方法二**: 命令行卸载
```bash
npm uninstall -g openclaw
```

**方法三**: 手动清理
```bash
# 删除全局安装包
npm uninstall -g openclaw

# 删除配置文件夹
rmdir /s /q %APPDATA%\OpenClaw

# 删除快捷方式
del "%USERPROFILE%\Desktop\OpenClaw.lnk"
rmdir /s /q "%APPDATA%\Microsoft\Windows\Start Menu\Programs\OpenClaw"
```

### Q7: 安装后无法访问控制面板？

**A**: 检查服务是否启动。

**解决方法**:
1. 确认 OpenClaw 服务已启动
2. 检查端口 18789 是否被占用
3. 尝试重启计算机
4. 查看日志: `%APPDATA%\OpenClaw\install.log`

### Q8: 如何更改安装路径？

**A**: 当前版本不支持自定义路径，但可以手动移动。

**临时方案**:
1. 完成标准安装
2. 移动配置文件到目标位置
3. 修改配置中的路径设置

---

## 🔍 故障排除

### 问题 1: 安装程序闪退

**症状**: 双击后窗口立即关闭

**原因**: 
- 缺少管理员权限
- Python 环境问题
- 依赖项缺失

**解决**:
```bash
# 1. 以管理员身份运行
# 2. 检查Python
python --version

# 3. 安装依赖
install_dependencies.bat

# 4. 查看详细错误
python install_gui.py
```

### 问题 2: npm 安装超时

**症状**: 长时间停留在 "安装OpenClaw..." 步骤

**原因**: 
- 网络速度慢
- npm 服务器响应慢
- 防火墙阻止

**解决**:
```bash
# 使用中国镜像
python install.py --install-mode cn-mirror

# 或设置npm代理
npm config set registry https://registry.npmmirror.com
```

### 问题 3: 快捷方式未创建

**症状**: 安装成功但找不到快捷方式

**原因**: 
- 权限问题
- 防病毒软件阻止

**解决**:
```bash
# 手动创建快捷方式
# 或使用命令行模式
python install.py --no-shortcuts

# 然后手动访问 http://localhost:18789
```

### 问题 4: 端口冲突

**症状**: 无法访问 http://localhost:18789

**原因**: 
- 端口 18789 已被其他程序占用

**解决**:
```bash
# 查找占用端口的程序
netstat -ano | findstr :18789

# 结束进程或更改配置端口
# 编辑: %APPDATA%\OpenClaw\config.json
# 修改 "port": 18789 为其他端口
```

### 问题 5: 日志文件位置

**所有安装日志位于**:
```
%APPDATA%\OpenClaw\install.log
```

**快速访问**:
1. 按 `Win + R`
2. 输入: `%APPDATA%\OpenClaw`
3. 打开 `install.log`

---

## 🛠️ 高级用法

### 静默安装

适用于自动化部署：

```bash
python install.py --silent --install-mode cn-mirror
```

### 不创建快捷方式

```bash
python install.py --no-shortcuts
```

### 查看帮助

```bash
python install.py --help
```

### 离线包准备

```bash
# 在有网络的机器上打包
npm pack openclaw@latest
ren openclaw-*.tgz openclaw-offline.tgz

# 将 openclaw-offline.tgz 复制到目标机器
# 运行离线安装
python install.py --install-mode offline
```

---

## 📞 技术支持

### 获取帮助

1. **查看日志文件**
   - 位置: `%APPDATA%\OpenClaw\install.log`
   - 包含详细的安装过程和错误信息

2. **运行系统测试**
   ```bash
   python test_system.py
   ```

3. **查阅文档**
   - 官方文档: https://github.com/wsxyy1145/openclaw
   - 安装说明: INSTALLATION_IMPROVEMENTS.md

4. **提交问题**
   - GitHub Issues: https://github.com/wsxyy1145/openclaw/issues
   - 附上日志文件和系统信息

### 社区支持

- **GitHub**: https://github.com/wsxyy1145/openclaw
- **文档**: https://openclaw.dev
- **讨论区**: https://github.com/wsxyy1145/openclaw/discussions

---

## 📝 更新日志

### v2.0.0 (2026-04-25)

**新增功能**:
- ✨ 现代化UI界面设计
- ✨ 增强的系统检查（磁盘、内存、网络）
- ✨ 安装重试机制
- ✨ 安装后自动验证
- ✨ 配置备份功能
- ✨ 详细的进度显示
- ✨ 改进的错误处理

**改进**:
- 🚀 更快的安装速度
- 🎨 更美观的界面
- 📊 更详细的日志
- 🔒 更好的安全性
- ⚡ 更稳定的性能

**修复**:
- 🐛 修复Node.js检测问题
- 🐛 修复权限检查问题
- 🐛 修复依赖安装问题

---

## 📄 许可证

OpenClaw 安装程序遵循开源许可证。详情请参阅项目根目录的 LICENSE 文件。

---

**最后更新**: 2026-04-25  
**版本**: 2.0.0  
**维护者**: OpenClaw Team

---

*祝您使用愉快！* 🎉

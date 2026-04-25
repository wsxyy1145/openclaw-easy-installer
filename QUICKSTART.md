# OpenClaw 快速开始指南

> ⏱️ **5分钟快速安装 OpenClaw**

---

## 🎯 前置准备（1分钟）

### 1. 检查 Python

打开命令提示符（Win + R，输入 `cmd`），运行：

```bash
python --version
```

✅ **如果显示版本号**（如 Python 3.13.12），继续下一步  
❌ **如果提示错误**，前往 [python.org](https://www.python.org/downloads/) 下载安装

**重要**：安装时务必勾选 **"Add Python to PATH"**

### 2. 以管理员身份运行

找到 `Install-OpenClaw.bat` 文件：
- **右键点击** → 选择 **"以管理员身份运行"**
- 在弹出的对话框中点击 **"是"**

---

## 🚀 开始安装（3分钟）

### 步骤 1: 选择安装模式

程序启动后，会显示以下选项：

```
请选择安装模式:
  1. 标准模式 (npm)              - 使用官方npm仓库
  2. 中国镜像模式                - 使用国内镜像加速下载 [推荐]
  3. 离线安装模式                - 使用本地离线包
  4. 开发版安装                  - 安装最新开发版本
  5. 仅命令行安装                - 不使用GUI界面
  0. 退出
```

**推荐选择**：直接按 **Enter** 键（默认选择 2 - 中国镜像模式）

### 步骤 2: 等待自动安装

安装过程全自动进行，包括：

```
✓ 检查系统环境
✓ 安装或验证 Node.js
✓ 部署 OpenClaw
✓ 配置程序与快捷方式
```

**预计时间**：3-10 分钟（取决于网络速度）

### 步骤 3: 安装完成

看到以下提示表示安装成功：

```
✓ 安装成功

访问地址: http://localhost:18789
```

---

## 🎉 开始使用（1分钟）

### 方法一：桌面快捷方式

双击桌面上的 **OpenClaw** 图标

### 方法二：浏览器访问

打开浏览器，访问：**http://localhost:18789**

### 方法三：开始菜单

开始 → OpenClaw → 控制面板

---

## ✅ 验证安装

安装完成后，可以运行测试脚本验证：

```bash
python test_system.py
```

所有测试通过即表示安装成功！

---

## 🆘 遇到问题？

### 问题 1: 提示"权限不足"

**解决**：确保右键选择"以管理员身份运行"

### 问题 2: Python 未找到

**解决**：
1. 重新安装 Python
2. 安装时勾选 "Add Python to PATH"
3. 重启电脑后重试

### 问题 3: 依赖项安装失败

**解决**：先运行依赖安装脚本

```bash
install_dependencies.bat
```

### 问题 4: 安装速度慢

**解决**：使用中国镜像模式（选项 2）

### 问题 5: 查看详细日志

日志位置：`%APPDATA%\OpenClaw\install.log`

快速访问：
1. Win + R
2. 输入：`%APPDATA%\OpenClaw`
3. 打开 `install.log`

---

## 📚 更多帮助

- 📖 **完整文档**：[README_使用指南.md](README_使用指南.md)
- 🔧 **改进说明**：[INSTALLATION_IMPROVEMENTS.md](INSTALLATION_IMPROVEMENTS.md)
- 💬 **社区支持**：[GitHub Discussions](https://github.com/wsxyy1145/openclaw/discussions)
- 🐛 **问题反馈**：[GitHub Issues](https://github.com/wsxyy1145/openclaw/issues)

---

## 🎓 下一步

安装成功后，你可以：

1. ✨ 浏览控制面板，了解功能
2. 📖 阅读官方文档学习使用方法
3. 🔧 根据个人需求进行配置
4. 🚀 开始你的第一个项目

---

<div align="center">

**祝你使用愉快！** 🎉

有任何问题欢迎随时反馈

</div>

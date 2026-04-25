# 🚀 Cloudflare Pages 快速部署指南

## ⏱️ 5分钟快速部署

### 步骤 1：准备环境（1分钟）

```bash
# 安装 Node.js（如果还没有）
# 下载: https://nodejs.org/

# 安装 Wrangler CLI
npm install -g wrangler
```

### 步骤 2：登录 Cloudflare（1分钟）

```bash
wrangler login
```

这会打开浏览器，授权访问您的 Cloudflare 账号。

### 步骤 3：部署网站（2分钟）

#### 选项 A：使用一键脚本（推荐）

```bash
cd e:\openclaw_install_tool
deploy_cloudflare.bat
```

按照提示操作即可！

#### 选项 B：手动命令

```bash
cd e:\openclaw_install_tool
wrangler pages deploy public --project-name=openclaw-easy-installer
```

### 步骤 4：访问网站（1分钟）

部署完成后，访问：
```
https://openclaw-easy-installer.pages.dev
```

---

## ✅ 验证清单

部署后检查：

- [ ] 网站可以正常访问
- [ ] 页面加载速度快
- [ ] 所有链接有效
- [ ] 移动端显示正常
- [ ] PWA 功能正常（可安装）

---

## 🔧 常用命令

```bash
# 查看部署列表
wrangler pages deployment list --project-name=openclaw-easy-installer

# 查看项目信息
wrangler pages project view openclaw-easy-installer

# 重新部署
wrangler pages deploy public --project-name=openclaw-easy-installer

# 回滚到上一个版本
wrangler pages deployment rollback --project-name=openclaw-easy-installer
```

---

## 🌐 自定义域名（可选）

1. 在 Cloudflare Dashboard 进入项目设置
2. 点击 **Custom domains**
3. 添加您的域名
4. Cloudflare 自动配置 DNS

示例：
```
installer.yourdomain.com → openclaw-easy-installer.pages.dev
```

---

## 📊 性能优势

Cloudflare Pages 提供：

- ⚡ **全球 CDN**：275+ 数据中心
- 🔒 **自动 HTTPS**：免费 SSL 证书
- 🚀 **HTTP/3**：更快的传输
- 💾 **智能缓存**：自动优化
- 📈 **详细分析**：流量统计

---

## ❓ 常见问题

### Q: 部署失败怎么办？

A: 检查以下几点：
1. 是否已登录：`wrangler whoami`
2. public 目录是否存在
3. 网络连接是否正常

### Q: 如何更新网站？

A: 只需重新运行部署命令：
```bash
wrangler pages deploy public --project-name=openclaw-easy-installer
```

### Q: 可以回滚吗？

A: 可以！Cloudflare 保留所有历史版本：
```bash
wrangler pages deployment rollback --project-name=openclaw-easy-installer
```

---

## 📚 更多资源

- **完整文档**: [CLOUDFLARE_DEPLOYMENT.md](CLOUDFLARE_DEPLOYMENT.md)
- **Cloudflare 文档**: https://developers.cloudflare.com/pages/
- **项目仓库**: https://github.com/wsxyy1145/openclaw-easy-installer

---

**开始部署吧！** 🎉

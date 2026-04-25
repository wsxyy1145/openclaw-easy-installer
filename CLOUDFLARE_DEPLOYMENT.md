# Cloudflare Pages 部署指南

## 📋 目录

- [快速开始](#快速开始)
- [部署方法](#部署方法)
- [配置说明](#配置说明)
- [自定义域名](#自定义域名)
- [环境变量](#环境变量)
- [故障排除](#故障排除)

---

## 🚀 快速开始

### 前提条件

1. **Cloudflare 账号**：注册并登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. **GitHub 仓库**：代码已推送到 `https://github.com/wsxyy1145/openclaw-easy-installer`

---

## 📦 部署方法

### 方法一：通过 Cloudflare Dashboard（推荐）

#### 步骤 1：连接到 Git

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. 进入 **Workers & Pages** > **Pages**
3. 点击 **Create a project** > **Connect to Git**
4. 选择 GitHub 并授权访问
5. 选择仓库：`wsxyy1145/openclaw-easy-installer`

#### 步骤 2：配置构建设置

```
Project name: openclaw-easy-installer
Production branch: main
Build command: (留空，静态网站不需要构建)
Build output directory: public
Root directory: / (根目录)
```

#### 步骤 3：部署

1. 点击 **Save and Deploy**
2. 等待部署完成（通常 30-60 秒）
3. 访问生成的域名：`https://openclaw-easy-installer.pages.dev`

---

### 方法二：使用 Wrangler CLI

#### 安装 Wrangler

```bash
npm install -g wrangler
```

#### 登录 Cloudflare

```bash
wrangler login
```

#### 部署项目

```bash
cd e:\openclaw_install_tool
wrangler pages deploy public --project-name=openclaw-easy-installer
```

#### 查看部署状态

```bash
wrangler pages deployment list --project-name=openclaw-easy-installer
```

---

## ⚙️ 配置说明

### 项目结构

```
openclaw-easy-installer/
├── public/              # Cloudflare Pages 部署目录
│   ├── index.html      # 主页面
│   ├── manifest.json   # PWA 配置
│   ├── robots.txt      # SEO 规则
│   └── sitemap.xml     # 网站地图
├── _routes.json        # Cloudflare 路由配置
└── ...
```

### 关键文件

| 文件 | 用途 |
|------|------|
| `public/index.html` | 主网站页面 |
| `_routes.json` | Cloudflare 路由规则 |
| `public/manifest.json` | PWA 应用配置 |
| `public/robots.txt` | 搜索引擎爬虫规则 |
| `public/sitemap.xml` | 网站地图 |

---

## 🌐 自定义域名

### 添加自定义域名

1. 在 Cloudflare Pages 项目中，进入 **Settings** > **Custom domains**
2. 点击 **Set up a custom domain**
3. 输入您的域名（如 `installer.yourdomain.com`）
4. Cloudflare 会自动配置 DNS 记录
5. 等待 DNS 传播（通常几分钟到几小时）

### DNS 配置（如果需要手动配置）

```
类型: CNAME
名称: installer (或 @)
内容: openclaw-easy-installer.pages.dev
TTL: Auto
```

---

## 🔧 环境变量

在 Cloudflare Pages 中可以设置环境变量：

1. 进入项目 **Settings** > **Environment variables**
2. 添加变量（示例）：

```
NODE_VERSION = 18
CACHE_BUSTER = v1.0.0
```

3. 重新部署以应用更改

---

## 📊 性能优化

### 自动优化

Cloudflare Pages 自动提供：

- ✅ **全球 CDN**：275+ 数据中心
- ✅ **HTTP/3**：更快的传输协议
- ✅ **自动 HTTPS**：SSL/TLS 证书
- ✅ **智能缓存**：自动缓存静态资源
- ✅ **压缩**：Gzip 和 Brotli 压缩

### 手动优化建议

1. **图片优化**：使用 WebP 格式
2. **代码分割**：减少初始加载大小
3. **懒加载**：延迟加载非关键资源
4. **预加载**：使用 `<link rel="preload">`

---

## 🔍 监控和分析

### 内置分析

Cloudflare Pages 提供：

- 📈 **访问量统计**
- 🌍 **地理位置分布**
- 📱 **设备类型分析**
- ⚡ **性能指标**

### 集成第三方分析

在 `public/index.html` 中添加：

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

## 🛠️ 故障排除

### 常见问题

#### 1. 部署失败

**症状**：构建错误或部署超时

**解决方案**：
```bash
# 检查本地文件
ls -la public/

# 验证 HTML 语法
npx html-validator public/index.html

# 重新部署
wrangler pages deploy public --project-name=openclaw-easy-installer
```

#### 2. 404 错误

**症状**：访问页面显示 404

**解决方案**：
- 确认 `public/index.html` 存在
- 检查 `_routes.json` 配置
- 清除浏览器缓存

#### 3. 缓存问题

**症状**：更新后看不到更改

**解决方案**：
```bash
# 强制清除缓存
wrangler pages deployment create --project-name=openclaw-easy-installer

# 或在 Dashboard 中手动触发重新部署
```

#### 4. 自定义域名不工作

**症状**：DNS 解析失败

**解决方案**：
- 检查 DNS 记录是否正确
- 等待 DNS 传播（最多 24 小时）
- 使用 `dig` 或 `nslookup` 验证：
  ```bash
  nslookup installer.yourdomain.com
  ```

---

## 📝 部署检查清单

部署前确认：

- [ ] 代码已推送到 GitHub
- [ ] `public/` 目录包含所有必要文件
- [ ] `index.html` 语法正确
- [ ] 所有链接有效
- [ ] 图片路径正确
- [ ] PWA manifest 配置完整
- [ ] SEO 标签完整
- [ ] 测试过本地预览

部署后验证：

- [ ] 网站可以正常访问
- [ ] 所有页面加载正常
- [ ] 响应式设计在移动端正常
- [ ] 控制台无错误
- [ ] Lighthouse 评分 > 90
- [ ] 自定义域名（如有）正常工作

---

## 🔗 相关资源

- **Cloudflare Pages 文档**: https://developers.cloudflare.com/pages/
- **Wrangler CLI 文档**: https://developers.cloudflare.com/workers/wrangler/
- **项目仓库**: https://github.com/wsxyy1145/openclaw-easy-installer
- **在线网站**: https://openclaw-easy-installer.pages.dev

---

## 💡 提示

### 最佳实践

1. **持续集成**：每次推送到 main 分支自动部署
2. **预览部署**：Pull Request 自动生成预览链接
3. **回滚策略**：保留历史部署版本，可随时回滚
4. **性能监控**：定期检查 Core Web Vitals
5. **安全头**：使用 `_headers` 文件配置安全策略

### 高级功能

- **函数支持**：可以添加 Cloudflare Workers 函数
- **KV 存储**：使用 Cloudflare KV 存储动态数据
- **D1 数据库**：集成 SQLite 数据库
- **R2 存储**：对象存储服务

---

## 🎉 总结

Cloudflare Pages 提供了：

- ⚡ **极速部署**：Git 推送即部署
- 🌍 **全球加速**：275+ CDN 节点
- 🔒 **安全可靠**：自动 HTTPS 和 DDoS 防护
- 💰 **免费额度**：充足的免费套餐
- 📊 **详细分析**：内置流量和性能分析

**现在就开始部署吧！** 🚀

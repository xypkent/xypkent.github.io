# 配置指南 / Setup Guide

## 📋 完成的配置

✅ 已为您配置好以下内容：

1. **Jekyll 网站结构** - 完整的学术主页框架
2. **个人信息** - 基于您提供的信息配置
3. **Google Scholar 集成** - 自动引用抓取系统
4. **响应式设计** - 支持桌面和移动设备
5. **美观的样式** - 现代化学术风格

## 🎨 下一步：添加您的照片

### 1. 替换个人照片

将您的个人照片替换到以下位置：
```
images/profile.png
```

**推荐尺寸**：400x400 像素，正方形，JPG 或 PNG 格式

### 2. 添加论文预览图

如果您有论文的预览图或截图，可以添加到：
```
images/haichart.png
images/paper2.png
...
```

然后在 `_pages/about.md` 中更新图片路径。

## 🔧 本地测试

### 安装依赖（首次使用）

```bash
# 确保已安装 Ruby (macOS 自带)
ruby -v

# 安装 Bundler
gem install bundler

# 安装项目依赖
cd /Users/xyp/xypkent.github.io
bundle install
```

### 启动本地服务器

```bash
./run_server.sh
```

或者：

```bash
bundle exec jekyll serve --livereload
```

然后访问：http://127.0.0.1:4000

## 🚀 部署到 GitHub Pages

### 1. 设置 GitHub Pages

1. 进入您的仓库：https://github.com/xypkent/xypkent.github.io
2. 点击 **Settings**
3. 左侧菜单选择 **Pages**
4. 在 **Source** 下选择：
   - Branch: `main`
   - Folder: `/ (root)`
5. 点击 **Save**

### 2. 配置 Google Scholar 自动更新

1. 进入仓库 **Settings** → **Secrets and variables** → **Actions**
2. 点击 **New repository secret**
3. 添加：
   - Name: `GOOGLE_SCHOLAR_ID`
   - Value: `Xt8HBrIAAAAJ`
4. 点击 **Add secret**

### 3. 启用 GitHub Actions

1. 进入仓库的 **Actions** 标签
2. 如果看到提示，点击 **I understand my workflows, go ahead and enable them**
3. GitHub Actions 将每天自动更新您的引用数据

### 4. 推送到 GitHub

```bash
cd /Users/xyp/xypkent.github.io
git add .
git commit -m "Setup academic homepage with AcadHomepage template"
git push origin main
```

## ✏️ 自定义内容

### 修改个人简介

编辑 `_pages/about.md`：

```markdown
I am a PhD student at...
```

### 添加新闻

在 `_pages/about.md` 的 `# 🔥 News` 部分添加：

```markdown
- *2024.10*: &nbsp;🎉🎉 新的消息内容
```

### 添加论文

在 `_pages/about.md` 的 `# 📝 Publications` 部分添加：

```markdown
- [论文标题](链接), 作者列表. **会议/期刊**, 年份.
```

### 添加奖项

在 `_pages/about.md` 的 `# 🎖 Honors and Awards` 部分添加：

```markdown
- *2024* 奖项名称
```

## 🎯 显示论文引用数

要显示特定论文的引用数，在论文描述中添加：

```html
<span class='show_paper_citations' data='PAPER_ID'></span>
```

**如何获取 PAPER_ID：**

1. 访问您的 Google Scholar 主页
2. 点击具体论文
3. URL 中 `citation_for_view=XXX:PAPER_ID`，其中 `PAPER_ID` 就是您需要的

## 📱 社交媒体链接

在 `_config.yml` 中更新：

```yaml
author:
  linkedin         : "your-linkedin-username"
  twitter          : "your-twitter-handle"
  orcid            : "0000-0000-0000-0000"
  researchgate     : "your-profile"
```

## 🎨 自定义样式

修改 `assets/css/main.css` 来自定义：

- 颜色主题
- 字体
- 布局
- 等等

## ❓ 常见问题

### Q: 网站显示空白？
A: 检查 Jekyll 是否正常编译，查看终端错误信息

### Q: 图片不显示？
A: 确保图片路径正确，使用相对路径如 `images/profile.png`

### Q: GitHub Pages 没有更新？
A: 可能需要等待几分钟，检查 Actions 标签查看构建状态

### Q: 引用数没有显示？
A: 确保已设置 GOOGLE_SCHOLAR_ID secret，等待 Actions 运行

## 📞 获取帮助

如果遇到问题：

1. 查看 [Jekyll 文档](https://jekyllrb.com/docs/)
2. 查看 [AcadHomepage 原始仓库](https://github.com/RayeRen/acad-homepage.github.io)
3. 检查 GitHub Actions 日志

## 🎉 完成！

您的学术主页已经配置完成！现在您可以：

1. ✅ 添加您的照片
2. ✅ 本地测试网站
3. ✅ 推送到 GitHub
4. ✅ 享受您的新主页！

祝您使用愉快！🚀


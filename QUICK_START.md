# 🚀 快速开始指南

您的学术主页已经配置完成！以下是已更新的内容和下一步操作。

## ✅ 已完成的配置

### 📝 论文列表（已根据您的 Google Scholar 更新）
1. **HAIChart** - VLDB 2024（34 引用）
2. **ChartMark** - IEEE VIS 2025（新论文！）
3. **智能数据可视化综述** - 软件学报 2023（8 引用）

✓ Navi 论文已移除（根据您的要求）

### 📊 统计信息
- 总引用数：42
- h-index: 2
- i10-index: 1

### 👤 个人信息
- 姓名：Yupeng Xie（谢宇鹏）
- 职位：PhD Student
- 学校：HKUST(GZ)
- 导师：Professor Yuyu Luo
- 研究方向：智能数据可视化
- 邮箱：yxie740@connect.hkust-gz.edu.cn
- Google Scholar：https://scholar.google.com/citations?user=Xt8HBrIAAAAJ

## 📋 接下来的步骤

### 1️⃣ 添加您的照片（重要！）

将您的个人照片复制到：
```bash
images/profile.png
```

**建议**：
- 尺寸：400x400 像素（正方形）
- 格式：PNG 或 JPG
- 背景：纯色或虚化

### 2️⃣ 本地预览（推荐）

```bash
# 安装依赖（首次使用）
gem install bundler
bundle install

# 启动服务器
./run_server.sh
```

访问：http://127.0.0.1:4000

### 3️⃣ 推送到 GitHub

```bash
git add .
git commit -m "Setup academic homepage"
git push origin main
```

### 4️⃣ 启用 GitHub Pages

访问：https://github.com/xypkent/xypkent.github.io/settings/pages

设置：
- **Source**: Branch `main`, folder `/ (root)`
- 点击 **Save**

### 5️⃣ 配置 Google Scholar 自动更新

访问：https://github.com/xypkent/xypkent.github.io/settings/secrets/actions

添加 Secret：
- **Name**: `GOOGLE_SCHOLAR_ID`
- **Value**: `Xt8HBrIAAAAJ`

## 🎨 可选的自定义

### 添加论文链接

如果您有 HAIChart 或 ChartMark 的项目页面、PDF 或代码，可以在 `_pages/about.md` 中添加：

```markdown
[**Project**](https://项目链接) | [**PDF**](https://论文链接) | [**Code**](https://github.com/...)
```

### 添加论文预览图

将论文的截图或预览图保存为：
- `images/haichart.png`（已有占位图）
- `images/chartmark.png`（已有占位图）

### 更新 News 部分

编辑 `_pages/about.md` 第 27-29 行，添加更多新闻。

### 更新奖项

编辑 `_pages/about.md` 第 52-54 行，添加真实的奖项信息。

## 📁 重要文件位置

| 文件 | 用途 |
|------|------|
| `_pages/about.md` | 主页内容 |
| `_config.yml` | 网站配置 |
| `images/profile.png` | 个人照片 |
| `images/haichart.png` | HAIChart 预览图 |
| `images/chartmark.png` | ChartMark 预览图 |

## 🎯 预期效果

您的主页将展示：
- ✨ 现代化响应式设计
- 📊 Google Scholar 引用徽章
- 📝 三篇论文（含引用数）
- 🔥 最新新闻动态
- 🎓 完整的学术信息
- 📱 移动端友好

## ❓ 常见问题

**Q: 网站多久更新？**  
A: 推送到 GitHub 后，通常 1-5 分钟内更新。

**Q: 引用数如何自动更新？**  
A: 配置 GOOGLE_SCHOLAR_ID secret 后，GitHub Actions 每天自动抓取。

**Q: 如何修改样式？**  
A: 编辑 `assets/css/main.css` 文件。

## 📞 需要帮助？

详细指南：`docs/SETUP_GUIDE.md`

---

**现在就开始吧！** 🎉

1. 添加您的照片
2. 运行 `./run_server.sh` 本地预览
3. 推送到 GitHub
4. 享受您的新主页！


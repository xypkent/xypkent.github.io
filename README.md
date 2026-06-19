# xypkent.github.io

Yupeng Xie 的个人学术主页，基于 [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) 模板构建。

线上地址：https://xypkent.github.io

---

## 本地预览

环境已就绪（Ruby + Jekyll + Bundler 均已安装），直接运行：

```bash
bash run_server.sh
```

然后在浏览器打开 http://127.0.0.1:4000 即可预览。

修改文件后页面会自动刷新，无需重启。

---

## 主要文件

| 文件/目录 | 说明 |
|---|---|
| `_pages/about.md` | 主页内容（个人简介、论文、新闻等） |
| `_config.yml` | 站点配置（姓名、邮箱、社交链接等） |
| `images/` | 论文配图、头像等图片资源 |

---

## 更新主页内容

1. 编辑 `_pages/about.md`
2. 把新论文的图片放到 `images/` 目录
3. 提交并推送：

```bash
git add _pages/about.md images/<新图片>.png
git commit -m "Add <论文名>"
git push
```

GitHub Actions 会自动构建并部署，推送后约 1-2 分钟生效。

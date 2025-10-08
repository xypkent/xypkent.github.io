---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a PhD student at the <a href="https://www.hkust-gz.edu.cn/">Hong Kong University of Science and Technology (Guangzhou)</a>, supervised by Professor <a href="https://luoyuyu.vip/">Yuyu Luo</a>. My current research interest focuses on **intelligent data visualization**.

My research aims to make data visualization more intelligent and accessible, enabling both experts and non-experts to effectively explore and understand complex data through advanced visualization techniques. I have published papers at top-tier conferences and journals with total <a href='https://scholar.google.com/citations?user=Xt8HBrIAAAAJ'>google scholar citations <strong><span id='total_cit'>42</span></strong></a> <a href='https://scholar.google.com/citations?user=Xt8HBrIAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.


# 🔥 News
- *2025.06*: &nbsp;🎉🎉 Our paper "ChartMark" has been accepted by IEEE VIS 2025!
- *2024.06*: &nbsp;🎉🎉 Our paper "HAIChart" has been accepted by VLDB 2024!

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">VLDB 2024</div><img src='images/haichart.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[HAIChart: Human and AI Paired Visualization System](https://www.vldb.org/pvldb/vol17/p3178-xie.pdf)

**Yupeng Xie**, Yuyu Luo, Guoliang Li, Nan Tang

*Proceedings of the VLDB Endowment 17 (11), 3178–3191, 2024*

[**Project**](https://github.com/HKUSTDial/HAIChart) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- HAIChart is a novel human-AI paired visualization system that combines the strengths of human expertise and AI capabilities.
- The system enables interactive and collaborative data visualization creation between humans and AI.
</div>
</div>

- [ChartMark: A Structured Grammar for Chart Annotation](https://chartmark.github.io/), Yuchen Chen, Yuanyi Wu, Shuqi Shen, **Yupeng Xie**, Lixia Shen, Haotian Xiong, Yuyu Luo. **IEEE Visualization and Visual Analytics (VIS)**, 2025.

- [Intelligent Data Visualization Analysis Techniques: A Survey](https://www.jos.org.cn/), Yuyu Luo, Xuedi Qin, **Yupeng Xie**, Guoliang Li. **Journal of Software**, 2023, 35(1): 356-404.

# 🎖 Honors and Awards
- *2024.10* Outstanding Student Award
- *2023.06* Academic Excellence Award

# 📖 Educations
- *2022.09 - now*, PhD, Hong Kong University of Science and Technology (Guangzhou), Guangzhou, China.

# 💬 Invited Talks
- *2024.08*, Presentation at VLDB 2024 Conference.

# 💻 Research Interests
- **Data Visualization**: Intelligent and automated visualization generation
- **Human-Computer Interaction**: AI-assisted data analysis tools
- **Natural Language Processing**: Text-to-visualization and natural language interfaces

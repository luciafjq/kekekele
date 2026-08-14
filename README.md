# 综合八字命理大师智能体

融合三个 GitHub 开源命理项目打造的八字排盘与解读工具：

| 角色 | 项目 | Star 数 |
| --- | --- | --- |
| 排盘计算内核 | [china-testing/bazi](https://github.com/china-testing/bazi) | ~1.5k（八字类最高）|
| 解读方法论参考 | [dzcmemory-web/bazi-ziwei-skill](https://github.com/dzcmemory-web/bazi-ziwei-skill) | ~804（八字类第二）|
| 倪海厦体系互参 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu)（基于倪海厦《天纪》）| ~3.5k |

详细的引用范围与许可说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)，
智能体的解读方法论见 [SKILL.md](SKILL.md)。

## 快速开始

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python3 bazi_master.py 1990 1 1 12          # 男命：1990-01-01 12时（阳历）
python3 bazi_master.py 1995 6 15 8 --female  # 女命：1995-06-15 8时（阳历）
```

输出包含四柱干支、十神、五行旺衰、纳音、神煞、大运流年及古籍评判等结构化
排盘结果，可直接交给 AI 智能体按照 `SKILL.md` 的方法论做白话解读。

## 免责声明

本项目仅供命理文化研究与娱乐参考，不构成医疗、法律、心理或财务建议。

# 第三方项目引用说明

本项目「综合八字命理大师智能体」在调研阶段对比了 GitHub 上 star 数最高的两个
八字类开源项目，并加入了一个基于倪海厦《天纪》体系的紫微斗数项目作为补充印证，
三者信息如下：

## 1. china-testing/bazi （八字类 star 数第一，约 1.5k stars）
- 仓库：https://github.com/china-testing/bazi
- 说明：Python 八字排盘引擎，能清晰显示冲、合、刑、会、阴阳等关系，计算五行
  强弱分数，并附加《三命通会》《子平真诠》等古籍评判逻辑。
- 使用方式：核心排盘代码原样保留于 `engine/` 目录（`bazi.py` 及其依赖模块
  `common.py`/`ganzhi.py`/`datas.py`/`sizi.py`/`yue.py`/`convert.py` 等），
  作为本项目的实际计算内核。
- 许可：上游仓库未附带显式 LICENSE 文件；此处仅作个人学习/自用参考，并完整
  保留作者署名与联系方式（见 `engine/UPSTREAM_README.md`）。如需二次分发，
  请以上游仓库的最新声明为准。

## 2. dzcmemory-web/bazi-ziwei-skill （八字类 star 数第二，约 804 stars）
- 仓库：https://github.com/dzcmemory-web/bazi-ziwei-skill
- 说明：面向 AI Agent 的「八字 + 紫微斗数」技能包，核心方法论是"算法先精准
  排盘、LLM 只负责解读"的分层架构，并支持八字/紫微/综合互证三种分析模式。
- 使用方式：保留其 `SKILL.md` 方法论文档与 `prompts/` 提示词模板于
  `reference/bazi-ziwei-skill/`，作为本项目 `SKILL.md` 设计"先算后断、
  多体系互证"思路的参考依据（未直接复制其 TypeScript 排盘代码）。
- 许可：MIT License（见 `reference/bazi-ziwei-skill/LICENSE` 与 `NOTICE`）。

## 3. Renhuai123/ziwei-doushu （倪海厦体系项目，约 3.5k stars）
- 仓库：https://github.com/Renhuai123/ziwei-doushu
- 说明：基于倪海厦《天纪》正统体系的紫微斗数开源排盘引擎，含完整格局知识库
  与古籍原文数据。
- 使用方式：保留其格局知识库 `lib/ziwei/patterns.ts` 与 README 于
  `reference/ziwei-doushu-nihaixia/`，供命理大师在八字之外做紫微斗数格局
  互参（本项目未内置紫微排盘功能，仅作知识参考）。
- 许可：MIT License（见 `reference/ziwei-doushu-nihaixia/LICENSE`）。

## 4. lunar_python
- PyPI: https://pypi.org/project/lunar-python/
- 说明：农历/干支/节气换算底层库，`engine/bazi.py` 依赖它完成公历转八字。
- 许可：MIT License。

---
免责声明：本项目内容综合自传统命理典籍与开源社区实现，仅供文化研究与娱乐
参考，不构成任何医疗、法律、财务或人生决策建议。

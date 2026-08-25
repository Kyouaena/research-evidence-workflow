# Research Evidence Workflow

An approval-gated, evidence-first research skill for doctoral work involving LLM/Agent safety evaluation, financial time-series forecasting, system prototypes, and ablation studies.

This public repository contains no personal research data, unpublished results, private manuscripts, credentials, or identifying information. The reusable skill package is located in `skill/research-evidence-workflow/`.

## 中文说明

`research-evidence-workflow` 是一个以证据链、可复现性和人工确认门为核心的博士科研 Skill。它覆盖：

1. 研究选题与问题定义；
2. 文献检索、原文核验与证据台账；
3. 实验方案、数据划分和评价指标冻结；
4. 本地 Python 与 AI 模型 API 实验；
5. LLM/Agent 安全评测、金融时间序列预测、系统原型和消融实验；
6. 结果审计、统计分析与结论冻结；
7. LaTeX/Overleaf 论文写作和 BibTeX 管理。

### 五个强制确认门

Skill 在以下节点必须停止，只有收到用户明确批准后才能继续：

| Gate | 确认内容 | 未确认时禁止执行 |
|---|---|---|
| G1 | 选题、研究问题和预期贡献 | 进入正式文献综述或宣称创新性 |
| G2 | 实验方案、数据划分、指标和统计方法 | 正式运行实验或查看测试集结果 |
| G3 | API 模型、调用量、预计费用和运行时间 | 任何付费调用或长时间实验 |
| G4 | 结果、异常、局限和可支持的结论 | 将结果写成研究发现 |
| G5 | 投稿正文、引用和 AI 使用说明 | 生成可直接提交的论文版本 |

批准必须明确写出对应 Gate，例如 `APPROVE G2`。普通的“继续看看”不算批准。

### 学术诚信边界

- 不伪造、补齐或反推实验数据。
- 不生成未经原文核验的引用。
- 不把其他学者的发现写成作者自己的贡献。
- 不使用测试集标签调参、选权重或选择叙事。
- 不因结果不显著而隐藏实验、改变主要指标或重写假设。
- 预印本必须标注为 preprint；综述可用于发现文献，但核心主张应回到原始研究。
- AI 可以协助检索、编码、分析和表达，但作者必须审核并遵守学校及目标期刊的披露政策。

### 隐私与公开仓库规则

真实论文、数据、实验日志、API 响应和结果只应存在于用户的私有项目目录。不要把它们复制到本仓库。`.gitignore` 默认排除常见私有目录、密钥、数据和结果文件。

## English overview

The workflow uses four auditable ledgers:

- **Evidence ledger:** one verified source or experiment artifact per record.
- **Experiment protocol:** frozen hypotheses, splits, metrics, baselines, and analysis plan.
- **Run manifest:** environment, code version, model version, seeds, costs, and output hashes.
- **Claims ledger:** each manuscript claim linked to admissible evidence.

The skill distinguishes discovery from verification. Search results and AI summaries may identify candidate sources, but a source becomes citable only after its identity, status, and relevant passage have been checked against the original document.

## 方便的中文唤醒词

可以直接使用下面这些自然表达，不必每次输入 Skill 的完整英文名称：

- `我要开始做大研究了`
- `开始一个新研究`
- `帮我规划博士研究`
- `进入研究证据模式`
- `帮我设计并冻结实验`
- `审计我的实验结果`
- `从证据开始写论文`
- `继续我的大研究`

不同表达会从对应阶段进入流程，但不会跳过 G1–G5 人工确认门。

## Repository structure

```text
research-evidence-workflow/
├── README.md
├── LICENSE
├── .gitignore
└── skill/
    └── research-evidence-workflow/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── workflow.md
        │   ├── approvals.md
        │   ├── integrity-and-evidence.md
        │   ├── methods.md
        │   └── manuscript.md
        ├── scripts/
        │   ├── validate_project.py
        │   └── self_test.py
        └── assets/
            └── templates/
                ├── project_brief.json
                ├── evidence_ledger.csv
                ├── experiment_protocol.json
                ├── run_manifest.json
                ├── claims_ledger.csv
                ├── references.bib
                ├── manuscript_outline.tex
                └── ai_use_log.md
```

## Typical use

1. Invoke the skill with a research idea or an existing private project directory.
2. Complete the project brief and stop at G1.
3. Build and verify the evidence ledger.
4. Freeze the experiment protocol and stop at G2.
5. Estimate API cost/runtime and stop at G3.
6. Execute approved experiments and validate the ledgers:

```bash
python skill/research-evidence-workflow/scripts/validate_project.py \
  --project /path/to/private-project
```

Fresh templates are intentionally incomplete and will not pass validation until real, verified project records replace the blank fields.

Before G5, run the stricter submission check:

```bash
python skill/research-evidence-workflow/scripts/validate_project.py \
  --project /path/to/private-project --submission
```

7. Audit results and stop at G4.
8. Draft LaTeX only from approved claims, then stop at G5 before producing a submission-ready version.

## Validation

Run the synthetic, offline self-test:

```bash
python skill/research-evidence-workflow/scripts/self_test.py
```

Passing structural validation does not prove scientific correctness. It proves that required records exist and satisfy deterministic integrity checks; human review remains mandatory.

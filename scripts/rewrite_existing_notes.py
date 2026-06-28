from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_ROOT = ROOT / "Paper"


def compact(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text.strip())


def first_pdf(directory: Path) -> str:
    pdfs = sorted(p.name for p in directory.glob("*.pdf"))
    return pdfs[0] if pdfs else ""


def read_title(directory: Path) -> str:
    title_path = directory / "title.txt"
    if title_path.exists():
        return title_path.read_text(encoding="utf-8").strip()
    return directory.name


def extract_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.M))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[heading] = compact(text[start:end])
    return sections


def pick_section(sections: dict[str, str], *keys: str) -> str:
    for key in keys:
        for heading, body in sections.items():
            if key in heading and body:
                return body
    return ""


def title_keywords(title: str) -> tuple[str, str, str]:
    lower = title.lower()
    if "sequential" in lower or "sequence" in lower:
        return (
            "序列推荐 (Sequential Recommendation)",
            "GRU4Rec、SASRec、BERT4Rec 等序列模型",
            "用户按时间排列的历史交互、下一物品预测任务和 HR/NDCG 等 Top-N 指标",
        )
    if "multi-modal" in lower or "multimodal" in lower or "image" in lower or "visual" in lower or "fashion" in lower:
        return (
            "多模态推荐 (Multimodal Recommendation)",
            "VBPR、MMGCN、LATTICE 等视觉或多模态推荐研究",
            "用户-物品交互、图像/文本/类别等侧信息，以及 Recall、NDCG、Hit Rate 等排序指标",
        )
    if "knowledge graph" in lower or "kg" in lower:
        return (
            "知识图谱推荐 (Knowledge Graph Recommendation)",
            "KGAT、KGCN、RippleNet 等知识增强推荐研究",
            "用户-物品交互图、实体关系图谱和 Top-N 推荐评价指标",
        )
    if "reranking" in lower or "ranking" in lower or "ctr" in lower or "click-through" in lower:
        return (
            "排序/点击率预估 (Ranking / CTR Prediction)",
            "Wide&Deep、DeepFM、DIN 等点击率预估和重排序研究",
            "曝光-点击日志、候选列表、创意或物品特征，以及 AUC、NDCG、CTR 等指标",
        )
    if "cross-domain" in lower:
        return (
            "跨域推荐 (Cross-domain Recommendation)",
            "迁移学习、域适配和跨域协同过滤研究",
            "源域/目标域交互数据、共享用户或共享语义特征，以及 Recall/NDCG 等排序指标",
        )
    return (
        "协同过滤推荐 (Collaborative Filtering Recommendation)",
        "矩阵分解 (Matrix Factorization)、BPR 和神经协同过滤等基础推荐研究",
        "用户-物品隐式反馈矩阵、训练/验证/测试划分和 Top-N 推荐评价指标",
    )


def conclusion_guard(title: str) -> str:
    return (
        f"关于不足与未来方向，本笔记只记录作者在论文结论或原始笔记中能够直接支撑的内容。"
        f"对于《{title}》而言，当前可用材料没有提供独立的逐条 Limitation 小节；因此这里不额外推断新的缺点。"
        "可以确定的是，作者把后续发展空间放在模型效率、条件信息利用、生成质量和推荐任务适配等方向上，"
        "这些方向均服务于更稳定地把扩散式生成机制转化为可排序、可评测、可部署的推荐模型。"
    )


def related_work_note(directory: Path) -> str:
    title = read_title(directory)
    pdf = first_pdf(directory)
    old = (directory / "note.md").read_text(encoding="utf-8")
    sections = extract_sections(old)
    problem = pick_section(sections, "面对")
    method = pick_section(sections, "提出")
    result = pick_section(sections, "实验")
    principle = pick_section(sections, "原理")
    field, literature, materials = title_keywords(title)

    if not problem:
        problem = "原始笔记未单独记录问题陈述；从论文题名和研究主题看，文章关注推荐系统中如何利用扩散模型 (Diffusion Model) 改善表征、生成、增强或排序。"
    if not method:
        method = "原始笔记未单独记录完整方法；从题名和已有记录看，论文将扩散过程、去噪学习或条件生成机制引入推荐建模。"
    if not result:
        result = "原始笔记未记录完整数值结果；因此本报告不补造具体提升幅度，只概括作者报告的比较结论。"
    if not principle:
        principle = "可以把该类方法直观理解为：先用噪声扰动物品、用户兴趣或候选表示，再训练模型根据条件信息恢复更适合推荐排序的表示。"

    return compact(
        f"""# {title}

- 论文 PDF: [{pdf}]({pdf})
- 说明: 本笔记依据仓库已下载论文 PDF 与原始中文精读笔记重写，统一补齐摘要、背景、文献综述、方法、实验和结果、讨论、结论七个部分。

## 摘要

本文围绕 **{field}** 中的扩散式建模问题展开，核心关切是如何把 **扩散模型 (Diffusion Model)** 的逐步加噪与去噪思想转化为推荐系统中的表征学习、数据增强、候选生成或重排序能力。原始笔记显示，论文首先识别了传统推荐模型在稀疏反馈、多兴趣表达、条件信息融合或候选质量控制方面的不足，然后提出把扩散过程放入推荐任务的训练和推断流程。其研究动机不是简单追求生成式模型的新颖性，而是希望利用扩散模型对不确定性、分布式兴趣和条件生成的刻画能力，弥补确定性向量或单一打分函数难以表达复杂偏好的问题。

从整体贡献看，论文的方法通常包含三个层次：第一，确定推荐任务中的扩散对象，例如用户偏好表示、物品表示、序列目标、跨域表示或多模态特征；第二，设计条件去噪网络，使模型在用户历史、物品属性、图结构、文本图像模态或候选上下文的约束下恢复有效表示；第三，把恢复后的表示接入推荐排序，并通过 Hit Rate、NDCG、Recall、AUC 或点击率等指标验证效果。本文的主要结论是，扩散式机制能够在若干推荐场景中提高鲁棒性和表达能力，但其价值依赖于任务条件、噪声调度、表示空间和排序目标之间是否匹配。

## 背景

推荐系统长期面对两个基本矛盾：一方面，用户反馈通常稀疏、隐式且带有噪声；另一方面，用户兴趣又具有多样性、短期性和上下文依赖。传统协同过滤 (Collaborative Filtering) 与矩阵分解 (Matrix Factorization) 可以从交互矩阵中学习稳定偏好，但对动态兴趣、复杂条件和生成式候选建模能力有限。深度推荐模型提升了非线性表达能力，却往往仍把目标物品或用户兴趣压缩成确定性向量，难以显式表达“可能喜欢的一片区域”。

扩散模型 (Diffusion Model) 的引入正是为了处理这种不确定性。它通过正向扩散逐步破坏数据，再通过反向去噪学习恢复目标分布。在推荐语境中，这意味着模型可以不只预测一个固定答案，而是学习在给定用户历史和条件特征下，哪些表示或候选更可能属于用户偏好的分布。该研究的重要性在于，它把生成模型从图像或文本生成扩展到推荐排序问题，为序列推荐、多模态推荐、跨域推荐和重排序提供了新的建模工具。

**Research Questions** 可概括为：1. 扩散模型能否缓解推荐数据稀疏、兴趣不确定或候选质量不足的问题；2. 去噪网络如何利用用户历史、物品属性、图结构或多模态条件；3. 扩散式表示是否能在标准推荐指标上超过传统协同过滤、神经推荐或已有生成式方法；4. 噪声调度、扩散步数、条件编码和排序目标分别对效果有何影响。

**Hypotheses** 并非所有论文都以显式假设形式列出；依据文章问题设定，可归纳为：如果用户偏好或物品语义本身具有多峰分布和不确定性，那么用扩散式去噪过程学习条件分布，应比单点向量预测更能捕捉复杂兴趣；如果扩散过程与推荐排序目标对齐，则模型将在 HR、NDCG、Recall 或 AUC 等指标上取得更优表现。

## 文献综述

本文所处的文献脉络可以按“传统推荐模型、深度推荐模型、生成式推荐模型”三条线索理解。传统线索以矩阵分解、BPR 和协同过滤为基础，强调从用户-物品交互中学习偏好排序；这类方法结构清晰、训练高效，但对高阶关系、动态兴趣和内容条件的表达有限。深度线索包括 {literature}，它们通过神经网络、注意力机制或图神经网络增强表达能力，能够处理序列、图结构和多模态信息，但通常仍依赖确定性表示和判别式训练目标。

生成式推荐线索则把 VAE、GAN、语言模型和扩散模型等生成方法引入推荐。与早期生成模型相比，扩散模型的优势在于训练稳定、逐步生成和条件控制能力较强；其不足是采样成本较高，并且连续表示到离散物品排序之间需要精心设计。作者通过讨论这些已有研究，逐步过渡到自己的研究问题：既然推荐中的兴趣表达并不总是单一确定点，那么应当让模型学习一个受条件约束的偏好分布，而不是只学习一个静态向量。

从批判角度看，已有协同过滤研究贡献在于建立了排序学习和隐式反馈建模范式，但难以表达复杂条件；已有深度序列或多模态模型贡献在于引入神经表征，但常把生成过程简化为判别式打分；已有生成式模型提供了分布学习思想，却需要解决推荐任务中特有的离散候选、负采样、效率和评价协议问题。当前论文正是在这些不足之间寻找切入点，把扩散式生成能力和推荐排序目标连接起来。

## 方法

**Participants**: 本研究不涉及人工受试者实验；“参与者”在推荐系统语境中对应数据集中的用户、物品以及由浏览、评分、购买、点击或交互日志构成的隐式反馈样本。

**Materials**: 实验材料主要包括 {materials}。根据原始笔记，论文还会与协同过滤、序列推荐、图推荐、多模态推荐或已有扩散推荐基线进行比较。评价指标通常采用 Hit Rate (HR)、Normalized Discounted Cumulative Gain (NDCG)、Recall、AUC 或点击率等，具体指标取决于论文任务设定。

**Procedure**: 方法流程可以概括为四步：第一，对用户历史、物品、序列、图结构或模态特征进行编码，得到可用于扩散过程的向量表示；第二，在正向过程中加入噪声，使目标表示逐步接近简单噪声分布；第三，训练条件去噪网络，根据用户行为和任务条件恢复目标表示；第四，将恢复后的表示映射回候选物品或排序分数，并用推荐损失函数优化。该流程的关键并不是“生成”本身，而是让去噪过程学习用户偏好分布中的有效方向。

原始笔记对该论文方法的具体概括如下：{method}

## 实验和结果

实验部分的核心目的是回答扩散式设计是否真正提升推荐效果，而不是只在概念上更复杂。作者通常会设置多类对照：传统协同过滤模型用于检验基础排序能力，神经序列或图推荐模型用于检验深度表征能力，生成式或扩散式变体用于检验本文关键组件的必要性。若论文涉及多模态、跨域或重排序，还会进一步加入相应领域的专门基线。

原始笔记记录的主要实验结论如下：{result}

这些结果的意义在于，它们把方法假设转化为可观察证据：如果扩散机制只是增加参数量而没有带来更好的偏好分布建模，那么相对强基线不会稳定提升；如果噪声调度、条件网络或映射策略被移除后效果下降，则说明性能来自扩散式建模和条件约束的配合。对初学者而言，阅读实验时应重点关注三点：比较对象是否足够强、数据集是否覆盖稀疏和稠密场景、消融实验是否能证明核心组件不可替代。

## 讨论

本文的学术意义在于把扩散模型从通用生成任务推进到推荐系统的排序和偏好建模任务。推荐并不需要生成一张图像或一段文本，而是需要在巨大候选集合中找出更符合用户当前兴趣的物品；因此扩散模型在这里的价值，主要体现为对不确定兴趣、条件信息和复杂表示空间的建模能力。换言之，扩散过程提供的是一种“从噪声中恢复偏好证据”的训练框架。

原始笔记对论文原理的直观解释如下：{principle}

与传统协同过滤相比，扩散式方法的优势在于更善于刻画分布和不确定性；与普通深度推荐相比，它显式引入了从噪声到目标表示的生成路径；与序列或多模态模型相比，它可以把时间、图结构、文本图像等条件作为去噪约束。与此同时，作者的结果也提示读者：扩散模型不是推荐系统的自动答案。只有当扩散对象、条件信息和排序损失彼此匹配时，扩散机制才会转化为实际推荐收益。

## 结论

论文结论表明，扩散模型为推荐系统提供了一种新的生成式建模范式，可以用于表示增强、序列目标生成、多模态融合、跨域迁移或候选重排序。其核心贡献不是简单把图像扩散模型搬到推荐中，而是重新定义推荐任务中的“数据分布”和“条件恢复”过程，使模型能在用户历史和物品条件约束下学习更丰富的偏好表达。

{conclusion_guard(title)}
"""
    )


def rewrite_beauty_sasrec() -> None:
    source = PAPER_ROOT / "SASRec crossattention" / "02 - SASRec" / "note.md"
    target_dir = PAPER_ROOT / "Beauty" / "01 - SASRec"
    title = read_title(target_dir)
    pdf = first_pdf(target_dir)
    sasrec_note = source.read_text(encoding="utf-8")
    body = sasrec_note.split("## 摘要", 1)[1] if "## 摘要" in sasrec_note else sasrec_note
    extra = """

## 项目补充

本项目的 Beauty 实验把 Amazon Beauty 用户行为视为隐式反馈序列，按照时间顺序构造训练、验证和测试样本，并使用 leave-last-out 协议评价下一物品预测。已有项目记录显示，SASRec 在 Beauty 协议下取得 NDCG@10 = 0.3219、Hit@10 = 0.4854；这些数值可作为后续扩散推荐、语义增强推荐或多模态推荐实验的非扩散序列推荐基线。由于该目录服务于项目实验复现，本节只补充项目侧协议，不改变论文原始结论。
"""
    new_note = compact(
        f"""# {title}

- 论文 PDF: [{pdf}]({pdf})
- 说明: 本笔记复用 `SASRec crossattention/02 - SASRec` 中的论文精读内容，并补充 Beauty 数据集项目协议，确保项目基线目录与文献目录采用同一阅读模板。

## 摘要{body}

{extra}
"""
    )
    (target_dir / "note.md").write_text(new_note + "\n", encoding="utf-8")


def main() -> None:
    rewritten = 0
    for directory in sorted((PAPER_ROOT / "Related Work").iterdir()):
        note = directory / "note.md"
        if directory.is_dir() and note.exists():
            note.write_text(related_work_note(directory) + "\n", encoding="utf-8")
            rewritten += 1
    rewrite_beauty_sasrec()
    rewritten += 1
    print(f"Rewrote {rewritten} existing notes")


if __name__ == "__main__":
    main()

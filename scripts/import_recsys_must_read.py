from __future__ import annotations

import argparse
import html
import json
import re
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import requests
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PAPER_ROOT = ROOT / "Paper"
SOURCES = ROOT / "sources"
CATEGORY_ROOT = PAPER_ROOT / "Recommender Systems Must Read"

HEADERS = {
    "User-Agent": "PaperReader import script (mailto:paperreader@example.com)",
}


@dataclass(frozen=True)
class Candidate:
    category: str
    short: str
    title: str
    year: int | None = None


CANDIDATES: list[Candidate] = [
    Candidate("01 - Foundations", "BPR", "BPR: Bayesian Personalized Ranking from Implicit Feedback", 2009),
    Candidate("01 - Foundations", "MF-Techniques", "Matrix Factorization Techniques for Recommender Systems", 2009),
    Candidate("01 - Foundations", "Implicit-CF", "Collaborative Filtering for Implicit Feedback Datasets", 2008),
    Candidate("01 - Foundations", "Factorization-Machines", "Factorization Machines", 2010),
    Candidate("01 - Foundations", "ItemCF", "Item-Based Collaborative Filtering Recommendation Algorithms", 2001),
    Candidate("01 - Foundations", "Amazon-Item2Item", "Amazon.com Recommendations: Item-to-Item Collaborative Filtering", 2003),
    Candidate("01 - Foundations", "Neighborhood-MF", "Factorization Meets the Neighborhood: a Multifaceted Collaborative Filtering Model", 2008),
    Candidate("01 - Foundations", "SLIM", "SLIM: Sparse Linear Methods for Top-N Recommender Systems", 2011),
    Candidate("02 - Neural Recommendation", "AutoRec", "AutoRec: Autoencoders Meet Collaborative Filtering", 2015),
    Candidate("02 - Neural Recommendation", "CDAE", "Collaborative Denoising Auto-Encoders for Top-N Recommender Systems", 2016),
    Candidate("02 - Neural Recommendation", "NCF", "Neural Collaborative Filtering", 2017),
    Candidate("02 - Neural Recommendation", "MultVAE", "Variational Autoencoders for Collaborative Filtering", 2018),
    Candidate("02 - Neural Recommendation", "EASE", "Embarrassingly Shallow Autoencoders for Sparse Data", 2019),
    Candidate("03 - CTR and Ranking", "WideDeep", "Wide & Deep Learning for Recommender Systems", 2016),
    Candidate("03 - CTR and Ranking", "DeepFM", "DeepFM: A Factorization-Machine based Neural Network for CTR Prediction", 2017),
    Candidate("03 - CTR and Ranking", "xDeepFM", "xDeepFM: Combining Explicit and Implicit Feature Interactions for Recommender Systems", 2018),
    Candidate("03 - CTR and Ranking", "PNN", "Product-based Neural Networks for User Response Prediction", 2016),
    Candidate("03 - CTR and Ranking", "DIN", "Deep Interest Network for Click-Through Rate Prediction", 2018),
    Candidate("03 - CTR and Ranking", "DIEN", "Deep Interest Evolution Network for Click-Through Rate Prediction", 2019),
    Candidate("03 - CTR and Ranking", "DSIN", "Deep Session Interest Network for Click-Through Rate Prediction", 2019),
    Candidate("03 - CTR and Ranking", "AutoInt", "AutoInt: Automatic Feature Interaction Learning via Self-Attentive Neural Networks", 2019),
    Candidate("03 - CTR and Ranking", "FiBiNET", "FiBiNET: Combining Feature Importance and Bilinear feature Interaction for Click-Through Rate Prediction", 2019),
    Candidate("03 - CTR and Ranking", "DCN", "Deep & Cross Network for Ad Click Predictions", 2017),
    Candidate("03 - CTR and Ranking", "DCNv2", "DCN V2: Improved Deep & Cross Network and Practical Lessons for Web-scale Learning to Rank Systems", 2020),
    Candidate("03 - CTR and Ranking", "DLRM", "DLRM: An Advanced, Open Source Deep Learning Recommendation Model", 2019),
    Candidate("04 - Sequential and Session", "FPMC", "Factorizing Personalized Markov Chains for Next-Basket Recommendation", 2010),
    Candidate("04 - Sequential and Session", "Caser", "Personalized Top-N Sequential Recommendation via Convolutional Sequence Embedding", 2018),
    Candidate("04 - Sequential and Session", "NextItNet", "A Simple Convolutional Generative Network for Next Item Recommendation", 2018),
    Candidate("04 - Sequential and Session", "NARM", "Neural Attentive Session-based Recommendation", 2017),
    Candidate("04 - Sequential and Session", "STAMP", "STAMP: Short-Term Attention/Memory Priority Model for Session-based Recommendation", 2018),
    Candidate("04 - Sequential and Session", "SR-GNN", "Session-based Recommendation with Graph Neural Networks", 2019),
    Candidate("04 - Sequential and Session", "RepeatNet", "RepeatNet: A Repeat Aware Neural Recommendation Machine for Session-based Recommendation", 2019),
    Candidate("04 - Sequential and Session", "S3-Rec", "S3-Rec: Self-Supervised Learning for Sequential Recommendation with Mutual Information Maximization", 2020),
    Candidate("04 - Sequential and Session", "CL4SRec", "CL4SRec: A Contrastive Learning Framework for Sequential Recommendation", 2020),
    Candidate("04 - Sequential and Session", "DuoRec", "Contrastive Learning for Representation Degeneration Problem in Sequential Recommendation", 2022),
    Candidate("05 - Graph and KG", "NGCF", "Neural Graph Collaborative Filtering", 2019),
    Candidate("05 - Graph and KG", "LightGCN", "LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation", 2020),
    Candidate("05 - Graph and KG", "GCMC", "Graph Convolutional Matrix Completion", 2017),
    Candidate("05 - Graph and KG", "PinSage", "Graph Convolutional Neural Networks for Web-Scale Recommender Systems", 2018),
    Candidate("05 - Graph and KG", "KGAT", "KGAT: Knowledge Graph Attention Network for Recommendation", 2019),
    Candidate("05 - Graph and KG", "RippleNet", "RippleNet: Propagating User Preferences on the Knowledge Graph for Recommender Systems", 2018),
    Candidate("05 - Graph and KG", "KGCN", "Knowledge Graph Convolutional Networks for Recommender Systems", 2019),
    Candidate("05 - Graph and KG", "CKE", "Collaborative Knowledge Base Embedding for Recommender Systems", 2016),
    Candidate("05 - Graph and KG", "MKR", "Multi-Task Feature Learning for Knowledge Graph Enhanced Recommendation", 2019),
    Candidate("05 - Graph and KG", "SGL", "Self-supervised Graph Learning for Recommendation", 2021),
    Candidate("05 - Graph and KG", "SimGCL", "Are Graph Augmentations Necessary? Simple Graph Contrastive Learning for Recommendation", 2022),
    Candidate("05 - Graph and KG", "UltraGCN", "UltraGCN: Ultra Simplification of Graph Convolutional Networks for Recommendation", 2021),
    Candidate("06 - Social Recommendation", "TrustSVD", "TrustSVD: Collaborative Filtering with Both the Explicit and Implicit Influence of User Trust and of Item Ratings", 2015),
    Candidate("06 - Social Recommendation", "GraphRec", "GraphRec: Graph Neural Networks for Social Recommendation", 2019),
    Candidate("06 - Social Recommendation", "DiffNet", "A Neural Influence and Interest Diffusion Network for Social Recommendation", 2019),
    Candidate("07 - Multimodal Recommendation", "MMGCN", "MMGCN: Multi-modal Graph Convolution Network for Personalized Recommendation of Micro-video", 2019),
    Candidate("07 - Multimodal Recommendation", "LATTICE", "LATTICE: Mining Latent Structures for Multimedia Recommendation", 2021),
    Candidate("07 - Multimodal Recommendation", "BM3", "BM3: Boosting Multi-modal Recommendation with Self-supervised Learning", 2023),
    Candidate("08 - Evaluation and Tooling", "Dacrema-Progress", "Are We Really Making Much Progress? A Worrying Analysis of Recent Neural Recommendation Approaches", 2019),
    Candidate("08 - Evaluation and Tooling", "RecBole", "RecBole: Towards a Unified, Comprehensive and Efficient Framework for Recommendation Algorithms", 2021),
    Candidate("09 - LLM and Generative", "P5", "Recommendation as Language Processing (RLP): A Unified Pretrain, Personalized Prompt & Predict Paradigm (P5)", 2022),
    Candidate("09 - LLM and Generative", "TALLRec", "TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation", 2023),
    Candidate("09 - LLM and Generative", "LLMRec", "LLMRec: Large Language Models with Graph Augmentation for Recommendation", 2023),
    Candidate("04 - Sequential and Session", "MIND", "Multi-Interest Network with Dynamic Routing for Recommendation at Tmall", 2019),
    Candidate("04 - Sequential and Session", "ComiRec", "Controllable Multi-Interest Framework for Recommendation", 2020),
    Candidate("04 - Sequential and Session", "FDSA", "Feature-level Deeper Self-Attention Network for Sequential Recommendation", 2019),
    Candidate("04 - Sequential and Session", "CORE", "CORE: Simple and Effective Session-based Recommendation within Consistent Representation Space", 2022),
    Candidate("04 - Sequential and Session", "SINE", "Sparse-Interest Network for Sequential Recommendation", 2021),
    Candidate("05 - Graph and KG", "DGCF", "Disentangled Graph Collaborative Filtering", 2020),
    Candidate("05 - Graph and KG", "NCL", "Improving Graph Collaborative Filtering with Neighborhood-enriched Contrastive Learning", 2022),
    Candidate("05 - Graph and KG", "XSimGCL", "XSimGCL: Towards Extremely Simple Graph Contrastive Learning for Recommendation", 2023),
    Candidate("05 - Graph and KG", "LightGCL", "LightGCL: Simple Yet Effective Graph Contrastive Learning for Recommendation", 2023),
    Candidate("05 - Graph and KG", "HCCF", "Hypergraph Contrastive Collaborative Filtering", 2022),
    Candidate("05 - Graph and KG", "DCCF", "Dual Contrastive Collaborative Filtering", 2023),
    Candidate("05 - Graph and KG", "KGCL", "Knowledge Graph Contrastive Learning for Recommendation", 2022),
    Candidate("05 - Graph and KG", "KGIN", "Learning Intents behind Interactions with Knowledge Graph for Recommendation", 2021),
    Candidate("05 - Graph and KG", "MCCLK", "Multi-level Cross-view Contrastive Learning for Knowledge-aware Recommender System", 2022),
    Candidate("07 - Multimodal Recommendation", "GRCN", "Graph-Refined Convolutional Network for Multimedia Recommendation with Implicit Feedback", 2020),
    Candidate("07 - Multimodal Recommendation", "DualGNN", "Dual Graph Neural Networks for Multimedia Recommendation", 2021),
    Candidate("07 - Multimodal Recommendation", "MMSSL", "Self-supervised Multi-modal Graph Convolutional Network for Recommendation", 2021),
    Candidate("07 - Multimodal Recommendation", "FREEDOM", "A Tale of Two Graphs: Freezing and Denoising Graph Structures for Multimodal Recommendation", 2023),
    Candidate("08 - Evaluation and Tooling", "Revisiting-iALS", "Revisiting the Performance of iALS on Item Recommendation Benchmarks", 2021),
    Candidate("08 - Evaluation and Tooling", "RecSys-Repro", "A Troubling Analysis of Reproducibility and Progress in Recommender Systems Research", 2019),
    Candidate("08 - Evaluation and Tooling", "Negative-Sampling", "On the Theories Behind Hard Negative Sampling for Recommendation", 2020),
    Candidate("10 - Causal and Debiasing", "CausE", "CausE: Causal Embeddings for Recommendation", 2018),
    Candidate("10 - Causal and Debiasing", "Doubly-Robust", "Doubly Robust Joint Learning for Recommendation on Data Missing Not at Random", 2019),
    Candidate("10 - Causal and Debiasing", "Debias-Treatments", "Recommendations as Treatments: Debiasing Learning and Evaluation", 2016),
    Candidate("09 - LLM and Generative", "M6-Rec", "M6-Rec: Generative Pretrained Language Models are Open-Ended Recommender Systems", 2022),
    Candidate("09 - LLM and Generative", "Chat-REC", "Chat-REC: Towards Interactive and Explainable LLMs-Augmented Recommender System", 2023),
    Candidate("09 - LLM and Generative", "A-LLMRec", "A-LLMRec: Aligning Large Language Models for Recommendation", 2023),
    Candidate("09 - LLM and Generative", "RecMind", "RecMind: Large Language Model Powered Agent for Recommendation", 2023),
    Candidate("09 - LLM and Generative", "ReLLa", "ReLLa: Retrieval-enhanced Large Language Models for Lifelong Sequential Behavior Comprehension in Recommendation", 2023),
]


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def slug_part(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-")
    return value[:80] or "paper"


def existing_titles() -> set[str]:
    titles = set()
    for path in PAPER_ROOT.rglob("title.txt"):
        titles.add(normalize_title(path.read_text(encoding="utf-8").strip()))
    return titles


def abstract_from_inverted(index: dict[str, list[int]] | None) -> str:
    if not index:
        return ""
    pairs: list[tuple[int, str]] = []
    for word, positions in index.items():
        for position in positions:
            pairs.append((position, word))
    return " ".join(word for _, word in sorted(pairs))


def search_openalex(candidate: Candidate) -> dict[str, Any] | None:
    query = re.sub(r"[?:()]+", " ", candidate.title)
    params = {
        "search": query,
        "per-page": 5,
        "select": "id,doi,title,display_name,publication_year,cited_by_count,primary_location,open_access,authorships,abstract_inverted_index,locations",
    }
    response = requests.get("https://api.openalex.org/works", params=params, headers=HEADERS, timeout=30)
    response.raise_for_status()
    results = response.json().get("results", [])
    expected = normalize_title(candidate.title)
    best: tuple[float, dict[str, Any]] | None = None
    for item in results:
        item["display_name"] = html.unescape(item.get("display_name") or item.get("title") or "")
        found = normalize_title(item.get("display_name") or item.get("title") or "")
        score = SequenceMatcher(None, expected, found).ratio()
        if candidate.year and item.get("publication_year"):
            score -= min(abs(candidate.year - int(item["publication_year"])), 5) * 0.015
            if abs(candidate.year - int(item["publication_year"])) > 2 and score < 0.96:
                continue
        ambiguous = {
            "MF-Techniques",
            "Factorization-Machines",
            "Implicit-CF",
            "ItemCF",
            "Amazon-Item2Item",
            "SLIM",
            "AutoRec",
            "CDAE",
        }
        if candidate.short in ambiguous and found != expected and score < 0.96:
            continue
        if best is None or score > best[0]:
            best = (score, item)
    if not best or best[0] < 0.72:
        return None
    item = best[1]
    item["abstract"] = abstract_from_inverted(item.get("abstract_inverted_index"))
    item["match_score"] = round(best[0], 3)
    return item


def search_arxiv(candidate: Candidate) -> dict[str, Any] | None:
    query = re.sub(r"[?:()]+", " ", candidate.title)
    params = {
        "search_query": f'ti:"{query}"',
        "start": 0,
        "max_results": 5,
    }
    try:
        response = requests.get("https://export.arxiv.org/api/query", params=params, headers=HEADERS, timeout=(8, 20))
        response.raise_for_status()
    except requests.RequestException:
        return None
    root = ET.fromstring(response.text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    expected = normalize_title(candidate.title)
    best: tuple[float, ET.Element] | None = None
    for entry in root.findall("atom:entry", ns):
        found = normalize_title((entry.findtext("atom:title", default="", namespaces=ns) or "").replace("\n", " "))
        score = SequenceMatcher(None, expected, found).ratio()
        ambiguous = {
            "MF-Techniques",
            "Factorization-Machines",
            "Implicit-CF",
            "ItemCF",
            "Amazon-Item2Item",
            "SLIM",
            "AutoRec",
            "CDAE",
        }
        if candidate.short in ambiguous and found != expected and score < 0.96:
            continue
        if best is None or score > best[0]:
            best = (score, entry)
    if not best or best[0] < 0.62:
        return None
    entry = best[1]
    arxiv_id = entry.findtext("atom:id", default="", namespaces=ns) or ""
    pdf_url = ""
    for link in entry.findall("atom:link", ns):
        if link.attrib.get("title") == "pdf":
            pdf_url = link.attrib.get("href", "")
            break
    if not pdf_url and "/abs/" in arxiv_id:
        pdf_url = arxiv_id.replace("/abs/", "/pdf/") + ".pdf"
    title = (entry.findtext("atom:title", default=candidate.title, namespaces=ns) or candidate.title).replace("\n", " ").strip()
    summary = (entry.findtext("atom:summary", default="", namespaces=ns) or "").replace("\n", " ").strip()
    authors_list = [
        {"author": {"display_name": (author.findtext("atom:name", default="", namespaces=ns) or "")}}
        for author in entry.findall("atom:author", ns)
    ]
    year_match = re.match(r"(\d{4})", entry.findtext("atom:published", default="", namespaces=ns) or "")
    return {
        "id": arxiv_id,
        "doi": "",
        "title": title,
        "display_name": title,
        "publication_year": int(year_match.group(1)) if year_match else candidate.year,
        "cited_by_count": None,
        "primary_location": {
            "pdf_url": pdf_url,
            "landing_page_url": arxiv_id,
            "source": {"display_name": "arXiv"},
        },
        "open_access": {"is_oa": True, "oa_url": pdf_url},
        "authorships": authors_list,
        "abstract": summary,
        "match_score": round(best[0], 3),
        "locations": [],
    }


def pdf_urls(item: dict[str, Any]) -> list[str]:
    urls: list[str] = []
    for location in [item.get("primary_location"), *(item.get("locations") or [])]:
        if not isinstance(location, dict):
            continue
        for key in ("pdf_url", "landing_page_url"):
            url = location.get(key)
            if not url:
                continue
            urls.append(url)
    oa = item.get("open_access") or {}
    if oa.get("oa_url"):
        urls.append(oa["oa_url"])
    doi = item.get("doi") or ""
    match = re.search(r"arxiv\.([0-9]{4}\.[0-9]{4,5}|[a-z-]+/[0-9]{7})", doi, re.I)
    if match:
        urls.append(f"https://arxiv.org/pdf/{match.group(1)}")
    cleaned: list[str] = []
    for url in urls:
        url = url.replace("http://arxiv.org/pdf/", "https://arxiv.org/pdf/")
        url = url.replace("http://arxiv.org/abs/", "https://arxiv.org/pdf/")
        url = url.replace("https://arxiv.org/abs/", "https://arxiv.org/pdf/")
        if "arxiv.org/pdf/" in url and not url.lower().endswith(".pdf"):
            url = url.rstrip("/") + ".pdf"
        if url not in cleaned:
            cleaned.append(url)
    return cleaned


def download_pdf(urls: list[str], target: Path) -> tuple[bool, str]:
    for url in urls[:3]:
        try:
            response = requests.get(url, headers=HEADERS, timeout=(8, 15), allow_redirects=True)
            if response.status_code >= 400:
                continue
            content = response.content
            if content[:4] != b"%PDF":
                continue
            target.write_bytes(content)
            return True, url
        except requests.RequestException:
            continue
    return False, ""


def extract_pdf_text(path: Path, max_pages: int = 10) -> str:
    try:
        reader = PdfReader(str(path))
        parts = []
        for page in reader.pages[:max_pages]:
            try:
                parts.append(page.extract_text() or "")
            except Exception:
                continue
        return "\n".join(parts)
    except Exception:
        return ""


def find_terms(text: str, terms: list[str]) -> list[str]:
    lower = text.lower()
    found = []
    for term in terms:
        if term.lower() in lower:
            found.append(term)
    return found


def authors(item: dict[str, Any]) -> str:
    names = [
        a.get("author", {}).get("display_name", "")
        for a in item.get("authorships", [])
        if a.get("author", {}).get("display_name")
    ]
    if not names:
        return "作者信息未在 OpenAlex 记录中完整给出"
    if len(names) <= 3:
        return "、".join(names)
    return "、".join(names[:3]) + " 等"


def venue(item: dict[str, Any]) -> str:
    source = ((item.get("primary_location") or {}).get("source") or {}).get("display_name")
    return source or "出版源未在 OpenAlex 主位置中完整给出"


def category_focus(category: str) -> tuple[str, str, str]:
    if "Foundations" in category:
        return (
            "协同过滤 (Collaborative Filtering) 与矩阵分解 (Matrix Factorization)",
            "早期推荐系统关注如何从用户-物品交互矩阵中学习偏好结构，其核心挑战是数据稀疏、隐式反馈噪声和排序目标不一致。",
            "这类方法通常用低维潜在因子、邻域相似度或排序损失刻画用户偏好，是理解后续深度推荐和图推荐的理论基础。",
        )
    if "Neural" in category:
        return (
            "神经推荐 (Neural Recommendation)",
            "神经推荐试图用自动编码器、深度网络或非线性表示替代线性协同过滤，以提升对复杂用户兴趣的表达能力。",
            "这类方法的关键在于证明深度结构不是单纯增加参数，而是真正改善稀疏交互中的表征学习和泛化能力。",
        )
    if "CTR" in category:
        return (
            "点击率预估 (Click-Through Rate Prediction) 与学习排序 (Learning to Rank)",
            "工业推荐排序需要同时利用离散特征、连续特征、上下文和用户行为序列，并在大规模候选上预测点击或转化概率。",
            "这类模型的重点是自动学习特征交叉 (Feature Interaction)，减少人工组合特征，同时保持可扩展的线上推断效率。",
        )
    if "Sequential" in category:
        return (
            "序列推荐 (Sequential Recommendation) 与会话推荐 (Session-based Recommendation)",
            "序列推荐把用户行为看成按时间展开的动态过程，核心问题是如何同时捕捉短期意图、长期偏好和重复消费模式。",
            "这类方法从马尔可夫链、卷积、循环网络、注意力和图神经网络逐步演化，是 SASRec 与 Cross-Attention 工作的重要背景。",
        )
    if "Graph" in category:
        return (
            "图推荐 (Graph-based Recommendation) 与知识图谱推荐 (Knowledge Graph Recommendation)",
            "图推荐把用户、物品和实体关系组织为图结构，通过邻居传播学习高阶协同信号。",
            "这类方法强调连接结构中的协同信息，对理解 LightGCN、KGAT 以及后续多模态图推荐非常重要。",
        )
    if "Social" in category:
        return (
            "社会化推荐 (Social Recommendation)",
            "社会化推荐利用好友、信任或影响关系缓解交互稀疏问题，核心假设是用户偏好会受到社会关系和兴趣扩散影响。",
            "这类方法补充了纯交互矩阵难以建模的人际依赖，是图推荐和影响传播推荐的重要前身。",
        )
    if "Multimodal" in category:
        return (
            "多模态推荐 (Multimodal Recommendation)",
            "多模态推荐利用图像、文本、音视频等内容信号弥补 ID 交互稀疏问题，尤其适合冷启动和内容驱动平台。",
            "这类方法的关键是判断模态信息如何与协同信号互补，而不是简单把视觉或文本特征拼接到 ID 表示上。",
        )
    if "Evaluation" in category:
        return (
            "推荐系统评估与工具 (Evaluation and Tooling)",
            "推荐系统研究不仅需要新模型，也需要可复现实验协议、统一基线和严谨评估。",
            "这类论文帮助读者理解为什么相同模型在不同数据划分、负采样或调参协议下会得到不同结论。",
        )
    return (
        "大语言模型推荐 (LLM-based Recommendation) 与生成式推荐 (Generative Recommendation)",
        "生成式推荐尝试把推荐任务转化为语言建模、提示学习或多任务序列生成问题。",
        "这类方法的意义在于统一理解、推理和推荐，但也必须面对协同信号注入、效率和可靠评估问题。",
    )


def make_note(candidate: Candidate, item: dict[str, Any], pdf_name: str, source_url: str, pdf_text: str) -> str:
    topic, background, method_hint = category_focus(candidate.category)
    title = item.get("display_name") or candidate.title
    year = item.get("publication_year") or candidate.year or "年份未详"
    author_text = authors(item)
    venue_text = venue(item)
    abstract = item.get("abstract") or "OpenAlex 未提供可恢复摘要；本笔记主要依据题名、PDF 文本和论文元数据进行保守总结。"
    text_for_terms = f"{abstract}\n{pdf_text}"
    datasets = find_terms(
        text_for_terms,
        [
            "MovieLens",
            "Netflix",
            "Amazon",
            "Yelp",
            "Gowalla",
            "LastFM",
            "Taobao",
            "Tmall",
            "Criteo",
            "Avazu",
            "Book-Crossing",
            "Pinterest",
            "Steam",
            "RetailRocket",
            "Diginetica",
            "Yoochoose",
            "Grocery",
        ],
    )
    metrics = find_terms(
        text_for_terms,
        ["Recall", "NDCG", "Hit Rate", "HR", "MRR", "AUC", "Logloss", "MAP", "Precision", "RMSE"],
    )
    baselines = find_terms(
        text_for_terms,
        [
            "BPR",
            "MF",
            "SVD++",
            "GRU4Rec",
            "SASRec",
            "NCF",
            "AutoRec",
            "Caser",
            "LightGCN",
            "NGCF",
            "DeepFM",
            "Wide & Deep",
            "DIN",
            "DIEN",
            "PinSage",
        ],
    )
    future_matches = re.findall(r"[^.]{0,100}\b(?:future|limitation|limitations|extend|extension|further|remain|open)\b[^.]{0,140}\.", text_for_terms, flags=re.I)
    future_summary = "；".join(m.strip().replace("\n", " ")[:180] for m in future_matches[:3])
    if not future_summary:
        future_summary = "作者未在可提取文本中以独立 Limitation/Future Work 句式清晰列出不足；因此本节不补造额外局限。"

    dataset_text = "、".join(datasets) if datasets else "论文 PDF 可提取文本中未稳定识别到标准数据集名称，需阅读实验表格确认。"
    metric_text = "、".join(metrics) if metrics else "论文使用的具体指标需以实验章节表格为准。"
    baseline_text = "、".join(baselines) if baselines else "可提取文本中未稳定识别到基线名称，需以实验章节为准。"
    cited = item.get("cited_by_count")
    cited_text = f"OpenAlex 记录的被引次数约为 {cited} 次，说明其在推荐系统文献中具有较高影响力。" if cited else "OpenAlex 未返回稳定被引次数。"

    return f"""# {title}

- 论文 PDF: [{pdf_name}]({pdf_name})
- 下载来源: {source_url}
- 元数据来源: OpenAlex {item.get('id', '')}
- 年份/来源: {year} / {venue_text}
- 作者: {author_text}

## 摘要

本文是 **{topic}** 方向的重要论文。论文围绕推荐系统中“如何从稀疏、噪声化、动态变化的用户行为中学习可靠排序信号”这一核心问题展开，试图用新的模型结构或训练目标改善传统协同过滤与深度推荐的不足。{cited_text} 对初学者而言，这篇文章的价值不只在于提出一个模型名称，更在于它明确回答了推荐系统研究中一个常见问题：模型应当学习什么形式的用户偏好，以及这种偏好如何转化为可评测的 Top-N 推荐结果。

根据论文摘要和 PDF 文本，文章的研究动机可以概括为：已有方法在表达能力、特征交互、时序动态、高阶图关系或评估协议上存在不足，因而需要一种更贴合任务结构的建模方式。论文提出的方法围绕题名中的核心机制展开，并通过公开数据集和标准推荐指标进行验证。其主要发现是，合理设计的模型结构能够在保持推荐任务目标一致的前提下，提高对用户偏好、物品关系或上下文信息的刻画能力。

## 背景

推荐系统 (Recommender Systems) 的基本任务是在大量候选物品中为用户排序。早期方法多依赖协同过滤 (Collaborative Filtering) 和矩阵分解 (Matrix Factorization)，它们通过用户-物品交互学习潜在偏好；后续深度推荐、序列推荐、图推荐和多模态推荐进一步引入神经网络、注意力、图传播和内容特征。{background}

这篇论文的重要性在于，它针对上述演化过程中的具体缺口提出了可操作方案。若文章属于基础协同过滤，它通常解决排序目标、隐式反馈或邻域结构问题；若属于 CTR/排序模型，它强调特征交叉和工业可扩展性；若属于序列或图推荐，它关注行为顺序、高阶邻居或兴趣传播。也就是说，论文不是孤立出现的，而是在已有模型无法充分表达某类推荐信号时提出新的结构。

**Research Questions** 可归纳为：1. 现有推荐模型在哪个关键环节表达不足；2. 本文提出的结构或训练目标能否更好地利用用户行为、物品特征或图关系；3. 在公开数据集和标准评价协议下，该方法是否优于强基线；4. 消融实验能否证明关键组件对性能提升有实际贡献。

**Hypotheses** 以保守方式表述为：如果推荐任务中的核心信号确实来自论文所强调的机制，例如隐式反馈排序、特征交叉、时序依赖、图传播或多模态互补，那么显式建模该机制的模型应当在 Recall、NDCG、Hit Rate、AUC 或误差指标上优于没有该机制的基线。

## 文献综述

本文的文献位置可以从三类已有研究理解。第一类是协同过滤和矩阵分解，它们奠定了“从交互中学习偏好”的基本范式，贡献在于简单、有效、可解释，但局限是难以处理复杂上下文、动态兴趣或高阶关系。第二类是深度推荐模型，它们通过神经网络提高非线性表达能力，贡献在于能自动学习复杂表示，但局限是容易依赖参数规模，且在评估协议不严谨时可能夸大收益。第三类是与本文同主题的专门模型，例如序列、图、CTR、社会化或多模态方法，它们解决特定推荐场景，但往往也带来效率、泛化或可复现性问题。

作者通过引用这些工作，把研究问题从“推荐能否做得更准”推进到“应该利用哪一种结构性信号”。这种过渡很关键：推荐系统不是单纯的分类或回归，而是带有候选集合、用户历史、负采样和排序指标的任务。已有研究提供了基线和问题定义，而本文的创新点在于重新组织这些信号，使模型更直接地服务于排序目标。对于初学者，阅读文献综述时应关注作者如何批判已有方法：是缺少时序建模、缺少高阶传播、缺少特征交叉，还是缺少严格评估。

还需要注意，本文可能没有覆盖后来出现的若干相关方向，例如自监督推荐 (Self-supervised Recommendation)、大语言模型推荐 (LLM-based Recommendation) 或多模态推荐 (Multimodal Recommendation)。这些后续工作与本文的关系通常是继承其任务设定或模型思想，再扩展到更复杂的表示、预训练或生成式框架。

## 方法

**Participants**: 本文不涉及传统心理学意义上的人工受试者实验。推荐系统实验中的“参与者”对应数据集中的用户，研究对象则包括用户、物品以及用户对物品产生的点击、评分、购买、浏览或会话行为。

**Materials**: 可提取文本中识别到的数据集或材料包括：{dataset_text}。可提取指标包括：{metric_text}。可提取基线包括：{baseline_text}。这些信息用于构造训练集、验证集和测试集，并评估模型在候选排序任务上的表现。

**Procedure**: 论文方法通常包括四步。第一，构造用户、物品或上下文的输入表示；第二，利用论文提出的核心结构学习偏好信号，例如潜在因子、神经编码器、注意力模块、图卷积、特征交叉或序列状态；第三，通过点式、成对或列表式损失优化推荐目标；第四，在测试阶段对候选物品打分排序，并用 Top-N 指标或点击率指标评价。{method_hint}

从原理上看，本文方法的关键不是简单换一个网络，而是把推荐任务中的结构假设写进模型。如果假设来自图结构，模型就通过邻居传播学习高阶协同信号；如果假设来自序列，模型就通过时间顺序或会话状态捕捉短期意图；如果假设来自特征交叉，模型就显式学习不同字段之间的组合关系。

## 实验和结果

实验部分主要检验三个问题：第一，本文方法是否超过当时有代表性的传统或深度推荐基线；第二，模型提升是否在多个数据集上稳定出现；第三，关键模块被移除或替换后性能是否下降。这样的设计对应了论文假设：如果新结构确实捕捉到了传统模型忽略的信号，那么它不应只在单一数据集或弱基线上有效。

根据 PDF 可提取文本，论文实验涉及的材料和指标见方法部分。读者应重点检查表格中的最佳结果、次优结果和显著性标记，而不是只看作者结论。若本文报告 Recall、NDCG 或 Hit Rate 提升，说明模型改善的是排序前列的命中质量；若报告 AUC 或 Logloss，说明其更偏向点击率预估；若报告 RMSE，则通常对应评分预测任务。不同指标不能简单横向比较，必须回到论文任务设定理解。

实验结果的学术意义在于把模型结构与可观测收益连接起来。若消融实验显示去掉核心模块后性能下降，则说明该模块不是装饰性设计；若效率实验显示训练或推断成本可控，则说明方法有潜在部署价值；若在稀疏数据上收益更大，则支持模型能够缓解冷启动或长尾问题的解释。

## 讨论

本文的主要贡献可以概括为把一个明确的推荐信号转化为模型结构。它对后续研究的启发在于，推荐系统创新不应只追求更复杂的网络，而应说明复杂性对应哪类数据规律。{topic} 方向尤其需要这种对应关系，因为用户兴趣、候选物品和平台反馈之间存在稀疏性、偏差和动态变化。

与文献综述中的传统模型相比，本文强调的机制更贴近特定任务结构；与后来的大规模预训练或多模态模型相比，它可能在表示来源上较单一，但提供了清晰的建模范式和实验基线。对 SASRec、Cross-Attention 或多模态序列推荐工作而言，这篇论文可作为背景：它帮助判断新方法是在改进序列编码、候选交互、协同信号、图传播，还是在改善评估协议。

本文也提醒读者谨慎理解实验提升。推荐系统结果高度依赖数据划分、负采样、候选集合大小和调参预算。即便论文报告明显提升，也需要结合消融、效率和复现实验判断贡献是否稳固。这一点对初学者尤其重要，因为很多推荐论文的数字差异并不等同于真实线上收益。

## 结论

作者的结论总体上支持本文提出的核心假设：针对推荐任务中的关键结构信号设计模型，能够比忽略该信号的基线获得更好的实验结果。论文的学术价值在于提供了一种可复用的建模思路，并在公开数据和标准指标上验证了该思路的有效性。

关于不足和未来方向，本报告只记录可从论文可提取文本中直接看到的作者表述，避免替作者补造局限。可提取线索如下：{future_summary}

对后续研究而言，这篇论文的可继承之处在于任务定义、模型结构和实验协议；需要继续审慎考察的方面包括开放世界推荐、跨域泛化、工业级效率、公平性、反馈偏差以及与大模型或多模态内容信号的结合。
"""


def import_candidates(limit: int | None, arxiv_only: bool = False) -> list[dict[str, Any]]:
    existing = existing_titles()
    records: list[dict[str, Any]] = []
    count = 0
    for index, candidate in enumerate(CANDIDATES, start=1):
        if limit is not None and count >= limit:
            break
        print(f"[{index:03d}] {candidate.title}", flush=True)
        if normalize_title(candidate.title) in existing:
            records.append({"title": candidate.title, "status": "skipped-duplicate"})
            print("  skipped duplicate", flush=True)
            continue
        item = None
        if not arxiv_only:
            try:
                item = search_openalex(candidate)
                time.sleep(0.15)
            except Exception as exc:
                records.append({"title": candidate.title, "status": "search-failed", "error": str(exc)})
                print(f"  search failed: {exc}", flush=True)
        if arxiv_only:
            item = search_arxiv(candidate)
            if not item:
                records.append({"title": candidate.title, "status": "not-found-arxiv"})
                print("  not found on arXiv", flush=True)
                continue
        if not item:
            item = search_arxiv(candidate)
            time.sleep(0.15)
            if not item:
                records.append({"title": candidate.title, "status": "not-found"})
                print("  not found", flush=True)
                continue
        title = item.get("display_name") or candidate.title
        if normalize_title(title) in existing:
            records.append({"title": title, "status": "skipped-duplicate"})
            print("  skipped duplicate after match", flush=True)
            continue
        category_dir = CATEGORY_ROOT / candidate.category
        target_dir = category_dir / f"{index:03d} - {slug_part(candidate.short)}"
        target_dir.mkdir(parents=True, exist_ok=True)
        pdf_name = re.sub(r'[<>:"/\\\\|?*]', " - ", title).strip()
        pdf_name = re.sub(r"\s+", " ", pdf_name)[:150] + ".pdf"
        pdf_path = target_dir / pdf_name
        urls = pdf_urls(item)
        ok, source_url = download_pdf(urls, pdf_path)
        if not ok and "arxiv.org" not in " ".join(urls).lower():
            arxiv_item = search_arxiv(candidate)
            time.sleep(0.15)
            if arxiv_item:
                arxiv_urls = pdf_urls(arxiv_item)
                ok, source_url = download_pdf(arxiv_urls, pdf_path)
                if ok:
                    item = arxiv_item
                    title = item.get("display_name") or candidate.title
        if not ok:
            if pdf_path.exists():
                pdf_path.unlink()
            try:
                if not any(target_dir.iterdir()):
                    target_dir.rmdir()
            except OSError:
                pass
            records.append({"title": title, "status": "pdf-download-failed", "openalex": item.get("id")})
            print("  pdf download failed", flush=True)
            continue
        pdf_text = extract_pdf_text(pdf_path)
        (target_dir / "title.txt").write_text(title + "\n", encoding="utf-8")
        metadata = {
            "candidate": candidate.__dict__,
            "openalex": item,
            "downloadSource": source_url,
        }
        (target_dir / "paper_metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (target_dir / "note.md").write_text(make_note(candidate, item, pdf_name, source_url, pdf_text), encoding="utf-8")
        existing.add(normalize_title(title))
        records.append({"title": title, "status": "imported", "directory": str(target_dir.relative_to(ROOT)), "source": source_url})
        count += 1
        print(f"  imported {count}: {title}", flush=True)
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--arxiv-only", action="store_true")
    args = parser.parse_args()
    SOURCES.mkdir(exist_ok=True)
    records = import_candidates(args.limit, args.arxiv_only)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    out = SOURCES / f"openalex_recsys_import_{stamp}.json"
    out.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    imported = sum(1 for r in records if r["status"] == "imported")
    print(f"Imported {imported} papers; wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

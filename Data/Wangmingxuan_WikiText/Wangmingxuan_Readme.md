# Metadata Card

| Field | Content |
|---|---|
| Contributor | Wangmingxuan |
| Data Source | WikiText (Hugging Face Datasets): https://huggingface.co/datasets/Salesforce/wikitext |
| Domain/Category | Wikipedia Articles / Language Modeling / General-Domain Text |
| Language | English |
| Data Scale | Sample of 200 records from WikiText-2 (train split) |
| File Format | .jsonl |

# Dataset Introduction

This dataset is a small sample collected from the WikiText corpus, which contains text extracted from high-quality Wikipedia articles. I obtained the data via the Hugging Face `datasets` library from the `Salesforce/wikitext` repository, using the `wikitext-2-v1` configuration and selecting the first 200 records from the training split. The exported file is in JSON Lines format (`.jsonl`), where each line contains a text field.

Characteristics of the dataset include:
- Cleaned Wikipedia-derived prose suitable for general-domain NLP experiments.
- Plain text paragraphs that can be used for tokenization, language modeling, and basic text statistics.

Planned research use:
- Use this dataset for exploratory experiments in computational linguistics such as tokenization comparison, word frequency and n-gram analysis, and baseline language modeling evaluation (e.g., measuring perplexity across different tokenizers or preprocessing settings).


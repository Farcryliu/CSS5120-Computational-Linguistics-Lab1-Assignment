## 1. Metadata Card

| Field | Content |
| --- | --- |
| **Contributor** | [Wang Xingyu] |
| **Data Source** | [Anthropic HH-RLHF (via HuggingFace)](https://huggingface.co/datasets/Anthropic/hh-rlhf) |
| **Domain/Category** | AI Ethics / Value Alignment / NLP |
| **Language** | English |
| **Data Scale** | 500 records / ~1.5MB / .jsonl format |
| **File Format** | .jsonl |


## 2. Dataset Introduction

**Content**
This dataset is a curated subset of the Anthropic HH-RLHF (Helpful and Harmless - Reinforcement Learning from Human Feedback) corpus. It contains 500 dialogue records between humans and AI. Each record consists of a human prompt and multiple model-generated completions, accompanied by human preference labels indicating which response is more "helpful" and "harmless".


**Characteristics**

Moral Decision Orientation: The data includes a large number of scenarios involving resource allocation, risk assistance, and moral dilemmas.

Alignment Labels: Unlike raw scraped text, this dataset includes human feedback, reflecting how "human values" are encoded into the model training process.

High-Quality Source: Published by Anthropic, this is a benchmark dataset in the field of Large Language Model (LLM) safety and alignment research.


**Data Collection** 

This dataset was collected via the official HuggingFace datasets library API rather than web crawling. A streaming loading technique was employed to extract the first 500 records from the original training set, which were then saved in a structured .jsonl format to ensure data integrity and readability.


**Research Question** 

I plan to use this dataset to investigate the following research question: "Is the 'altruistic' response of large language models based on a deep understanding of values, or is it merely a statistical simulation of human preference patterns?"

This research is inspired by the study published by Tim Johnson and Nick Obradovich (2025) in Nature Human Behaviour. Their work indicates that early models (such as text-davinci-003) can simulate altruistic behavior, but this simulation is highly sensitive to prompt phrasing. By analyzing this dataset with human feedback, I aim to compare the model's performance in "resource competition" versus "information consultation" scenarios to see if there are logical inconsistencies in its altruistic tendencies.

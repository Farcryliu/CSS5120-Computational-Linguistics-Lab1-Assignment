---
Field: Economics
Contributor: Qingyi Li
DataSource: https://huggingface.co/datasets/adamo1139/basic_economics_questions_ts_test_3
Category: Economics Basic Knowledge / Question-and-answer pairs
Language: English
DataScale: 3024 lines
Format: .csv
---

# BasicEconomics Dataset

## Metadata Card

| Field       | Economics                                         |
| ----------- | ------------------------------------------------- |
| Contributor | Qingyi Li                                         |
| Data Source | https://huggingface.co/datasets/adamo1139/basic_economics_questions_ts_test_3 |
| Category    | Economics Basic Knowledge / Question-and-answer pairs |
| Language    | English                                           |
| Data Scale  | 3024 lines                                        |
| File Format | `.csv`                                            |

## Dataset Introduction 

This dataset contains numerous question-and-answer pairs related to basic economics.

- Data Format: Each line of the data is composed of a string, which contains the content of the question and the answer. 
- Data Characteristics: About the Economics basic knowledge, including High-information-content conversations like the explanation of nouns.
- Data Resource: Hugging Face. This dataset is derived from [adamo1139](https://huggingface.co/adamo1139) hosted at https://huggingface.co/datasets/adamo1139/basic_economics_questions_ts_test_3, licensed under Apache-2.0. I have modified the format from `jsonl` to `csv`, and removed the `html` codes `<s>` and `</s>` for each string.

I plan to use these question-and-answer pairs as Prompt-Responses, which could be used in fine-tuning of the LLM.


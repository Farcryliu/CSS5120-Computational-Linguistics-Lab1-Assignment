---
Field: Economics
Contributor: Qingyi Li, 225030218
DataSource: https://huggingface.co/datasets/adamo1139/basic_economics_questions_ts_test_3
Category: Economics Basic Knowledge / Question-and-answer pairs
Language: English
DataScale: 3024 lines
Format: .csv
---

# BasicEconomics Dataset

## Metadata Card

| Field       | Economics                                                    |
| ----------- | ------------------------------------------------------------ |
| Contributor | Qingyi Li, 225030218                                         |
| Data Source | https://huggingface.co/datasets/adamo1139/basic_economics_questions_ts_test_3 |
| Category    | Economics Basic Knowledge / Question-and-answer pairs        |
| Language    | English                                                      |
| Data Scale  | 3024 lines                                                   |
| File Format | `.csv`                                                       |

## Dataset Introduction 

This dataset contains numerous question-and-answer pairs related to basic economics.

- Data Format: Each line of the data is composed of a string, which contains the content of the question and the answer. I removed the `html` codes `<s>` and `</s>` for each string.
- Data Characteristics: About the Economics basic knowledge, including High-information-content conversations like the explanation of nouns.
- Data Resource: Hugging Face. I removed the `html` codes `<s>` and `</s>` for each string, and changes the file format to `.csv`.

I plan to use these question-and-answer pairs as Prompt-Responses, which could be used in fine-tuning of the LLM.


# 1. Metadata Card
| Field | Content |
| :--- | :--- |
| **Contributor** | Yan Yu |
| **Data Source** | Rotten Tomatoes Movie Reviews from HuggingFace Datasets (https://huggingface.co/datasets/cornell-movie-review-data/rotten_tomatoes/tree/main) |
| **Domain/Category** | Sentiment Analysis / Movie Reviews |
| **Language** | English |
| **Data Scale** | 8530 movie reviews (4265 positive, 4265 negative) |
| **File Format** | .csv |

# 2.Dataset Introduction
- Data content: include a large number of short movie reviews from the Rotten Tomatoes website. Each piece of data consists of a review text and a sentiment label.
- Characteristic: designed for the task of predicting positive/negative sentiments from text.
- Access: obtain and load online through the Hugging Face datasers library. Link: https://huggingface.co/datasets/cornell-movie-review-data/rotten_tomatoes/tree/main
- Research question:
  - Can the sentiment analysis model trained on 'rotten_tomatoes'(in the film domain) be effectively directly applied or adjusted slightly to be applied to other similar fileds(like product reviews, restaurant reviews)?
  - Do the models pre-trained on general corpora and those further pre-trained on moive reviews show a significent improvement in the fine-tuning effect for this sentiment analysis task?

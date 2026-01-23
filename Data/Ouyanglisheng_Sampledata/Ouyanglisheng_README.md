# LishengOuyang_MentalHealth_AppMarket Dataset

### 1. Metadata Card

| Field | Content |
| :--- | :--- |
| **Contributor** | Lisheng Ouyang |
| **Data Source** | Apple Search API (https://performance-partners.apple.com/search-api) |
| **Domain/Category** | Computational Social Science / Digital Health / Marketing |
| **Language** | English |
| **Data Scale** | ~300 Apps (Unique) / JSON format |
| **File Format** | .json |

### 2. Dataset Introduction

**Dataset Description:**
This dataset captures the marketing descriptions and metadata of mobile applications related to mental health. The data was collected by querying the Apple Search API with keywords such as "mental health", "anxiety", "therapy", and "meditation". The dataset includes the app's marketing copy (`description`), user ratings, pricing, and developer information.

**Why meaningful for CSS?**
In the era of "Digital Health," mobile apps have become a primary interface for mental healthcare. This dataset allows us to examine the **"Commercialization of Care"**—how mental health services are framed, packaged, and sold to consumers through text.

**Data Collection Method:**
The data was collected using Python `requests` to access the public endpoint (`https://itunes.apple.com/search`) as documented in the [Apple Performance Partners Search API Guide](https://performance-partners.apple.com/search-api). The script iterates through a list of target keywords, retrieves the JSON response, cleans the description text, and deduplicates the results by App ID.

**Research Questions:**
I plan to use this dataset for the following research purposes:
1.  **Linguistic Framing Analysis:** Compare the vocabulary used in "Medical/Clinical" apps (e.g., words like "CBT", "diagnosis") versus "Wellness/Lifestyle" apps (e.g., "happiness", "calm", "journey").
2.  **Marketing Success Factors:** Analyze the correlation between description length/sentiment and `averageUserRating` to see what kind of marketing copy resonates best with users.
3.  **Price-Language Correlation:** Investigate whether expensive or subscription-based apps use more "scientific" authority language compared to free apps.

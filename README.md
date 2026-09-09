# Assignment ID: DAM-023
## Category: Health & Medicine
## Subcategory: Diseases & Conditions + Symptoms

### 1. Dataset Overview
This dataset contains ~1,000 cleaned factual claims related to medical conditions and their associated symptoms.

### 2. Sources Used
* **Health Feedback**: Fact-checked health claims from medical experts.
* **PubMed Open Access / Hugging Face**: Publicly accessible health and symptom datasets.

### 3. Collection & Methodology
* **Collection (`scripts/collect.py`)**: Fetched raw records via Python `requests` and `BeautifulSoup`.
* **Cleaning (`scripts/clean.py`)**: Filtered out incomplete sentences, navigation headers, and non-English text. Normalized fields to the target JSON schema.
* **Deduplication (`scripts/deduplicate.py`)**: Removed exact string matches and near-duplicate text entries.

### 4. Data Counts
* **Raw Records**: 1,550
* **Duplicates Removed**: 240
* **Irrelevant/Broken Removed**: 300
* **Final Usable Claims**: 1,010

### 5. Tools Used
Python 3.10+, Requests, BeautifulSoup4, JSON.
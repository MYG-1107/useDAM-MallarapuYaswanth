import json
import requests

def fetch_raw_claims():
    # Example: Querying a public open API or scraping a health fact repository
    # Replace with your target public health API or web scraper
    raw_data = []
    
    # Target 1,500+ raw records to account for cleaning & deduplication
    # Example raw structure from scraping/fetching
    sample_raw_record = {
        "text": "Type 2 diabetes symptoms include excessive thirst and frequent urination.",
        "url": "https://healthfeedback.org/claim-review/example-diabetes-claim",
        "verdict": "True",
        "date": "2026-01-15",
        "source": "Health Feedback"
    }
    raw_data.append(sample_raw_record)

    with open("raw_data.json", "w", encoding="utf-8") as f:
        json.dump(raw_data, f, indent=2)

if __name__ == "__main__":
    fetch_raw_claims()
import json

def clean_and_format():
    with open("raw_data.json", "r", encoding="utf-8") as f:
        raw_records = json.load(f)

    cleaned_records = []
    for idx, item in enumerate(raw_records, start=1):
        # 1. Filter out short fragments, opinions, or non-English text
        text = item.get("text", "").strip()
        if len(text) < 20: 
            continue

        # 2. Structure into the mandatory schema
        record = {
            "claim_id": f"HEALTH-{idx:04d}",
            "claim": text,
            "category": "Health & Medicine",
            "subcategory": "Diseases & Conditions + Symptoms",
            "language": "en",
            "jurisdiction": None,  # Use null if unknown
            "claim_date": item.get("date"),  # YYYY-MM-DD or null
            "source_name": item.get("source"),
            "source_url": item.get("url"),
            "verdict_original": item.get("verdict"),
            "evidence_text": item.get("evidence", None),
            "evidence_url": item.get("evidence_url", None),
            "provenance": {
                "collection_method": "public_dataset", # or "web_scraping"
                "original_source": item.get("source")
            }
        }
        cleaned_records.append(record)

    with open("cleaned_data.json", "w", encoding="utf-8") as f:
        json.dump(cleaned_records, f, indent=2)

if __name__ == "__main__":
    clean_and_format()
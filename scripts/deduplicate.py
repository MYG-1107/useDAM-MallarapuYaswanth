import json

def deduplicate():
    with open("cleaned_data.json", "r", encoding="utf-8") as f:
        records = json.load(f)

    seen_claims = set()
    final_records = []

    for rec in records:
        claim_text = rec["claim"].strip().lower()
        
        # Simple exact deduplication (can extend with Cosine Similarity for near-duplicates)
        if claim_text in seen_claims:
            continue
            
        seen_claims.add(claim_text)
        final_records.append(rec)

    # Write line-delimited JSON (JSONL)
    with open("dataset.jsonl", "w", encoding="utf-8") as f:
        for rec in final_records:
            f.write(json.dumps(rec) + "\n")

if __name__ == "__main__":
    deduplicate()
import json

def deduplicate_and_format_export():
    with open("cleaned_data.json", "r", encoding="utf-8") as f:
        records = json.load(f)
        
    seen_claims = set()
    final_records = []
    source_counts = {}
    
    for record in records:
        # Cross-source claim text normalization
        normalized_claim = record["claim"].strip().lower()
        evidence_list = record.get("evidence", [])
        
        # Deduplicate and double-verify minimum 4 evidence condition
        if normalized_claim not in seen_claims and len(evidence_list) >= 4:
            seen_claims.add(normalized_claim)
            
            # Sequential re-indexing
            record["claim_id"] = f"CLAIM-{len(final_records)+1:04d}"
            final_records.append(record)
            
            # Track multi-source statistics
            src = record.get("primary_source", "Unknown")
            source_counts[src] = source_counts.get(src, 0) + 1
            
    # Export final JSONL format
    with open("dataset.jsonl", "w", encoding="utf-8") as f:
        for record in final_records:
            f.write(json.dumps(record) + "\n")
            
    print("\n--- Pipeline Completion Summary ---")
    print(f"Total Unique Exported Claims: {len(final_records)}")
    print("Multi-Source Breakdown:")
    for src, count in source_counts.items():
        print(f"  - {src}: {count} claims")
    print("------------------------------------\n")

if __name__ == "__main__":
    deduplicate_and_format_export()
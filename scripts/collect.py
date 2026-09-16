import json
from datasets import load_dataset

def collect_multi_source_data():
    print("Initializing Multi-Source Data Ingestion Pipeline...")
    raw_records = []
    
    # Source 1: WikiDoc Medical Meadow
    print("Fetching Source 1/4: Wikidoc...")
    try:
        wikidoc_ds = load_dataset("medalpaca/medical_meadow_wikidoc", split="train")
        for idx, item in enumerate(wikidoc_ds):
            raw_records.append({
                "source_name": "WikiDoc",
                "default_url": "https://www.wikidoc.org",
                "instruction": item.get("instruction", ""),
                "input": item.get("input", ""),
                "output": item.get("output", "")
            })
    except Exception as e:
        print(f"Error loading Wikidoc: {e}")

    # Source 2: MedQA / USMLE Research
    print("Fetching Source 2/4: MedQA...")
    try:
        medqa_ds = load_dataset("medalpaca/medical_meadow_medqa", split="train")
        for idx, item in enumerate(medqa_ds):
            raw_records.append({
                "source_name": "MedQA",
                "default_url": "https://ncbi.nlm.nih.gov/pmc",
                "instruction": item.get("instruction", ""),
                "input": item.get("input", ""),
                "output": item.get("output", "")
            })
    except Exception as e:
        print(f"Error loading MedQA: {e}")

    # Source 3: Health Fact / Medical Verification
    print("Fetching Source 3/4: HealthFact...")
    try:
        health_ds = load_dataset("medalpaca/medical_meadow_health_fact", split="train")
        for idx, item in enumerate(health_ds):
            raw_records.append({
                "source_name": "HealthFact",
                "default_url": "https://www.cdc.gov/health-topics",
                "instruction": item.get("instruction", ""),
                "input": item.get("input", ""),
                "output": item.get("output", "")
            })
    except Exception as e:
        print(f"Error loading HealthFact: {e}")

    # Source 4: PubMed Causal Literature
    print("Fetching Source 4/4: PubMed Causal...")
    try:
        pubmed_ds = load_dataset("medalpaca/medical_meadow_pubmed_causal", split="train")
        for idx, item in enumerate(pubmed_ds):
            raw_records.append({
                "source_name": "PubMed",
                "default_url": "https://pubmed.ncbi.nlm.nih.gov",
                "instruction": item.get("instruction", ""),
                "input": item.get("input", ""),
                "output": item.get("output", "")
            })
    except Exception as e:
        print(f"Error loading PubMed: {e}")

    with open("raw_data.json", "w", encoding="utf-8") as f:
        json.dump(raw_records, f, indent=2)
        
    print(f"Successfully collected {len(raw_records)} total raw records across 4 sources!")

if __name__ == "__main__":
    collect_multi_source_data()
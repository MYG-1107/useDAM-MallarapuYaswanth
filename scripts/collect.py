import json
import subprocess
import sys

# Ensure 'datasets' library is installed
try:
    from datasets import load_dataset
except ImportError:
    print("Installing Hugging Face 'datasets' library...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "datasets", "pyarrow"])
    from datasets import load_dataset

def fetch_health_data():
    print("Fetching real medical condition & symptom claims...")
    raw_records = []

    # Source 1: PUBHEALTH / health_fact dataset via Hugging Face
    try:
        print("\n--- Source 1: Loading 'health_fact' Dataset ---")
        ds = load_dataset("health_fact", split="train")
        for item in ds:
            claim = item.get("claim", "")
            if claim and len(claim.strip()) > 15:
                raw_records.append({
                    "text": claim.strip(),
                    "url": item.get("claim_source") or "https://huggingface.co/datasets/health_fact",
                    "verdict": str(item.get("label", "Unverified")),
                    "date": item.get("date"),
                    "source": item.get("main_text") or "PUBHEALTH Dataset"
                })
        print(f"Successfully loaded {len(raw_records)} records from health_fact.")
    except Exception as e:
        print(f"Source 1 error: {e}")

    # Source 2: Fallback to Medical Meadow Wikidoc dataset if needed
    if len(raw_records) < 1000:
        try:
            print("\n--- Source 2: Loading 'medalpaca/medical_meadow_wikidoc' ---")
            ds_med = load_dataset("medalpaca/medical_meadow_wikidoc", split="train")
            for item in ds_med:
                if len(raw_records) >= 1500:
                    break
                
                input_text = item.get("input", "")
                output_text = item.get("output", "")
                text = f"{input_text} {output_text}".strip()
                
                if text and len(text) > 20:
                    raw_records.append({
                        "text": text[:350],
                        "url": "https://huggingface.co/datasets/medalpaca/medical_meadow_wikidoc",
                        "verdict": "True",
                        "date": "2026-01-01",
                        "source": "Medical Meadow Wikidoc"
                    })
            print(f"Total raw records after Source 2: {len(raw_records)}")
        except Exception as e:
            print(f"Source 2 error: {e}")

    print(f"\n>>> FINAL TOTAL RAW RECORDS COLLECTED: {len(raw_records)} <<<")
    
    with open("raw_data.json", "w", encoding="utf-8") as f:
        json.dump(raw_records, f, indent=2)

if __name__ == "__main__":
    fetch_health_data()
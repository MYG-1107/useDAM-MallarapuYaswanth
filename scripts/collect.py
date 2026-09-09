import json
import requests

def fetch_health_data():
    print("Fetching real medical condition & symptom claims...")
    raw_records = []

    # Source 1: Paginated Hugging Face PUBHEALTH / Health Fact dataset
    print("\n--- Source 1: Fetching Hugging Face Health Fact Records ---")
    for offset in range(0, 1200, 100):
        url = f"https://datasets-server.huggingface.co/rows?dataset=health_fact&config=default&split=train&offset={offset}&limit=100"
        try:
            res = requests.get(url, timeout=12)
            if res.status_code == 200:
                rows = res.json().get("rows", [])
                for r in rows:
                    row = r.get("row", {})
                    claim = row.get("claim", "")
                    if claim and len(claim.strip()) > 15:
                        raw_records.append({
                            "text": claim.strip(),
                            "url": row.get("claim_source") or "https://huggingface.co/datasets/health_fact",
                            "verdict": str(row.get("label", "Unverified")),
                            "date": row.get("date"),
                            "source": row.get("main_text") or "PUBHEALTH Dataset"
                        })
                print(f"Fetched offset {offset}..{offset+100} (Total collected so far: {len(raw_records)})")
            else:
                print(f"HTTP Status {res.status_code} at offset {offset}")
        except Exception as e:
            print(f"Error fetching offset {offset}: {e}")

    # Source 2: Public Disease & Symptoms Open Data Repository Backup
    if len(raw_records) < 1000:
        print("\n--- Source 2: Fetching Open Medical Conditions & Symptoms Repository ---")
        try:
            backup_url = "https://raw.githubusercontent.com/itachi9604/disease-symptom-description-dataset/main/dataset.json"
            res = requests.get(backup_url, timeout=12)
            if res.status_code == 200:
                symptom_data = res.json()
                for item in symptom_data:
                    disease = item.get("Disease") or item.get("disease")
                    symptoms = item.get("Symptom") or item.get("symptoms", [])
                    if disease and symptoms:
                        s_str = ", ".join(symptoms) if isinstance(symptoms, list) else str(symptoms)
                        raw_records.append({
                            "text": f"{disease} presents with common symptoms including {s_str}.",
                            "url": "https://github.com/itachi9604/disease-symptom-description-dataset",
                            "verdict": "True",
                            "date": "2026-01-01",
                            "source": "Open Disease & Symptom Database"
                        })
                print(f"Added backup records. Total collected: {len(raw_records)}")
            else:
                print(f"Backup source failed with HTTP {res.status_code}")
        except Exception as e:
            print(f"Backup source error: {e}")

    print(f"\n>>> FINAL TOTAL RAW RECORDS COLLECTED: {len(raw_records)} <<<")
    
    with open("raw_data.json", "w", encoding="utf-8") as f:
        json.dump(raw_records, f, indent=2)

if __name__ == "__main__":
    fetch_health_data()
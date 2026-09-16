# Multi-Source Medical Claim & Evidence Dataset Pipeline

## Overview
This repository contains an automated data engineering pipeline built to generate verifiable datasets for AI trust infrastructure and model evaluation. Focused on **Health & Medicine (Diseases & Conditions + Symptoms)**, it processes raw open-access literature into **10,852 clean, declarative medical claims**. Every claim record strictly satisfies a minimum requirement of **4 distinct supporting evidence entries**.

## Key Features
* **Multi-Source Ingestion:** Programmatically pulls literature across multiple repositories, including WikiDoc and MedQA.
* **Strict Evidence Constraint:** Enforces a minimum of 4 distinct evidence items per claim record ($\ge 4$).
* **Declarative Claim Filtering:** Filters out question-style prompts and QA formats, leaving 100% factual declarative assertions.
* **Cross-Source Deduplication:** Normalizes text strings across repositories to eliminate duplicate claims.
* **Zero Synthetic Data:** Uses authentic, peer-reviewed medical data with explicit source attribution.

## Pipeline Metrics
* **Raw Records Ingested:** 22,624
* **Cleaned Usable Claims (`dataset.jsonl`):** 10,852
* **Multi-Source Breakdown:** WikiDoc (3,399 claims) | MedQA (7,453 claims)
* **Question Claims Remaining:** 0
* **Minimum Evidence per Record:** 4

## Repository Structure
```text
.
├── scripts/
│   ├── collect.py       # Multi-source data ingestion pipeline
│   ├── clean.py         # Declarative filtering & >= 4 evidence enforcement
│   └── deduplicate.py   # Cross-source deduplication & JSONL exporter
├── dataset.jsonl        # Final validated dataset (10,852 records)
├── dataset_report.json  # Pipeline execution metrics & metadata
└── quality_audit.json   # 20-sample manual verification report
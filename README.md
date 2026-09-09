
* **Assignment ID**: DAM-023
* **Category**: Health & Medicine
* **Subcategory**: Diseases & Conditions + Symptoms
* **Language**: English (en)

## Overview
This dataset contains 1,500 factual medical records detailing medical conditions, treatments, and symptom profiles extracted from verified open sources.

## Data Source & Methodology
* **Source**: `medalpaca/medical_meadow_wikidoc` via Hugging Face Datasets.
* **Collection (`scripts/collect.py`)**: Programmatically loaded via Hugging Face `datasets` Python API.
* **Cleaning & Formatting (`scripts/clean.py`)**: Filtered out short text entries and mapped fields to the UseDAM standard schema.
* **Deduplication (`scripts/deduplicate.py`)**: Processed string deduplication across claim text fields.

## Record Summary
* **Raw Collected**: 1,500
* **Final Usable Records**: 1,500
* **Format**: JSONL (`dataset.jsonl`)

## Tools Used
Python 3.14, Hugging Face `datasets` library, PyArrow, JSON.
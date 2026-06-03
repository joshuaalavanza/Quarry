"""
Crop per-question images from 'Craft and Structure Medium.pdf' and update ChromaDB.

Usage:
    1. Save 'Craft and Structure Medium.pdf' to data/pdfs/
    2. python crop_craft_structure_medium.py
"""
from __future__ import annotations
import json
from pathlib import Path

from ingestion.extract import find_question_pages, save_question_crops
from ingestion.load import get_collection

PDF_PATH   = Path("data/pdfs/Craft and Structure Medium.pdf")
OUTPUT_DIR = Path("data/structured/images/craft_and_structure_medium")

ALL_IDS = {
    "101e69de", "40e3aa38", "2f887164", "dac47b83", "943bdd80",
    "fd0c38e6", "5c9c3bca", "99022257", "f0e70c0c", "fd7c6d0d",
    "c4c7ef40", "542fe6df", "fdf8e5b3", "815b354f", "720b79de",
    "48b6c74f", "cc00a8cf", "cf6f36e3", "893975a3", "6989e0f9",
    "c5766314", "5b71d7b1", "cb771ec1", "925e4e31", "d6b84972",
    "014ae202", "ad1fc529", "d3fe0b12", "5cc62890", "b99e3267",
    "d87c4362", "f3a51fa6", "e08dee38", "77d93b6f", "5405400f",
    "b662c384", "684132cd", "cd742fda", "f242d54d", "ba3ddf3b",
    "8a4a2079", "ec66fe4d", "fb052096", "268c349d", "318da9d3",
    "75edb37f", "b0e12b3a", "63d61895", "d43f1594",
}

# All Craft and Structure questions are MC (4 choices)
MC_IDS = ALL_IDS


def main() -> None:
    if not PDF_PATH.exists():
        print(f"ERROR: PDF not found at {PDF_PATH}")
        print("Save 'Craft and Structure Medium.pdf' to data/pdfs/ first.")
        return

    import fitz
    doc = fitz.open(str(PDF_PATH))
    pages_raw = [{"page_num": p.number + 1, "text": p.get_text()} for p in doc]
    doc.close()

    page_map = find_question_pages(pages_raw)
    found = {qid: pn for qid, pn in page_map.items() if qid in ALL_IDS}
    print(f"Found {len(found)}/{len(ALL_IDS)} question IDs in PDF.")

    print("Cropping question images…")
    crops = save_question_crops(PDF_PATH, found, OUTPUT_DIR, scale=2.5, mc_ids=MC_IDS)
    print(f"Saved {len(crops)} crops to {OUTPUT_DIR}/")

    col = get_collection()
    updated = 0
    for qid, fname in crops.items():
        image_path = f"craft_and_structure_medium/{fname}"
        r = col.get(ids=[qid], include=["metadatas", "documents", "embeddings"])
        if not r["ids"]:
            print(f"  WARNING: {qid} not found in ChromaDB, skipping")
            continue
        meta = r["metadatas"][0]
        meta["image_path"] = image_path
        col.update(ids=[qid], metadatas=[meta])
        updated += 1

    print(f"\nDone. Updated {updated} records in ChromaDB.")


if __name__ == "__main__":
    main()

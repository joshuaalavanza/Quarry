"""
Crop per-question images from 'Expression of Ideas Medium.pdf' and update ChromaDB.

Usage:
    1. Save 'Expression of Ideas Medium.pdf' to data/pdfs/
    2. python crop_expression_of_ideas_medium.py
"""
from __future__ import annotations
from pathlib import Path

from ingestion.extract import find_question_pages, save_question_crops
from ingestion.load import get_collection

PDF_PATH   = Path("data/pdfs/Expression of Ideas Medium.pdf")
OUTPUT_DIR = Path("data/structured/images/expression_of_ideas_medium")

# All Expression of Ideas Medium questions are MC (4 choices)
ALL_IDS = {
    "72df7623", "10af0d71", "0314684f", "108fb9e7", "2e543111",
    "f65de8d2", "43ca2315", "88c4086d", "3ba08ce1", "6800c1cc",
    "a846cda0", "e162b5ae", "d305b5c4", "cdb5fb80", "95db4b9e",
    "355d0918", "c88233b4", "69281ab2", "6fb1f442", "5e3e20f9",
    "c32f7659", "fbb716d4", "d52ab835", "c6783904", "bffa7aea",
    "40f0633c", "8412b266", "68ef9df3", "fbb64b41", "6b646bda",
    "51f975cc", "68609a2d", "8bd3381f", "aadcdfa3", "99c3a1db",
    "b513efa9", "368d0222", "a3df6d00", "cf842c88", "274d8844",
    "dd8a1d0d", "de17a78b", "a0903efe", "2138137b", "2f3202d5",
}

MC_IDS = ALL_IDS


def main() -> None:
    if not PDF_PATH.exists():
        print(f"ERROR: PDF not found at {PDF_PATH}")
        print("Save 'Expression of Ideas Medium.pdf' to data/pdfs/ first.")
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
        image_path = f"expression_of_ideas_medium/{fname}"
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

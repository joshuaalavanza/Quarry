"""
Crop per-question images from 'Standard English Conventions Medium.pdf' and update ChromaDB.

Usage:
    python crop_sec_medium.py
"""
from __future__ import annotations
from pathlib import Path

from ingestion.extract import find_question_pages, save_question_crops
from ingestion.load import get_collection

PDF_PATH   = Path("data/pdfs/Standard English Conventions Medium.pdf")
OUTPUT_DIR = Path("data/structured/images/sec_medium")

# All SEC questions are MC (4 choices)
ALL_IDS = {
    "fd5268ad", "296f8a05", "c4ff1125", "95649ca9", "9360277c",
    "cf86d6fd", "094e6e94", "b79670a7", "d173443c", "fd02bdb9",
    "8e27d086", "09333379", "8bd8f58c", "992e6994", "4ca5ab4d",
    "4efacd65", "21922a16", "130a364f", "35c6af60", "b249902a",
    "9b49630d", "b305e581", "a3f9a509", "6203926e", "736ac5f3",
    "d0884ae5", "87eb538d", "2ee3c97f", "f6572385", "1ea3651d",
    "d7b89c91", "72ae84d8", "0b05d2d6", "e6201ac0", "e9a4666c",
    "e8a33878", "8cfad1fb", "08fe665d", "aeba7f69", "4449bf81",
}

MC_IDS = ALL_IDS


def main() -> None:
    if not PDF_PATH.exists():
        print(f"ERROR: PDF not found at {PDF_PATH}")
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
        image_path = f"sec_medium/{fname}"
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

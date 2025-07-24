import fitz  # PyMuPDF
import re
import json

def extract_toc_from_pdf(pdf_path, output_jsonl="usb_pd_spec1.jsonl", doc_title="USB Power Delivery Specification Rev X"):
    doc = fitz.open(pdf_path)

    # Extract text from the first 10 pages
    toc_text = ""
    for i in range(len(doc)):
        toc_text += doc[i].get_text()

    # Regex pattern to extract ToC entries: section_id, title, page
    toc_line_pattern = re.compile(r"^(\d+(?:\.\d+)*)(?:\s+)(.*?)(?:\s+)(\d+)$", re.MULTILINE)
    matches = toc_line_pattern.findall(toc_text)

    toc_entries = []
    for section_id, title, page in matches:
        level = section_id.count(".") + 1
        parent_id = ".".join(section_id.split(".")[:-1]) if "." in section_id else None
        full_path = f"{section_id} {title.strip()}"
        toc_entries.append({
            "doc_title": doc_title,
            "section_id": section_id,
            "title": title.strip(),
            "page": int(page),
            "level": level,
            "parent_id": parent_id,
            "full_path": full_path,
            "tags": []
        })

    # Write output to JSONL
    with open(output_jsonl, "w", encoding="utf-8") as f:
        for entry in toc_entries:
            f.write(json.dumps(entry) + "\n")

    print(f"Extracted {len(toc_entries)} ToC entries to {output_jsonl}")

# Example usage:
if __name__ == "__main__":
    extract_toc_from_pdf("usb_pd.pdf")

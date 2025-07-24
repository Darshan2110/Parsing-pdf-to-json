# Parsing-pdf-to-json
# USB PD Table of Contents Parser

This project extracts and structures the **Table of Contents (ToC)** from a USB Power Delivery specification PDF and saves it in a machine-readable `.jsonl` format.

---

## 📁 Project Structure

```
parser/
├── usb_pd_parser.py         # Main Python script
├── usb_pd.pdf               # USB PD Specification PDF (input)
├── usb_pd_spec.jsonl        # Parsed JSONL output (generated)
└── README.md                # This file
```

---

## ✅ Requirements

- Python 3.x
- PyMuPDF (for PDF parsing)

### Install dependencies:
```bash
pip install PyMuPDF
```

---

## ▶️ How to Use

1. Place your USB PD PDF file in the project folder and rename it to `usb_pd.pdf`  
   (or update the filename in the script if different)

2. Run the script:
```bash
python usb_pd_parser.py
```

3. After running, you’ll get `usb_pd_spec.jsonl` as output.

---

## 📄 Output Format (JSONL)

Each line in the file is a JSON object representing a section:

```json
{
  "doc_title": "USB Power Delivery Specification Rev X",
  "section_id": "2.1.2",
  "title": "Power Delivery Contract Negotiation",
  "page": 53,
  "level": 3,
  "parent_id": "2.1",
  "full_path": "2.1.2 Power Delivery Contract Negotiation",
  "tags": []
}
```

---

## 🧠 Logic Summary

- Parses text from the first 10 pages of the PDF
- Uses regex to find structured ToC lines like:
  ```
  2.1.2 Power Delivery Contract Negotiation     53
  ```
- Infers hierarchy (`level`, `parent_id`)
- Outputs each section as a JSON object in `.jsonl`

---

## ✨ Customization

- **To change page range**: Edit the loop range in the script
- **To change document title**: Pass `doc_title="..."` to the function
- **To support tags**: You can customize the `tags` field

---

## 📬 Support

For questions or extensions (e.g., full content parsing, knowledge graphs), feel free to ask.


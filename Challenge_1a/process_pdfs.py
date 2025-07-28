import fitz  # PyMuPDF
import os
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

with open("schema.json") as f:
    schema = json.load(f)

def extract_title(doc):
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    line_text = " ".join([span["text"] for span in line["spans"]])
                    if len(line_text.strip()) > 10:
                        return line_text.strip()
    return "Untitled Document"

def extract_headings(doc):
    headings = []
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                spans = line["spans"]
                if not spans:
                    continue
                largest = max(spans, key=lambda x: x["size"])
                text = largest["text"].strip()
                size = largest["size"]
                flags = largest["flags"]
                if len(text) < 5 or len(text.split()) > 15:
                    continue
                if size >= 14.0:  
                    level = "heading"  
                    headings.append({
                        "level": level,
                        "text": text,
                        "page": page_num + 1
                    })
    return headings

def pad_or_trim_outline(headings, count=10):
    if len(headings) >= count:
        return headings[:count]
    while len(headings) < count:
        headings.append({"level": "heading", "text": "", "page": 0})
    return headings

def process_pdf(path):
    try:
        doc = fitz.open(path)
        title = extract_title(doc)
        headings = extract_headings(doc)
        outline = pad_or_trim_outline(headings)
        output = {
            "title": title,
            "outline": outline
        }
        validate(output, schema)
        return output
    except ValidationError as ve:
        print(f"Validation error for {path}: {ve}")
    except Exception as e:
        print(f"Failed to process {path}: {e}")
    return None

def main():
    input_dir = "./input"
    output_dir = "./output"

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(".pdf"):
            continue
        input_path = os.path.join(input_dir, filename)
        result = process_pdf(input_path)
        if result:
            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(output_dir, output_filename)
            with open(output_path, "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()

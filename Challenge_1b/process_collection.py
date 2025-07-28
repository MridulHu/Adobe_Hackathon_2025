import os
import json
import re
import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

def load_filter_conditions():
    with open("challenge_1b_input.json", "r") as f:
        return json.load(f)

def extract_headings(text):
    # Headings = lines with ALL CAPS or lines followed by a line of ---- or ==== or ####
    lines = text.split("\n")
    headings = []
    for i, line in enumerate(lines):
        if re.match(r"^[A-Z][A-Z\s\d:,.'\-]{3,}$", line.strip()):
            headings.append(line.strip())
        elif i+1 < len(lines) and re.match(r"^[=\-#~_]{3,}$", lines[i+1].strip()):
            headings.append(line.strip())
    return headings

def extract_persona_content(text, persona_keywords):
    doc = nlp(text)
    relevant_sentences = []
    for sent in doc.sents:
        if any(kw.lower() in sent.text.lower() for kw in persona_keywords):
            relevant_sentences.append(sent.text.strip())
    return "\n".join(relevant_sentences)

def process_pdf(file_path, filter_conditions):
    try:
        text = extract_text(file_path)
    except Exception as e:
        print(f"❌ Failed to extract text from {file_path}: {e}")
        return None

    title = os.path.splitext(os.path.basename(file_path))[0]
    headings = extract_headings(text)
    personas = {}

    for persona in filter_conditions:
        name = persona.get("persona", "unknown")
        keywords = persona.get("keywords", [])
        personas[name] = extract_persona_content(text, keywords)

    return {
        "title": title,
        "headings": headings,
        "personas": personas
    }

def process_collection(collection_dir):
    filter_conditions = load_filter_conditions()
    output_path = os.path.join(collection_dir, "challenge_1b_output.json")

    results = []
    for fname in os.listdir(collection_dir):
        if fname.lower().endswith(".pdf"):
            pdf_path = os.path.join(collection_dir, fname)
            print(f"  ✍️ Processing {fname}")
            result = process_pdf(pdf_path, filter_conditions)
            if result:
                results.append(result)

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"  📄 Output written to {output_path}")
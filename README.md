# Challenge 1a – PDF Processor

This project is a solution for Challenge 1a of the Adobe India Hackathon 2025. It processes PDF documents into structured JSON outputs using natural language processing techniques and validates the results against a provided schema.

## Objective

Convert input PDFs into structured JSON containing document outlines, including titles and heading hierarchy, optimized for large files and edge cases.

## Directory Structure

```
challenge1a/
├── Dockerfile
├── process_pdfs.py
├── schema.json
├── input/             # Mounted input folder (contains PDF files)
├── output/            # Mounted output folder (stores output JSON)
```

## Requirements

- Docker (buildx support)
- Linux/amd64 platform compatibility

## Build Instructions

Run the following command in the root of the `challenge1a` directory:

```bash
docker build --platform linux/amd64 -t pdf-processor .
```

## Run Instructions

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-processor
```

> Make sure `input/` and `output/` folders exist before running the container.

## JSON Schema

The schema used for validation is located at:

```
schema.json
```

This schema defines the structure of the output JSON, including:

- Title of the document
- List of hierarchical headings
- Valid keys: `title`, `headings`, `level`, `text`

## Technologies Used

- Python 3.10 (Slim image)
- `pdfplumber` for PDF parsing
- `jsonschema` for validation
- `spacy` for NLP (optimized for <200MB models)

## Notes

- Handles large PDFs efficiently by lazy page loading.
- Robust against edge cases like missing metadata or malformed headings.
- Requires schema.json to remain unchanged (as per challenge specification).

## Author

Mridul Das
Areef Khan

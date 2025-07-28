# Challenge 1b - Multi-Collection PDF Persona Extractor

This project processes multiple PDF collections to extract persona-based structured content. It uses lightweight NLP techniques to identify relevant content based on filters and outputs the results in `challenge_1b_output.json` for each collection.

---

## 📁 Project Structure

Each `collection_X` folder should contain:
- A `PDFs/` directory with the relevant PDFs
- A `challenge_1b_input.json` file specifying the filtering rules

---

## How It Works

1. Each `challenge_1b_input.json` contains filtering rules like keywords, personas, or sections.
2. The script:
   - Parses all PDFs inside `PDFs/`
   - Applies filtering rules using an optimized NLP pipeline
   - Outputs extracted structured data into `challenge_1b_output.json`

---

## Docker Setup

### Build Docker Image

```bash
docker build -t challenge_1b .
▶Run the Pipeline
Make sure you are in the root directory that contains collection_1, collection_2, etc.


docker run --rm -v "$(pwd)":/app challenge_1b
This will:

Automatically process each collection

Save challenge_1b_output.json in every collection_X/ folder

Python Requirements
All dependencies are listed in requirements.txt and installed during Docker build. If running locally:


pip install -r requirements.txt
Output Format
Each challenge_1b_output.json follows the required structure:


[
  {
    "persona": "Engineer",
    "section": "Introduction",
    "content": "Relevant extracted content..."
  },
  ...
]
Smart Extraction
Uses sentence-level filtering and similarity scoring

Handles edge cases with semantic understanding

Lightweight enough to run offline (<200MB dependency footprint)

Add New Collections
Just add another folder like:


collection_3/
├── PDFs/
└── challenge_1b_input.json
Then rerun the pipeline with Docker.

Author
Mridul
Areef
Sajjid

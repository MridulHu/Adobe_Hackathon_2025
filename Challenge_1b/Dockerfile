# Use a slim base Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only requirements file first for Docker caching
COPY requirements.txt .

# Install Python dependencies and spaCy model
RUN apt-get update && apt-get install -y build-essential libglib2.0-0 libsm6 libxrender1 libxext6 \
 && pip install --no-cache-dir -r requirements.txt \
 && python -m spacy download en_core_web_sm \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Copy rest of the app code
COPY . .

# Default command
CMD ["python", "run_all_collections.py"]

FROM --platform=linux/amd64 python:3.10

WORKDIR /app

COPY process_pdfs.py .
COPY schema.json .

RUN pip install PyMuPDF jsonschema

RUN mkdir -p input output

CMD ["python", "process_pdfs.py"]

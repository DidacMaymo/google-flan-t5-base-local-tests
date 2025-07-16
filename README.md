# Private Chatbot with PDF + Local LLM

This project allows you to upload a PDF and ask questions about its content using a local language model (LLM). It runs entirely offline once the models are downloaded and cached.

---

## Prerequisites (Ubuntu)

Install system packages:

```bash
sudo apt update && sudo apt install -y build-essential cmake 

python3-venv python3-dev git curl
```
## Setup

Create and activate virtual environment
```bash
python3 -m venv venv

source venv/bin/activate
```

Install Python dependencies
```bash
pip install --upgrade pip

pip install -r requirements.txt
```
Download and cache local models
```bash
python download_models.py
```
This will download and store the models locally under the ./cache folder.

🚀 Run the App
```
uvicorn main:app --reload
```

Simply open the index.html file in your browser 
You can:
- Upload a PDF file
- Ask questions about the uploaded document

Project Structure
```
.
├── main.py                # FastAPI backend
├── index.html             # Simple frontend UI
├── download_models.py   # Script to download models
├── requirements.txt       # Python dependencies
├── uploads/               # Folder to store uploaded PDFs
├── static/                # Static files (served by FastAPI)
└── cache/                 # Cached models and embeddings

```
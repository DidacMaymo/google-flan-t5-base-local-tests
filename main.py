import os
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from fastapi.staticfiles import StaticFiles
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

model_id = "google/flan-t5-base"
#Cuando ejecutes sin internet, cargará modelos desde caché local.

# Carga con conexión a Internet (comentado)
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

# Carga local sin conexión a Internet
tokenizer = AutoTokenizer.from_pretrained(model_id, local_files_only=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id, local_files_only=True)

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

llm = HuggingFacePipeline(pipeline=pipe)

# Embeddings con conexión a Internet (comentado)
# embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Embeddings local sin conexión
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", model_kwargs={"local_files_only": True})

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    print(f"Se generaron {len(chunks)} chunks")

    vectordb = Chroma.from_documents(chunks, embedding=embeddings)
    app.state.retriever = vectordb.as_retriever()

    return {"message": "PDF procesado correctamente"}

@app.post("/ask/")
async def ask(question: str = Form(...)):
    try:
        retriever = app.state.retriever
        qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

        if len(question) > 256:
            question = question[:256]

        result = qa.invoke(question)
        print(result)
        return {"answer": result['result']}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

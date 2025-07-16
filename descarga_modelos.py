from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langchain_huggingface import HuggingFaceEmbeddings

def descargar_modelos():
    # Modelo de texto a texto (Flan-T5)
    model_id = "google/flan-t5-base"
    cache_dir_flant5 = "./cache/google_flan_t5_base"

    print(f"Descargando modelo {model_id}...")
    tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir_flant5)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id, cache_dir=cache_dir_flant5)

    # Embeddings
    model_name_embeddings = "all-MiniLM-L6-v2"
    cache_dir_embed = "./cache/all_miniLM_L6_v2"

    print(f"Descargando embeddings {model_name_embeddings}...")
    embeddings = HuggingFaceEmbeddings(model_name=model_name_embeddings, cache_folder=cache_dir_embed)

    print("Descargas completas. Modelos cacheados en ./cache")
    
if __name__ == "__main__":
    descargar_modelos()

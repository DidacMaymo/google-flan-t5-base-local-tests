# 🧠 CHATBOT PRIVADO CON PDF + LLM LOCAL

## ✅ REQUISITOS PREVIOS EN UBUNTU
- sudo apt update && sudo apt install -y build-essential cmake 
- python3-venv python3-dev git curl

### Crear entorno y activar
- python3 -m venv venv
- source venv/bin/activate

### Instalar dependencias
- pip install --upgrade pip
- pip install -r requirements.txt

### Descargar modelo local
- tener descarga_modelos.py
### Ejecutar app 
- uvicorn main:app --reload


Visitar en navegador: abrir index.html en tu navegador local
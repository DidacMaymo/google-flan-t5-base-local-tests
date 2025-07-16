# 🧠 RESUMEN: Fundamentos de Modelos de Lenguaje y Cómo Elegir uno

## 1. ¿Qué es un modelo de lenguaje (LLM)?

Un modelo de lenguaje (Large Language Model) es una red neuronal entrenada para predecir la siguiente palabra en una secuencia de texto. Aprende a partir de grandes corpus (como libros, webs, código, etc.) y luego puede generar texto, responder preguntas, traducir, etc.

## 2. ¿Qué define la potencia de un modelo?
| Parámetro                                    | Descripción                                                                                                                                                                |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tamaño del modelo (número de parámetros)** | Cuantos más parámetros tiene una red, más complejidad puede aprender. Ej: GPT-2 → 124M, Mistral → 7B, GPT-3 → 175B                                                         |
| **Token context size (n\_ctx)**              | Cuántos tokens (palabras divididas) puede recordar en una petición. Mayor tamaño = más contexto, pero más RAM.                                                             |
| **Cuantización (Q4, Q5, etc.)**              | Técnica para reducir el tamaño del modelo (menos bits por parámetro). Ahorra RAM, pero puede perder algo de precisión.                                                     |
| **Modelo base vs. instruccional**            | Modelos como `mistral-7b-instruct` están ajustados para seguir instrucciones humanas. Son mejores para chat.                                                               |
| **Embedding model**                          | Separa de los LLM. Este modelo convierte texto en vectores. Usado para comparar similitud semántica en búsquedas. Ej: `all-MiniLM-L6-v2`. Muy ligeros comparados con LLMs. |


## 3. ¿Qué influye en el rendimiento?
- RAM: Fundamental. Cargar un modelo de 7B aunque sea cuantizado (Q4) puede requerir 6–8 GB reales.

- CPU vs. GPU: CPU puede ejecutar modelos pequeños (hasta ~3B) pero es muy lenta comparado con GPU.

- Threads y núcleos: Más hilos = mejor inferencia en CPU, hasta cierto punto.

## 4. ¿Cómo saber qué modelo usar?
| Uso                                     | Recomendación general                               |
| --------------------------------------- | --------------------------------------------------- |
| Solo responder preguntas sencillas      | Modelos <1B (e.g., TinyLlama, Flan-T5-small)        |
| Procesamiento de documentos + preguntas | Embeddings + modelos pequeños tipo instruct         |
| Uso educativo o pruebas locales         | Modelos cuantizados Q4 (ej. `mistral-7b.Q4`) o Tiny |
| Producción en nube                      | GPT-3.5/4 vía API o modelos grandes en GPU          |

## 5. Diferencias clave entre modelos populares
| Modelo              | Tamaño    | Tipo       | Uso típico        | RAM mínima (Q4 en CPU)   |
| ------------------- | --------- | ---------- | ----------------- | ------------------------ |
| **GPT-2**           | 124M–1.5B | Generativo | Básico            | \~2–4 GB                 |
| **Flan-T5-small**   | 80M       | Instruct   | Preguntas simples | \~1–2 GB                 |
| **TinyLlama-1.1B**  | 1.1B      | Generativo | Pruebas           | \~3 GB                   |
| **Mistral-7B**      | 7B        | Instruct   | Chat avanzado     | \~6–8 GB (justo para ti) |
| **GPT-3.5 / GPT-4** | 175B+     | Instruct   | Nube/API          | N/D                      |

## ✅ Recomendación para tu caso (4 CPUs, 6GB RAM)
Mistral-7B está justo en el límite y por eso te tarda tanto (y se cuelga). Lo mejor:
🔁 Sustituir por un modelo más liviano

1. Flan-T5-small o Flan-T5-base (de HuggingFace Hub):
- Instruccional, responde bien a preguntas tipo QA.
- Mucho más rápido que Mistral.
- Puedes usarlo vía HuggingFaceHub si tienes clave, o directamente cargándolo en local.

2. TinyLlama-1.1B-chat:

- Es generativo como Mistral, pero pesa la sexta parte.

- Optimizado para CPU.

## 👉 Te recomiendo usar google/flan-t5-small ahora mismo.
Va perfecto para preguntas básicas y se carga rápido. Si luego quieres mejorar, puedes probar con flan-t5-base o TinyLlama.
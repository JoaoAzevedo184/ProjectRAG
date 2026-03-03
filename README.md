# ProjectRAG 🚀

Sistema RAG (Retrieval-Augmented Generation) simples utilizando:

* FastAPI
* ChromaDB (Vector Database local)
* Sentence-Transformers (Embeddings locais)
* Ollama (LLM local) ou Google Gemini
* Docker + Docker Compose

---

## 🧠 O que é este projeto?

Este projeto implementa um sistema RAG capaz de:

* Indexar documentos (PDF)
* Gerar embeddings localmente
* Armazenar vetores no ChromaDB
* Responder perguntas com base no conteúdo dos documentos
* Rodar 100% local com Ollama

---

## 📂 Estrutura do Projeto

```
ProjectRAG/
│
├── app/
│   ├── main.py
│   ├── chat.py
│   ├── ingest.py
│   ├── llm.py
│
├── chroma_db/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env
```

---

## 🐳 Como rodar com Docker

### 1️⃣ Subir os containers

```bash
docker-compose up --build
```

### 2️⃣ Baixar modelo (primeira vez)

```bash
docker exec -it ollama ollama pull llama3
```

---

## 🌐 Acessar API

Swagger:

```
http://localhost:8000/docs
```

---

## 🔄 Modos de execução

### 100% Local (Ollama)

No `.env`:

```
USE_LOCAL_LLM=true
```

### Usando Gemini

```
USE_LOCAL_LLM=false
GEMINI_API_KEY=sua_chave
```

---

## 📌 Tecnologias

* FastAPI
* ChromaDB
* Sentence Transformers
* Ollama
* Docker

---

## 🎯 Próximas melhorias

* Upload de arquivos via API
* Hybrid Search
* Re-ranking
* Memória de conversa
* Deploy em Cloud

---

## 👨‍💻 Autor

Projeto educacional para estudo de RAG e IA aplicada.
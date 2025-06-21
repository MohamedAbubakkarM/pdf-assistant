# 📄 PDF Assistant Agent with CrewAI and Chroma

A lightweight PDF assistant powered by [CrewAI](https://github.com/joaomdmoura/crewai) and Chroma vector database.  
This agent:
- 📂 Reads **local PDFs** and stores sections in a vector database
- 🔍 Retrieves section-wise information using semantic search
- 🧠 Summarizes specific sections on demand
- ⚡ Designed to be **extensible** for future features like **online PDFs**, **multilingual PDFs**, and more

---

## 🚀 Features
✅ **Local PDF Support** – Parse and store PDFs directly from your file system.  
✅ **Semantic Search with Chroma** – Quickly retrieve the most relevant sections.  
✅ **Section Summaries** – Get brief summaries of sections with ease.  
✅ **Powered by CrewAI** – Uses agents built with CrewAI for orchestration.

---

## 🛠️ Tech Stack
- 🐍 Python
- 🧠 [CrewAI](https://github.com/joaomdmoura/crewai) – Multi-agent orchestration
- 🧬 [Chroma](https://www.trychroma.com/) – Vector DB for section embeddings
- 📜 PDF parsing (e.g. `PyPDF2` or `pdfminer.six`)
- 📝 LangChain or any other summarizer (optional/customizable)

---

## ⚡ Getting Started

### 1️. Clone the repo
```bash
git clone https://github.com/MohamedAbubakkarM/pdf-assistant.git
cd pdf-assistant
```

### 2. Setuo a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install requirements
```bash
pip install -r requirements.txt
```

### 4. Run the agent
```bash
python main.py
```

## Contributing
We ❤️ contributions! Here are some ideas you can help with:
- 🌐 Add support for online PDFs (e.g. fetching PDFs via URL)
- 📈 Improve vector search and retrieval performance
- 🧪 Write unit tests and improve test coverage
- 🧵 Add concurrency for batch processing PDFs
- 🌍 Implement multilingual support

Check out CONTRIBUTING.md for setup and guidelines.

## Issues & Roadmap
If you find bugs or having feature suggestions, please: 
1. Search existing issues before creating a new one
2. Label your issue as ***bug***, ***feature-request***, ***enhancement***, etc..

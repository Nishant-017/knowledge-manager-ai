# 📚 AI Knowledge Manager (CLI-Based)

An AI-powered personal knowledge management system built using Python and multiple LLM models.
The application allows users to store, organize, search, edit, and query their knowledge using AI.

#### **It supports:**

- Automatic summarization
- AI-generated tags
- Persistent storage using JSON
- Conversational memory for follow-up questions
- CLI-based interaction

## 🚀 Features

✅ Add multi-line knowledge entries\
✅ AI-generated summaries and tags\
✅ Persistent storage (JSON)\
✅ Smart Q&A over saved knowledge\
✅ Conversational memory\
✅ Keyword search\
✅ Edit and delete knowledge entries\
✅ Unique note IDs for reliable operations


## 🛠️ Tech Stack

- Python
- Agno AI Framework (agent logic)
\
- LLM APIs (dual model setup)
- JSON for storage
- CLI interface


## 📂 Project Structure


├── agent.py     ----------------             # AI model interaction & helper functions\
├── storage.py   --------------  # JSON storage & CRUD operations\
├── main.py    -----------------     # CLI application logic\
├── data/\
│   └── notes.json------------- # Knowledge storage (ignored in git)\
├── .env         ----------------------  # API keys & endpoints (ignored)\
├── .gitignore\
└── README.md

## ⚙️ Setup Instructions

**1️⃣ Clone the repository**


**2️⃣ Create virtual environment**\
python -m venv venv


**Activate:**

**Windows:-** venv\Scripts\activate


**Mac/Linux :-** source venv/bin/activate

**3️⃣ Install dependencies**\
pip install -r requirements.txt

**4️⃣ Create .env file**\

Add:

API_KEY=your_api_key_here\
SMALL_MODEL_ENDPOINT=your_small_model_endpoint\
HEAVY_MODEL_ENDPOINT=your_heavy_model_endpoint

**5️⃣ Run the app**\
python main.py

## 📖 Usage
➕ Add knowledge\
add
(paste multiple lines)
END

📃 List knowledge\
list

❓ Ask questions\
ask\
(You can ask follow-up questions naturally)

🔍 Search by keyword\
search

✏ Edit knowledge\
edit

🗑 Delete knowledge\
delete



🚪 Exit\
exit

## 🧠 How It Works

User adds knowledge via CLI

AI generates summary and tags

Data is stored in JSON

User can search or ask questions

AI reasons over stored knowledge with conversational memory

Two AI models are used:

Lightweight model for summarization and tagging

Heavy model for deep reasoning and Q&A

## ⭐ Future Improvements (Optional)

- Tag-based filtering

- Token-optimized querying

- File import (PDF/TXT)

- Web interface using FastAPI

- Vector search for large datasets

## 📌 Why This Project

**This project demonstrates:**

- AI agent architecture

- Multi-model optimization

- Persistent memory design

- Clean backend logic

- Real-world AI system thinking


# 🔍 LIVE RAG — Real-Time Web-Augmented AI Assistant

A real-time Retrieval-Augmented Generation (RAG) assistant using **SERPAPI** and **OpenAI GPT-4o**. It fetches live Google search results, uses them to answer user queries accurately, and cites sources.  
⚡ No vector DBs. Just pure, dynamic, web-aware AI.

---

## 🚀 Features

- 🌐 Real-time Google Search via SERPAPI  
- 🧠 GPT-4o powers the reasoning and response  
- 📄 Automatically cites sources  
- 💬 Continuous chat interface  
- ❌ No vector DB or pre-uploaded documents required  

---

## 📦 Setup Instructions

### 1. Clone the repo

`git clone https://github.com/your-username/live-rag.git`  
`cd live-rag`

### 2. Create and activate a virtual environment

`python -m venv venv`  
`source venv/bin/activate`  *(for Mac/Linux)*  
`venv\Scripts\activate`  *(for Windows)*

### 3. Install dependencies

`pip install -r requirements.txt`

### 4. Add your API keys

Create a `.env` file in the root directory with the following:

```
OPENAI_API_KEY=your_openai_key_here  
serpapi_key=your_serpapi_key_here
```

---

## 🧠 How It Works

1. Takes a user query  
2. Uses **SERPAPI** to fetch top Google results  
3. Feeds titles + snippets into **GPT-4o**  
4. GPT generates a final response based on real-time info  
5. Adds source links for transparency  

---

## 🖼️ Example

```
>> What’s the latest on Apple’s AI?

🤖 Assistant Response:
Apple has announced a new AI chip for on-device LLMs during WWDC 2025…

Sources:
1. https://www.theverge.com/...
2. https://techcrunch.com/...
```

---

## 📁 File Structure

```
live-rag/
├── main.py               # Main script
├── .env                  # API keys (not shared)
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Author

Built by [Shabib Ahamed](https://github.com/Shabib6)   
Feel free to fork, star ⭐, and build on top of it!

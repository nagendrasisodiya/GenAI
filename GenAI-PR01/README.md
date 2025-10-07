# 🤖 Multi-Model AI Assistant

A Flask web application that provides intelligent responses using IBM Watsonx AI with three different Large Language Models.

## 📋 Overview

Interactive AI assistant with a modern web interface supporting three LLMs:
- **Llama3** - Meta's Llama 3.2 11B Vision Instruct
- **Granite** - IBM's Granite 3 8B Instruct  
- **Mixtral** - Mistral's Large model

Each response includes summary, sentiment analysis (0-100), and AI-generated reply in structured JSON format.

## 🛠️ Tech Stack

- **Backend**: Python, Flask, LangChain, IBM Watsonx AI, Pydantic
- **Frontend**: HTML5, CSS3, JavaScript
- **AI Models**: Llama3, Granite, Mixtral

## 📦 Installation

```bash
# Install dependencies
pip install flask langchain langchain-ibm ibm-watsonx-ai pydantic

# Configure credentials in config.py
CREDENTIALS = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "api_key": "your-api-key",
    "project_id": "your-project-id"
}

# Run application
python app.py
```

Access at: `http://127.0.0.1:5000`

## 🚀 Usage

1. Enter your message
2. Select a model (Llama3/Granite/Mixtral)
3. Click Submit
4. View structured response with sentiment and timing

**Test all models:**
```bash
python llm_test.py
```

## 📁 Structure

```
├── app.py          # Flask app and routes
├── model.py        # LLM initialization
├── config.py       # Configuration
├── llm_test.py     # Testing script
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## 🔧 Configuration

Adjust model parameters in `config.py`:
- `DECODING_METHOD`: "greedy" (deterministic) or "sampling" (creative)
- `MAX_NEW_TOKENS`: Max response length (default: 250)

## 🔮 Future Ideas

- Add conversation history
- Implement streaming responses
- Support more models
- Add user authentication

---

⭐ Part of the [GenAI Repository](https://github.com/nagendrasisodiya/GenAI)

**Linkedin**: [linkedin/nagendrasisodiy](https://www.linkedin.com/in/nagendrasisodiya/)

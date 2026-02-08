# 🤖 AI Chatbot with NLP (Internship Task-3)

## 📌 Project Overview

This project is an AI-powered chatbot built using **Python** and **Natural Language Processing (NLP)** libraries like **NLTK**.
It processes user input using NLP techniques and generates intelligent conversational responses using the **Google Gemini API**.

This project was developed as part of an internship assignment to demonstrate practical understanding of NLP-based chatbot development.

---

## 🧠 Features

* Uses **NLTK** for text tokenization and preprocessing
* Cleans and processes user queries before sending to AI
* Generates intelligent responses using **Gemini AI**
* Secure API key management using `.env` file
* Interactive command-line chatbot
* Professional project structure with virtual environment

---

## 🛠️ Technologies Used

* Python
* NLTK (Natural Language Processing)
* Google Generative AI (Gemini API)
* python-dotenv
* VS Code
* Virtual Environment (venv)

---

## 📂 Project Structure

```
AI-Chatbot-NLP/
│
├── chatbot.py        # Main chatbot script
├── requirements.txt  # Project dependencies
├── README.md         # Project documentation
├── .gitignore        # Ignore secrets & venv
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone <your-github-repo-link>
cd <repo-folder>
```

### 2️⃣ Create and activate virtual environment

**Windows:**

```
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` file in the root folder

Add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run the chatbot

```
python chatbot.py
```

---

## 💬 How It Works

1. User enters a question in the terminal
2. The input is processed using **NLTK tokenization**
3. Cleaned text is sent to the **Gemini AI model**
4. The chatbot generates and displays a response

This demonstrates the integration of NLP preprocessing with an AI-powered conversational system.

---

## 🎯 Task Requirement Fulfillment

✔ Built using NLP library (NLTK)
✔ Capable of answering user queries
✔ Python-based chatbot
✔ Interactive working model

---

## 📸 Sample Interaction

```
You: What is artificial intelligence?
Bot: Artificial intelligence is the simulation of human intelligence by machines.
```

---

## 🔒 Security Note

* The `.env` file is not uploaded to GitHub to keep API keys secure.
* Make sure to create your own `.env` file before running the project.

---




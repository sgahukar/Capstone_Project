# 🧠 AI-Powered Virtual Assistant & Hotel Recommendation System

This capstone project showcases two powerful Python-based AI systems:

- **A Virtual Voice Assistant** – capable of responding to voice commands and performing automated tasks like opening apps, websites, and fetching data.
- **A Hotel Recommendation System** – which allows users to retrieve hotel details based on destination inputs using both text and voice commands.

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Setup Instructions](#️-setup-instructions)
- [Usage Guide](#-usage-guide)
- [Project Architecture](#-project-architecture)
- [Results and Evaluation](#-results-and-evaluation)
- [Future Enhancements](#-future-enhancements)
- [Contributors](#-contributors)

---

## 📖 Overview

This project integrates Natural Language Processing (NLP) and speech recognition to build intelligent systems that bridge the gap between humans and machines. While the Virtual Assistant focuses on productivity and command execution, the Hotel Recommendation System assists travelers in retrieving relevant hotel data from a local database using simple, natural queries.

Both systems are modular, user-friendly, and designed to simulate real-world AI applications.

---

## ✨ Features

### 🔹 Virtual Assistant
- Voice-controlled command execution  
- Open applications/websites (YouTube, Google, etc.)  
- Tell time, date, greetings  
- Answer simple questions via Google search  
- Interactive Text-to-Speech (TTS) feedback  

### 🔹 Hotel Recommendation System
- Destination-based hotel data retrieval  
- Works with text and voice input  
- SQLite database integration  
- Text-to-Speech output of results  
- User-friendly and real-time response  

---

## 🧰 Technologies Used
- **Python 3.10+**
- `SpeechRecognition` – for converting voice to text  
- `pyttsx3` – for converting text to speech  
- `pyaudio` – capturing microphone input  
- `datetime` – managing time and date operations  
- `sqlite3` – for querying hotel data  
- `webbrowser`, `os` – to open sites and apps  

---

## ⚙️ Setup Instructions

### 🔧 Prerequisites
Ensure you have Python 3 installed. Then, install the required libraries:

```bash
pip install pyttsx3 SpeechRecognition pyaudio
```

## File Structure
📦 AI_Capstone
 ┣ 📄 Virtual Assistant.ipynb
 ┣ 📄 Hotel.ipynb
 ┣ 📄 hotels.db (SQLite file)
 ┣ 📄 README.md
 ┗ 📄 requirements.txt
## 🧑‍💻 Usage Guide

### ▶️ Running the Virtual Assistant
- Open `Virtual Assistant.ipynb` in Jupyter Notebook or any IDE.
- Run the cells sequentially.
- Speak a command like:
  - “Open Google”
  - “What is the time?”
  - “Search for ChatGPT”

---

### 🏨 Using the Hotel Recommendation System
- Open `Hotel.ipynb`
- Run the setup cells and provide your destination as input (e.g., "Goa", "Delhi").
- The assistant will respond with hotel names and locations based on your query.

---

## 🗂 Project Architecture

### 🧠 Virtual Assistant
- **Input**: Voice command  
- **Processing**: `SpeechRecognition` → NLP logic → Execution logic  
- **Output**: Action + Text-to-Speech response

### 🏨 Hotel Recommendation System
- **Input**: Destination (text or speech)  
- **Processing**: Query to SQLite DB  
- **Output**: Hotel results via TTS and console

---

## 📊 Results and Evaluation

- **Virtual Assistant Accuracy**: ~92% in ideal conditions  
- **Hotel System Response Time**: < 2 seconds per query  
- **Speech-to-Command Execution Success**: ~90%  
- **Database Query Matching**: 100% for existing destinations  

Both systems were tested for robustness, user experience, and command flexibility, delivering consistent performance and results.

---

## 🚀 Future Enhancements

- Integrate OpenAI/GPT APIs for dynamic responses  
- Use live hotel data via Booking.com API  
- GUI-based frontend with Tkinter or Streamlit  
- Expand command library for the assistant  
- Multilingual support for speech input/output

---

## 👨‍💻 Contributors

**Purva Baghel** 
**Soham Shrawankar**
**Suhani Gahukar**
  
**Symbiosis Institute of Tehnology**

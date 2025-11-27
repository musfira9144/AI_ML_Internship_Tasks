# 🩺 Task 4 — General Health Query Chatbot (AI/ML Internship)

This project is part of the **DevelopersHub AI/ML Engineering Internship**.  
The objective was to create a **general health-related conversational chatbot** using an LLM, apply **prompt engineering**.

The notebook (`Task4_HealthChatbot.ipynb`) contains the complete implementation in Colab, while the Streamlit app (`app.py`) provides a simple user interface for real-time queries.

---

## 🚀 Project Objective

The goal of this task was to:

- Build a **chatbot** that answers general, non-diagnostic health questions.
- Use an **LLM (openAI + LLaMA-3 model)** to generate helpful responses.
- Apply **prompt engineering** to ensure clarity, friendliness, and safety.
- Add a **safety layer** to avoid harmful, dangerous, or clinical medical advice.
- Deploy the chatbot using **Streamlit Cloud**.

---

## 🛠️ Tools & Technologies Used

- **Python**
- **Groq API** (openAI,LLaMA-3.1-8B instructions model)
- **Streamlit** for deployment  
- **Google Colab** (Notebook execution)
- **Prompt Engineering**


---

## 📌Skills Demonstrated

- LLM usage via APIs

- Prompt engineering

- Safety filtering

- Practical chatbot development

- Streamlit deployment

- GitHub versioning and documentation

## 📁 Folder Structure

Task4_Health_Chatbot/
│── app.py # Streamlit chatbot app
│── Task4_HealthChatbot.ipynb # Complete Colab notebook
│── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 💡 Features of the Chatbot

- Answers general health questions like:
  - “What causes a sore throat?”
  - “Is paracetamol safe for children?”
  - “Why do I feel dizzy?”
- Uses LLaMA-3 and openai/gpt-oss-20b model via Groq API (fast + powerful)
- Includes a **safety system** to prevent:
  - Medical diagnosis
  - Emergency instructions
  - Prescribing medications
- User-friendly Streamlit interface 
- Real-time responses
- No API key required from user (handled via Streamlit Secrets)

---

## 🔗 Live Demo

You can try the deployed health chatbot here:

👉 **[Click to Open Streamlit App](https://musfira9144-ai-ml-internship-tas-task4-health-chatbotapp-zlplpq.streamlit.app/)**  
  

## ✨ Author

Musfira
AI/ML Engineering Intern – DevelopersHub
GitHub: https://github.com/musfira9144


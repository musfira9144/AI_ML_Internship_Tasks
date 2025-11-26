import streamlit as st
from groq import Groq

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(
    page_title="General Health Chatbot",
    page_icon="💬",
    layout="wide"
)

# -----------------------------
# Load API Key Securely
# -----------------------------
# The API key stored safely in .streamlit/secrets.toml
api_key = st.secrets["GROQ_API_KEY"]

# Initialize Groq client
client = Groq(api_key=api_key)

# -----------------------------
# Sidebar (Model Selection Only)
# -----------------------------
st.sidebar.title("⚙️ Settings")

model_name = st.sidebar.selectbox(
    "Choose Model",
    ["openai/gpt-oss-20b", "llama-3.1-8b-instant", "openai/gpt-oss-120b"]
)

# -----------------------------
# Main Chatbot UI
# -----------------------------
st.title("💬 General Health Chatbot")

st.write(
    """
    This chatbot provides **general health information** only.  
    It does **not** diagnose diseases or prescribe medications.
    """
)

user_question = st.text_input(
    "Ask a health-related question:",
    placeholder="e.g., What causes a sore throat?"
)

# -----------------------------
# Function to Ask the LLM
# -----------------------------
def ask_groq(question):
    system_prompt = (
        "You are a friendly health information assistant. "
        "Provide simple and safe general health explanations. "
        "Do NOT give medical diagnosis or prescribe medications. "
        "Always encourage seeing a doctor for serious symptoms."
    )

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0.4,
        max_tokens=300
    )

    return response.choices[0].message.content

# -----------------------------
# Generate Response
# -----------------------------
if st.button("Get Answer"):
    if user_question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                answer = ask_groq(user_question)
                st.subheader("🤖 Chatbot Response:")
                st.write(answer)

            except Exception as e:
                st.error(f"Error: {e}")

import streamlit as st
import google.generativeai as genai

KEY = "Enter your Key"
genai.configure(api_key=KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI Dashboard", layout="wide")

menu = st.sidebar.radio("Menu", ["Dashboard", "Chatbot", "Help"])

if menu == "Dashboard":
    st.title("AI Dashboard")
    col1, col2 = st.columns(2)
    col1.metric("Model", "Gemini 2.5 Flash")
    col2.metric("Mode", "Streaming")
    st.write("Welcome to the AI Dashboard. Open the Chatbot from the menu.")

elif menu == "Chatbot":
    st.title("Chatbot")   

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

    for role, text in st.session_state.chat_history:
        if role == "user":
            st.write("You: " + text)
        else:
            st.write("Bot: " + text)

    def send_message():
        text = st.session_state.user_input
        if text.strip() == "":
            return
        st.session_state.chat_history.append(("user", text))
        st.session_state.user_input = ""
        placeholder = st.empty()
        bot_text = ""
        try:
            response = model.generate_content(text, stream=True)
            for chunk in response:
                bot_text += (chunk.text or "")
                placeholder.write("Bot: " + bot_text)
            st.session_state.chat_history.append(("bot", bot_text))
        except Exception as e:
            st.write("Error:", e)
        st.rerun()

    st.text_input("You:", key="user_input", on_change=send_message)
    st.button("Send", on_click=send_message)

elif menu == "Help":
    st.title("Help")
    box = st.container()
    box.subheader("Contact Information")
    box.write("Name: Enter Your")
    box.write("Phone: Enter Your")
    box.write("Email: Enter Your")

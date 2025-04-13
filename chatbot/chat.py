from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")
chat = model.start_chat(history=[])

# Function to check if question is AKTU related
def is_aktu_related(question):
    prompt = f"""Is the following question related to Dr. A.P.J. Abdul Kalam Technical University (AKTU), its exams, syllabus, colleges, or student-related issues?

    Question: "{question}"

    Reply only with "yes" or "no"."""
    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)
    return "yes" in response.text.strip().lower()

# Function to get AKTU-related answer
def get_aktu_response(question):
    system_prompt = """You are an assistant that only answers questions related to AKTU (Dr. A.P.J. Abdul Kalam Technical University). 
    Only respond if the question is about AKTU's syllabus, colleges, exams, results, or student life."""
    prompt = f"{system_prompt}\n\nQuestion: {question}"
    response = chat.send_message(prompt, stream=True)
    return response

# Streamlit UI
st.set_page_config(page_title="AKTU Assistant")
st.title("🎓 AKTU Student Assistant")
st.write("Ask anything related to AKTU — syllabus, exams, results, etc.")

# Chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Input from user
question = st.text_input("Your question:")
if st.button("Ask") and question:
    st.session_state.chat_history.append(("You", question))
    
    with st.spinner("Checking your question..."):
        if is_aktu_related(question):
            with st.spinner("Getting AKTU answer..."):
                response = get_aktu_response(question)
                answer = ""
                for chunk in response:
                    answer += chunk.text
                st.session_state.chat_history.append(("AKTU Bot", answer))
                st.success("Answer generated!")
        else:
            warning = "❌ I can only answer AKTU-related questions. Please try again."
            st.session_state.chat_history.append(("AKTU Bot", warning))
            st.warning(warning)

# Display chat history
st.subheader("🗂 Chat History")
for role, msg in st.session_state.chat_history:
    st.write(f"**{role}:** {msg}")

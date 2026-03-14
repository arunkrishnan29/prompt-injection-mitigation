import streamlit as st
from detector import PromptInjectionDetector
from sanitizer import sanitize_prompt
from llm_interface import query_llm

st.set_page_config(
    page_title="Prompt Injection Security System",
    page_icon="🛡️"
)

st.title("Prompt Injection Mitigation System")

detector = PromptInjectionDetector()

user_prompt = st.text_input("Enter your prompt")

if st.button("Submit"):

    if detector.detect(user_prompt):
        st.warning("⚠ Prompt Injection Detected!")

        safe_prompt = sanitize_prompt(user_prompt)

        st.write("Sanitized Prompt:", safe_prompt)

        response = query_llm(safe_prompt)

    else:
        response = query_llm(user_prompt)

    st.success(response)
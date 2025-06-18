# app/main.py

import streamlit as st
from dotenv import load_dotenv

from ui.generation_eval import generation_eval_page
from ui.summary_eval import summary_eval_page
from ui.history import history_page

load_dotenv()

def main_page():
    st.set_page_config(page_title="에세이 생성·요약 평가 시스템")
    st.title(f"에세이 생성·요약 평가 시스템")

    if 'history' not in st.session_state:
        st.session_state.history = []

    st.sidebar.markdown("## 📋 메뉴")
    if st.sidebar.button("에세이 생성 및 평가"):
        st.session_state["page"] = "generation_eval"
    if st.sidebar.button("에세이 요약 및 평가"):
        st.session_state["page"] = "summary_eval"
    if st.sidebar.button("이전 평가"):
        st.session_state["page"] = "history"
    
    page = st.session_state.get("page", "generation_eval")
    if page == "generation_eval":
        generation_eval_page()
    elif page == "summary_eval":
        summary_eval_page()
    elif page == "history":
        history_page()

if __name__ == "__main__":
    main_page()
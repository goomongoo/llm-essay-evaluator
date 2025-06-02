# app/ui/history.py

import streamlit as st


def history_page():
    st.markdown("## 이전 평가 기록")

    if "history" not in st.session_state or not st.session_state.history:
        st.info("아직 평가 기록이 없습니다.")
        return

    for i, entry in enumerate(st.session_state.history):
        entry_type = entry.get("type", "N/A").capitalize()
        timestamp = entry.get("timestamp", "N/A")
        model_name = entry.get("model_name", "N/A")

        with st.expander(
                f"{i + 1}. [{model_name}] {entry_type}: {entry.get('prompt', entry.get('original_essay', ''))[:20]}... ({timestamp})"):
            st.markdown(f"**타입:** {entry_type}")
            st.markdown(f"**모델:** {model_name}")
            st.markdown(f"**최대 글자수:** {entry.get('max_length', 'N/A')}")

            if entry["type"] == "generation":
                st.markdown("**프롬프트:**")
                st.text_area("Prompt", entry.get("prompt", ""), height=100, key=f"prompt_{i}", disabled=True)
                st.markdown("**생성된 에세이:**")
                st.text_area("Generated Essay", entry.get("generated_text", ""), height=200, key=f"gen_text_{i}",
                             disabled=True)
            elif entry["type"] == "summary":
                st.markdown("**원본 에세이:**")
                st.text_area("Original Essay", entry.get("original_essay", ""), height=150, key=f"orig_text_{i}",
                             disabled=True)
                st.markdown("**생성된 요약:**")
                st.text_area("Generated Summary", entry.get("generated_text", ""), height=150, key=f"sum_text_{i}",
                             disabled=True)

            st.markdown("---")
            st.markdown("#### 평가 결과")
            results = entry.get("evaluation_results", {})
            if results:
                for metric, detail in results.items():
                    st.markdown(f"##### {metric.upper()}")
                    score = detail.get('score', 'N/A')
                    reason = detail.get('reason', 'N/A')
                    st.write(f"점수: {score}점")
                    st.write(f"사유: {reason}")
                    st.markdown("---")
            else:
                st.write("평가 결과가 없습니다.")
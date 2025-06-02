# app/ui/summary_eval.py

import streamlit as st
import sys
import os
from langchain_core.runnables import RunnableMap
from datetime import datetime

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from main import summarize_essay, MODELS
from evaluators.content import evaluate_content
from evaluators.coherence import evaluate_coherence
from evaluators.fluency import evaluate_fluency
from evaluators.hallucination import evaluate_hallucination
from evaluators.length import evaluate_length

def summary_eval_page():
    st.markdown("## 에세이 요약 및 평가")

    essay_original = st.text_area("원본 에세이", height=300, key="original_essay_area")
    max_length = st.number_input("최대 요약 글자 수", min_value=50, max_value=500, value=150, step=25, key="summary_max_length")

    st.markdown("### 모델 선택")
    model_name_selected = st.selectbox(
        "에세이 요약에 사용할 모델을 선택하세요:",
        MODELS,
        key="summary_model_select"
    )
    model_idx = MODELS.index(model_name_selected)

    if st.button("에세이 요약 및 평가", key="summarize_evaluate_button"):
        if not essay_original:
            st.warning("원본 에세이를 입력해주세요.")
        else:
            st.info(f"입력된 최대 요약 글자 수: {max_length}")
            st.info(f"선택된 모델: {model_name_selected}")

            summarization_context = {
                "essay_original": essay_original,
                "max_length": max_length,
                "model_idx": model_idx,
            }

            with st.spinner("에세이 요약 중..."):
                summary = summarize_essay(summarization_context)

            st.success("에세이 요약 완료!")
            st.markdown("### 생성된 요약")
            st.text_area("generated_summary", summary, height=200, key="generated_summary_area")

            st.markdown("---")
            st.markdown("### 요약 평가")
            with st.spinner("요약 평가 중..."):
                evaluation_context = {
                    "prompt": "N/A for summary evaluation",
                    "input_text": summary,
                    "original_text": essay_original,
                    "summarized_text": summary
                }

                evaluation_chain = RunnableMap({
                    "content": evaluate_content,
                    "coherence": evaluate_coherence,
                    "fluency": evaluate_fluency,
                })

                results = evaluation_chain.invoke(evaluation_context)
                results["hallucination"] = evaluate_hallucination(evaluation_context)
                results["length"] = evaluate_length(summary, max_length)

            st.success("요약 평가 완료!")
            st.markdown("#### 평가 결과")
            for metric, detail in results.items():
                st.markdown(f"##### {metric.upper()}")
                # 할루시네이션 평가 결과는 특별한 형식으로 표시
                if metric=="length":
                    if detail['score']:
                        st.write("✅ 만족")
                    else:
                        st.write("❌ 불만족")
                elif metric == "hallucination":
                    if detail['score']:
                        st.write("❌ 불만족")
                    else:
                        st.write("✅ 만족")
                else:
                    st.write(f"점수: {detail['score']}점")
                st.write(f"사유: {detail['reason']}")
                st.markdown("---")

            # Save to history
            history_entry = {
                "type": "summary",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "original_essay": essay_original,
                "max_length": max_length,
                "model_name": model_name_selected,
                "generated_text": summary,
                "evaluation_results": results,
            }
            st.session_state.history.insert(0, history_entry) # Insert at the beginning
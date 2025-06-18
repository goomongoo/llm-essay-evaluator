# app/ui/generation_eval.py

import streamlit as st
import sys
import os

from fontTools.varLib.cff import merge_region_fonts
from langchain_core.runnables import RunnableMap
from datetime import datetime

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from llm_tasks import generate_essay, MODELS
from evaluators.content import evaluate_content
from evaluators.coherence import evaluate_coherence
from evaluators.fluency import evaluate_fluency
from evaluators.length import evaluate_length

def generation_eval_page():
    st.markdown("## 에세이 생성 및 평가")

    max_length = st.number_input("최대 글자 수", min_value=100, max_value=1000, value=250, step=50)
    essay_prompt = st.text_area("에세이 프롬프트", height=150)

    st.markdown("### 모델 선택")
    model_name_selected = st.selectbox(
        "에세이 생성에 사용할 모델을 선택하세요:",
        MODELS
    )
    model_idx = MODELS.index(model_name_selected)

    if st.button("에세이 생성 및 평가", key="generate_evaluate_button"):
        if not essay_prompt:
            st.warning("에세이 프롬프트를 입력해주세요.")
        else:
            st.info(f"입력된 최대 글자 수: {max_length}")
            st.info(f"입력된 프롬프트: {essay_prompt}")
            st.info(f"선택된 모델: {model_name_selected}")

            generation_context = {
                "essay_prompt": essay_prompt,
                "max_length": max_length,
                "model_idx": model_idx,
            }

            with st.spinner("에세이 생성 중..."):
                essay = generate_essay(generation_context)

            st.success("에세이 생성 완료!")
            st.markdown("### 생성된 에세이")
            st.text_area("generated_essay", essay, height=300, key="generated_essay_area")

            st.markdown("---")
            st.markdown("### 에세이 평가")
            with st.spinner("에세이 평가 중..."):
                evaluation_context = {
                    "prompt": essay_prompt,
                    "input_text": essay,
                }

                evaluation_chain = RunnableMap({
                    "content": evaluate_content,
                    "coherence": evaluate_coherence,
                    "fluency": evaluate_fluency,
                })

                results = evaluation_chain.invoke(evaluation_context)
                results["length"] = evaluate_length(essay, max_length)

            st.success("에세이 평가 완료!")
            st.markdown("#### 평가 결과")
            for metric, detail in results.items():
                st.markdown(f"##### {metric.upper()}")
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
                "type": "generation",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "prompt": essay_prompt,
                "max_length": max_length,
                "model_name": model_name_selected,
                "generated_text": essay,
                "evaluation_results": results,
            }
            st.session_state.history.insert(0, history_entry)
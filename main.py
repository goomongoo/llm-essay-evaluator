# main.py

# Evaluator based on CLI, not streamlit

import sys
import argparse
from dotenv import load_dotenv
from langchain_core.runnables import RunnableMap
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from evaluators.content import evaluate_content
from evaluators.coherence import evaluate_coherence
from evaluators.fluency import evaluate_fluency
from evaluators.hallucination import evaluate_hallucination
from evaluators.length import evaluate_length
import prompts.generation_prompt as generation_prompt

load_dotenv()

MODELS = ["gpt-4o", "gpt-4.1", "gemini-2.0-flash", "gemma2-9b-it", "llama-3.1-8b-instant"]

def run_llm(context: dict, prompt):
    model_idx = context["model_idx"]

    if model_idx < 0 or model_idx >= len(MODELS):
        return None

    if model_idx <= 1:
        llm = ChatOpenAI(model=MODELS[model_idx])
        chain = prompt | llm
        response = chain.invoke(context)
        result = response.content
    elif model_idx == 2:
        llm = ChatGoogleGenerativeAI(model=MODELS[model_idx])
        chain = prompt | llm
        response = chain.invoke(context)
        result = response.content
    else:
        llm = ChatGroq(model=MODELS[model_idx])
        chain = prompt | llm
        response = chain.invoke(context)
        result = response.content

    return result

def generate_essay(context: dict):
    prompt = ChatPromptTemplate.from_template(generation_prompt.GENERATION_PROMPT)
    return run_llm(context, prompt)

def generate_essay_feedback(context: dict):
    prompt = ChatPromptTemplate.from_template(generation_prompt.GENERATION_PROMPT_FEEDBACK)
    return run_llm(context, prompt)

def summarize_essay(context: dict):
    prompt = ChatPromptTemplate.from_template(generation_prompt.SUMMARY_PROMPT)
    return run_llm(context, prompt)

def summarize_essay_feedback(context: dict):
    prompt = ChatPromptTemplate.from_template(generation_prompt.SUMMARY_PROMPT_FEEDBACK)
    return run_llm(context, prompt)

def generation_evaluator(max_length: int):
    essay_prompt = input("에세이 프롬프트를 입력하세요: ")
    print("\n에세이 생성에 사용할 모델 번호를 선택하세요:")
    for idx, model_name in enumerate(MODELS):
        print(f"  {idx}. {model_name}")
    model_idx = int(input("모델 번호 입력: "))

    context = {
        "essay_prompt": essay_prompt,
        "max_length": max_length,
        "model_idx": model_idx,
    }

    print("\n에세이 생성 중...\n" + "=" * 50)
    essay = generate_essay(context)

    print("\n생성된 에세이\n" + "-" * 50)
    print(essay)
    print("-" * 50)

    print("\n에세이 평가 중...\n" + "=" * 50)
    context = {
        "prompt": essay_prompt,
        "input_text": essay,
    }

    evaluation_chain = RunnableMap({
        "content": evaluate_content,
        "coherence": evaluate_coherence,
        "fluency": evaluate_fluency,
    })

    result = evaluation_chain.invoke(context)
    result["length"] = evaluate_length(essay, max_length)

    print("\n에세이 평가 결과\n" + "-" * 50)
    for metric, detail in result.items():
        print(f"[{metric.upper()}]")
        print(f"점수: {detail['score']}점")
        print(f"사유: {detail['reason']}\n")
    print("-" * 50)

def summarization_evaluator(max_length: int):
    essay_original = input("에세이 원문을 입력하세요: ")
    print("\n에세이 요약에 사용할 모델 번호를 선택하세요:")
    for idx, model_name in enumerate(MODELS):
        print(f"  {idx}. {model_name}")
    model_idx = int(input("모델 번호 입력: "))

    context = {
        "essay_original": essay_original,
        "max_length": max_length,
        "model_idx": model_idx,
    }

    print("\n에세이 요약 중...\n" + "=" * 50)
    essay = summarize_essay(context)

    print("\n요약된 에세이\n" + "-" * 50)
    print(essay)
    print("-" * 50)

    print("\n에세이 평가 중...\n" + "=" * 50)
    context = {
        "prompt": "Prompt is not given because {{input_text}} is summarized essay",
        "input_text": essay,
    }

    evaluation_chain = RunnableMap({
        "content": evaluate_content,
        "coherence": evaluate_coherence,
        "fluency": evaluate_fluency,
    })

    result = evaluation_chain.invoke(context)
    result["hallucination"] = evaluate_hallucination({
        "original_text": essay_original,
        "summarized_text": essay
    })
    result["length"] = evaluate_length(essay, max_length)

    print("\n에세이 평가 결과\n" + "-" * 50)
    for metric, detail in result.items():
        print(f"[{metric.upper()}]")
        print(f"점수: {detail['score']}점")
        print(f"사유: {detail['reason']}\n")
    print("-" * 50)

    return result

parser = argparse.ArgumentParser()
parser.add_argument('--option', help=' : generation or summary')
parser.add_argument('--length', help=' : maximum number of characters (100~500)', type=int)
args = parser.parse_args()

import sys

def main(_argv, _args):
    if not hasattr(_args, 'option') or _args.option is None:
        print('--option 인자가 필요합니다. (generation 또는 summary)')
        sys.exit(1)

    if not hasattr(_args, 'length') or _args.length is None:
        print('--length 인자가 필요합니다. (100에서 1000 사이의 자연수)')
        sys.exit(1)

    if int(_args.length) < 100 or int(_args.length) > 1000:
        print('--length는 100에서 1000 사이의 자연수여야 합니다.')
        sys.exit(1)

    if _args.option == 'generation':
        generation_evaluator(int(_args.length))
    elif _args.option == 'summary':
        summarization_evaluator(int(_args.length))
    else:
        print('--option은 generation 또는 summary 중 하나여야 합니다.')
        sys.exit(1)


if __name__ == "__main__":
    argv = sys.argv
    main(argv, args)
# evaluators/llm_runner.py

import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from utils.logger import logger
from utils.scoring import get_expected_score
from dotenv import load_dotenv
import config

load_dotenv()

def run_llm_evaluation(prompt_template: str, context: dict, tag: str):
    llm = ChatOpenAI(
        model=config.MODEL_NAME,
        temperature=config.LLM_TEMPERATURE,
        top_p=config.TOP_P,
    )

    prompt = ChatPromptTemplate.from_template(prompt_template)
    chain = prompt | llm

    repeat_count = config.REPEAT_EVAL_COUNT
    scores = []

    for i in range(repeat_count):
        logger.info(f"[{tag}] LLM Evaluation iteration {i + 1}/{repeat_count}")

        try:
            response = chain.invoke({
                "prompt": context["prompt"],
                "input_text": context["input_text"],
            })
            logger.debug(f"[{tag}] Raw LLM response: {response.content}")

            score = int(response.content.strip())
            scores.append(score)

        except Exception as e:
            logger.warning(f"[{tag}] Failed on iteration {i + 1}: {e}")

    expected_score = get_expected_score(scores)

    return expected_score

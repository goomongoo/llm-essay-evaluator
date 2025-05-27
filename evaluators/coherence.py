# evaluators/coherence.py

import json
import config
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from utils.logger import logger
from prompts.coherence_prompt import COHERENCE_PROMPT

load_dotenv()

llm = ChatOpenAI(
    model=config.MODEL_NAME,
    temperature=config.LLM_TEMPERATURE,
    top_p=config.TOP_P,
)

def evaluate_coherence(context: dict):
    prompt = ChatPromptTemplate.from_template(COHERENCE_PROMPT)
    chain = prompt | llm

    try:
        response = chain.invoke({
            "prompt": context["prompt"],
            "input_text": context["input_text"],
        })
        logger.debug(f"[Coherence] Raw LLM response: {response.content}")
        result = json.loads(response.content)

        if not isinstance(result, dict) or "score" not in result or "reason" not in result:
            raise ValueError("Unexpected Format")

        return result

    except Exception as e:
        logger.error(f"[Coherence] Error: {e}")
        return {
            "score": None,
            "reason": None
        }
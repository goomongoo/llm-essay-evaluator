# evaluators/hallucination.py

import json
import config
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from prompts.hallucination_prompt import HALLUCINATION_PROMPT
from utils.logger import logger

load_dotenv()

llm = ChatOpenAI(
    model=config.MODEL_NAME,
    temperature=config.LLM_TEMPERATURE,
    top_p=config.TOP_P,
)

def evaluate_hallucination(context: dict):
    prompt = ChatPromptTemplate.from_template(HALLUCINATION_PROMPT)
    chain = prompt | llm

    try:
        response = chain.invoke({
            "original_text": context.get("original_text"),
            "summarized_text": context.get("summarized_text"),
        })

        logger.debug(f"[Hallucination] Raw LLM response: {response.content}")
        result = json.loads(response.content)

        if not isinstance(result, dict) or "hallucination" not in result or "reason" not in result:
            raise ValueError("Unexpected format")

        return {
            "score": result["hallucination"],
            "reason": result["reason"],
        }

    except Exception as e:
        logger.error(f"[Hallucination] Error: {e}")
        return {
            "score": None,
            "reason": None
        }
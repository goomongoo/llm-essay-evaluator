# evaluators/fluency.py

import json
import config
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from utils.logger import logger
from prompts.fluency_prompt import FLUENCY_PROMPT

load_dotenv()

llm = ChatOpenAI(
    model=config.MODEL_NAME,
    temperature=config.LLM_TEMPERATURE,
    top_p=config.TOP_P,
)

def evaluate_fluency(context: dict):
    prompt = ChatPromptTemplate.from_template(FLUENCY_PROMPT)
    chain = prompt | llm

    try:
        response = chain.invoke({
            "prompt": context["prompt"],
            "input_text": context["input_text"],
        })
        logger.debug(f"[Fluency] Raw LLM response: {response.content}")
        result = json.loads(response.content)

        if not isinstance(result, dict) or "score" not in result or "reason" not in result:
            raise ValueError("Unexpected Format")

        return result

    except Exception as e:
        logger.error(f"[Fluency] Error: {e}")
        return {
            "score": None,
            "reason": None
        }
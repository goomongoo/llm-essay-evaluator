# evaluators/llm_runner.py

import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from utils.logger import logger
from utils.scoring import get_expected_score
from dotenv import load_dotenv
import config

load_dotenv()

def run_llm_evaluation(prompt_template: str, criteria: list[str], context: dict, tag: str):
    llm = ChatOpenAI(
        model=config.MODEL_NAME,
        temperature=config.LLM_TEMPERATURE,
        top_p=config.TOP_P,
    )

    prompt = ChatPromptTemplate.from_template(prompt_template)
    chain = prompt | llm

    score_dict = {criterion: [] for criterion in criteria}
    repeat_count = config.REPEAT_EVAL_COUNT

    for i in range(repeat_count):
        logger.info(f"[{tag}] LLM Evaluation iteration {i + 1}/{repeat_count}")

        try:
            response = chain.invoke({
                "prompt": context["prompt"],
                "input_text": context["input_text"],
            })
            logger.debug(f"[{tag}] Raw LLM response: {response.content}")

            parsed_scores = json.loads(response.content)

            for item in parsed_scores:
                criterion = item["criterion"]
                score = item["score"]
                if criterion in score_dict:
                    score_dict[criterion].append(score)

        except Exception as e:
            logger.warning(f"[{tag}] Failed on iteration {i + 1}: {e}")

    expected_scores = {
        criterion: get_expected_score(scores)
        for criterion, scores in score_dict.items()
    }

    return expected_scores

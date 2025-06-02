# tests/content.py

import os
import json
from dotenv import load_dotenv
from glob import glob
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from scipy.stats import spearmanr
from tqdm import tqdm

import config
from utils.logger import logger
from utils.scoring import get_expected_score
import tests.prompts.content_prompt as content_prompt

load_dotenv()

llm = ChatOpenAI(
        model=config.MODEL_NAME,
        temperature=config.LLM_TEMPERATURE,
        top_p=config.TOP_P,
)

DATASET_DIR = os.environ.get("ESSAY_DATASET_DIR")

def evaluate_content_test(context: dict):
    prompt = ChatPromptTemplate.from_template(content_prompt.PLAN_SOLVE_ONESHOT)
    chain = prompt | llm

    repeat_count = config.REPEAT_EVAL_COUNT
    scores = []

    for i in range(repeat_count):
        logger.info(f"[Content] LLM Evaluation iteration {i + 1}/{repeat_count}")

        try:
            response = chain.invoke({
                "prompt": context["prompt"],
                "input_text": context["input_text"],
            })
            logger.debug(f"[Content] Raw LLM response: {response.content}")

            score = int(response.content.strip())
            scores.append(score)

        except Exception as e:
            logger.warning(f"[Content] Failed on iteration {i + 1}: {e}")

    expected_score = get_expected_score(scores)

    return expected_score

def main():
    file_paths = glob(os.path.join(DATASET_DIR, "*.json"))

    human_scores = []
    llm_scores = []

    for path in tqdm(file_paths, desc="Evaluating essays"):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        prompt = data["info"]["essay_prompt"]
        paragraphs = data["paragraph"]
        llm_input = "\n".join([p["paragraph_txt"] for p in paragraphs])

        human_score = float(data["score"]["essay_scoreT_detail"]["essay_scoreT_cont"])
        llm_score = evaluate_content_test({
            "prompt": prompt,
            "input_text": llm_input,
        })

        human_scores.append(human_score)
        llm_scores.append(llm_score)

    spearman = spearmanr(human_scores, llm_scores)[0]

    print("\nCorrelation Results (Content Score)")
    print(f"    Spearman: {spearman:.3f}")

if __name__ == "__main__":
    main()
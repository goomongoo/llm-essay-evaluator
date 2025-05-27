# tests/hallucination.py

import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from tqdm import tqdm

import config
from utils.logger import logger
import tests.prompts.hallucination_prompt as hallucination_prompt

load_dotenv()

llm = ChatOpenAI(
        model=config.MODEL_NAME,
        temperature=config.LLM_TEMPERATURE,
        top_p=config.TOP_P,
)

FILE_PATH = os.environ.get("HALLU_DATASET_PATH")

def evaluate_hallucination_test(context: dict):
    prompt = ChatPromptTemplate.from_template(hallucination_prompt.BASE)
    chain = prompt | llm

    try:
        response = chain.invoke({
            "original_text": context.get("original_text"),
            "summarized_text": context.get("summarized_text"),
        })

        logger.debug(f"[Hallucination] Raw LLM response: {response.content}")
        result = json.loads(response.content)

        if not isinstance(result, dict) or "hallucination" not in result:
            raise ValueError("Unexpected format")

        return result

    except Exception as e:
        logger.error(f"[Hallucination Eval] Error: {e}")
        return {
            "hallucination": None,
        }

def load_dataset(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def main():
    dataset = load_dataset(FILE_PATH)

    total = 0
    correct = 0

    tp = fp = tn = fn = 0

    for data in tqdm(dataset, desc="Evaluating hallucination"):
        for key, label in [("right_summary", False), ("hallucinated_summary", True)]:
            total += 1

            result = evaluate_hallucination_test({
                "original_text": data["document"],
                "summarized_text": data[key],
            })
            predicted = result.get("hallucination")

            if predicted is None:
                continue

            if predicted == label:
                correct += 1

            if label:
                if predicted:
                    tp += 1
                else:
                    fn += 1
            else:
                if predicted:
                    fp += 1
                else:
                    tn += 1

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    accuracy = correct / total * 100 if total > 0 else 0

    print(f"\n Hallucination Evaluation Results:")
    print(f"    Total Data              : {total}")
    print(f"    Correct Predictions     : {correct}")
    print(f"    Accuracy                : {accuracy:.2f}%")
    print(f"    Precision               : {precision:.3f}")
    print(f"    Recall                  : {recall:.3f}")
    print(f"    F1                      : {f1:.3f}")
    print(f"\n Confusion Matrix:")
    print(f"    TP={tp}, FP={fp}, TN={tn}, FN={fn}")

if __name__ == "__main__":
    main()
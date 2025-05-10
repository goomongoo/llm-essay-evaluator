import os
import json
import random
from glob import glob

from config import DATASET_DIR, COHERENCE_CRITERIA
from evaluators.coherence import evaluate_coherence
from scipy.stats import pearsonr, spearmanr


def load_json_files(base_dir: str, limit: int = None, randomize: bool = False):
    json_paths = glob(os.path.join(base_dir, "*.json"))
    if randomize:
        random.shuffle(json_paths)
    return json_paths if limit is None else json_paths[:limit]


def print_and_evaluate_total_content_scores(limit: int = 10, randomize: bool = True):
    file_paths = load_json_files(DATASET_DIR, limit=limit, randomize=randomize)

    print(f"📂 Evaluating {len(file_paths)} essay files from: {DATASET_DIR}\n")

    human_total_scores = []
    llm_total_scores = []

    for idx, path in enumerate(file_paths):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        prompt = data["info"]["essay_prompt"]
        paragraphs = data["paragraph"]
        llm_input = "\n".join([p["paragraph_txt"] for p in paragraphs])

        gt_scores = data["score"]["essay_scoreT_detail"]["essay_scoreT_org"]
        llm_result = evaluate_coherence({
            "prompt": prompt,
            "input_text": llm_input
        })

        human_total = round(sum(gt_scores), 2)
        llm_total = round(sum(llm_result[criterion] for criterion in COHERENCE_CRITERIA), 2)

        human_total_scores.append(human_total)
        llm_total_scores.append(llm_total)

        print(f"📄 Essay {idx+1}: {os.path.basename(path)}")
        print(f"   Human Total Score : {human_total}")
        print(f"   LLM Total Score   : {llm_total}")
        print("-" * 40)

    # 상관관계 계산
    print("\n📊 Correlation Results (Total Coherence Score)")
    if len(human_total_scores) < 2:
        print("Not enough data for correlation.")
        return

    pearson = pearsonr(human_total_scores, llm_total_scores)[0]
    spearman = spearmanr(human_total_scores, llm_total_scores)[0]

    print(f"   Pearson  : {pearson:.3f}")
    print(f"   Spearman : {spearman:.3f}")


if __name__ == "__main__":
    print_and_evaluate_total_content_scores(limit=50, randomize=True)

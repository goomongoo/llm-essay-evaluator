# evaluators/fluency.py

import config
from prompts.fluency_prompt import FLUENCY_PROMPT
from evaluators.llm_runner import run_llm_evaluation

def evaluate_fluency(context: dict):
    return run_llm_evaluation(
        prompt_template=FLUENCY_PROMPT,
        criteria=config.FLUENCY_CRITERIA,
        context=context,
        tag="Fluency"
    )
# evaluators/coherence.py

import config
from prompts.coherence_prompt import COHERENCE_PROMPT
from evaluators.llm_runner import run_llm_evaluation

def evaluate_coherence(context: dict):
    return run_llm_evaluation(
        prompt_template=COHERENCE_PROMPT,
        criteria=config.COHERENCE_CRITERIA,
        context=context,
        tag="Coherence"
    )
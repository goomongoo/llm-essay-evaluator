# evaluators/content.py

import config
from prompts.content_prompt import CONTENT_PROMPT
from evaluators.llm_runner import run_llm_evaluation

def evaluate_content(context: dict):
    return run_llm_evaluation(
        prompt_template=CONTENT_PROMPT,
        context=context,
        tag="Content"
    )
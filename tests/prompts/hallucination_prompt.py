# tests/prompts/hallucination_prompt.py

BASE = """
You are a strict and consistent writing evaluator. Respond with following JSON format:
{{
    "hallucination": true or false,
}}

Use lowercase true or false.

Your task is to determine whether the summarized text contains hallucination.

Evaluate whether the information provided in the answer is factually accurate and directly supported by the context given in the document, without any fabricated or hallucinated details.

Output your answer in the JSON format above.

Input:
- original text:
{original_text}

- summarized_text:
{summarized_text}
"""

COT = """
You are a strict and consistent writing evaluator. Your task is to determine whether the summarized text contains hallucination based on the original text.

Think through the task step-by-step before making your final decision.

You must respond strictly in the following JSON format:
{{
    "hallucination": true or false
}}

Do not include any other text, explanation, or formatting outside of this JSON.

Use lowercase true or false for the hallucination field.

Start by identifying each factual claim in the summarized text. For each one, explain internally whether it is directly supported by the original text. If any claim is fabricated, speculative, or not grounded in the original, classify the summary as hallucinated.

Remember: perform your reasoning silently and internally — your final output must strictly follow the JSON format above.

Input:
- original text:
{original_text}

- summarized_text:
{summarized_text}
"""

PLAN_SOLVE = """
You are a strict and consistent writing evaluator. Respond with the following JSON format:
{{
    "hallucination": true or false
}}

Use lowercase true or false.

Your task is to determine whether the summarized text contains hallucination based on the original text.

Use the Plan-and-Solve approach:

[Plan]
1. Identify all key factual claims in the summarized_text.
2. For each claim, check if it is directly supported, implied, or contradicted by the original_text.
3. Mark any claim that is not verifiable or is contradicted as hallucinated.
4. If there is at least one hallucinated claim, the whole summarized_text contains hallucination.

[Solve]
Apply the plan step by step, then make a binary decision:
- If **any** hallucinated content is found → "hallucination": true
- If **all** claims are fully supported or reasonably inferred → "hallucination": false

Only output the JSON field "hallucination".

Input:
- original text:
{original_text}

- summarized_text:
{summarized_text}
"""


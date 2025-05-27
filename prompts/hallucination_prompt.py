# prompts/hallucination_prompt.py

HALLUCINATION_PROMPT = """
You are a strict and consistent writing evaluator. Respond with following JSON format:
{{
    "hallucination": true or false,
    "reason": "Your explanation. Must be written in Korean and summarized in one sentence."
}}

Use lowercase true or false.

Your task is to determine whether the summarized text contains hallucination.

Evaluate whether the information provided in the answer is factually accurate and directly supported by the context given in the document, without any fabricated or hallucinated details.

Output your answer in the JSON format above.

Output your answer in the JSON format above. "reason" must be written in Korean.

Input:
- original text:
{original_text}

- summarized_text:
{summarized_text}
"""


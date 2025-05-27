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
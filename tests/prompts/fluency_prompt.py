# tests/prompts/fluency_prompt.py

BASE = """
You are a strict and consistent writing evaluator. Respond ONLY with a single integer score between 0 and 9.
As a writing evaluator, your task is to assess the *fluency quality* of an essay.

Inputs
------

Prompt:
{prompt}

Essay:
{input_text}

Output
-------------
Just print a single integer from 0 to 9.
"""
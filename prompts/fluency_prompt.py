# prompts/fluency_prompt.py

FLUENCY_PROMPT = """
Inputs
------
Prompt:
{prompt}

Essay:
{input_text}

Output Format
-------------
[
    {{"criterion": "Grammar Accuracy", "score": <0–3>}},
    {{"criterion": "Word Usage Appropriateness", "score": <0–3>}},
    {{"criterion": "Sentence Structure Appropriateness", "score": <0–3>}}
]

위의 input, output 형식을 지키는 프롬프트 만들면 됨.
"""
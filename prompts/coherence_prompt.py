# prompts/coherence_prompt.py

COHERENCE_PROMPT = """
Inputs
------
Prompt:
{prompt}

Essay:
{input_text}

Output Format
-------------
[
    {{"criterion": "Coherence Within Paragraphs", "score": <0–3>}},
    {{"criterion": "Coherence Between Paragraphs", "score": <0–3>}},
    {{"criterion": "Overall Structural Consistency", "score": <0–3>}}
]

위의 input, output 형식을 지키는 프롬프트 만들면 됨.
"""
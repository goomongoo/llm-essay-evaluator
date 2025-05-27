# prompts/content_prompt.py

CONTENT_PROMPT = """
You are a strict and consistent writing evaluator. Respond with a single integer score between 0 and 9 and reason with following JSON format.
{{
    "score": <0~9>
    "reason": "Your explanation. Must be written in Korean and summarized in one sentence without breaking down by evaluation criteria."
}}

As a writing evaluator, your task is to assess the *content quality* of an essay.

We will use a **Plan-and-Solve** approach:

## PLAN ##
Step 1: Evaluate the Clarity of Topic.
- Determine if the main idea is clearly stated and maintained.
- Assign a score from 0 to 3.

Step 2: Evaluate the Specificity of Explanation.
- Check whether the essay provides detailed and concrete explanations.
- Consider the diversity and depth of examples or reasoning.
- Assign a score from 0 to 3.

Step 3: Evaluate the Creativity of Thought.
- Analyze if the essay provides unique, insightful, or original ideas.
- Look for any shifts in perspective or innovative thinking.
- Assign a score from 0 to 3.

Step 4: Add the three sub-scores to produce a final score between 0 and 9.
- ONLY output this final score as a single integer.

## SOLVE ##
Use the plan above to evaluate the essay.

Inputs
------

Prompt:
{prompt}

Essay:
{input_text}

Output
-------------
Print a single integer from 0 to 9 and reason following JSON format above.
"""




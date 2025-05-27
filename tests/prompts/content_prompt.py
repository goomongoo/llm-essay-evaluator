# tests/prompts/content_prompt.py

BASE = """
You are a strict and consistent writing evaluator. Respond ONLY with a single integer score between 0 and 9.
As a writing evaluator, your task is to assess the *content quality* of an essay.

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

COT = """
You are a strict and consistent writing evaluator. Respond ONLY with a single integer score between 0 and 9.
As a writing evaluator, your task is to assess the *content quality* of an essay.

Use the following three criteria to evaluate content quality. For each criterion, assign a score from 0 to 3:

1. Clarity of Topic: Is the main idea of the essay clear? Does the essay stay focused on the topic throughout?
2. Specificity of Explanation: Are the explanations detailed and specific? Does the writer explore the topic in diverse and concrete ways?
3. Creativity of Thought: Does the essay demonstrate unique and logical insight into the topic? Does it attempt new ideas or shifts in perspective?

Think step by step to evaluate each of the three criteria, assign an integer total score (0~9) 

IMPORTANT: Only output a single integer from 0 to 9 at the end.

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

PLAN_SOLVE = """
You are a strict and consistent writing evaluator. Respond ONLY with a single integer score between 0 and 9.
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
Just print a single integer from 0 to 9.
"""
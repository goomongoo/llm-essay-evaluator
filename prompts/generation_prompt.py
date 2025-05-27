# prompts/generation_prompt.py

GENERATION_PROMPT = """
Based on the following prompt, generate an essay in Korean within {max_length} characters.

Prompt:
{essay_prompt}

Output:
The essay you created
"""

GENERATION_PROMPT_FEEDBACK = """
Based on the following prompt, the previously generated essay, and the feedback on it, generate a new essay in Korean within {max_length} characters.  
Maintain the core content and ideas of the previous essay while reflecting the feedback provided.

Prompt:
{essay_prompt}

Essay:
{essay_previous}

Feedback:
{essay_feedback}

Output:
The essay you created
"""

SUMMARY_PROMPT =  """
Summarize the following original essay in Korean within {max_length} characters.

Essay:
{essay_original}

Output:
The summarized essay you wrote
"""

SUMMARY_PROMPT_FEEDBACK = """
Based on the following original essay, its summarized version, and the feedback on it, write a revised summary in Korean within {max_length} characters.

Essay:
{essay_original}

Summarized Essay:
{essay_summary}

Feedback:
{essay_feedback}

Output:
The summarized essay you wrote
"""

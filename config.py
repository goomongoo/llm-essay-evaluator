# config.py

# Model configuration
MODEL_NAME = "gpt-4.1-mini-2025-04-14"
LLM_TEMPERATURE = 0.2
TOP_P = 1.0

# Repeat evaluation count
REPEAT_EVAL_COUNT = 3

# Length constraint penalty ratio
LENGTH_PENALTY_RATIO = 0.3

# Default max length
MAX_CHAR_LENGTH = 300

# Metrics
EVAL_METRICS = ["Coherence", "Fluency", "Content"]

COHERENCE_CRITERIA = [
    "Coherence Within Paragraphs",
    "Coherence Between Paragraphs",
    "Overall Structural Consistency",
]

FLUENCY_CRITERIA = [
    "Grammar Accuracy",
    "Word Usage Appropriateness",
    "Sentence Structure Appropriateness",
]

CONTENT_CRITERIA = [
    "Clarity of the Topic",
    "Specificity of Explanations",
    "Understanding of the Prompt",
]

# DATASET DIRECTORY
DATASET_DIR = "/home/mongoo/Workspace/essay_dataset"
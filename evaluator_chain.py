# evaluator_chain.py

from langchain_core.runnables import RunnableMap
from evaluators.content import evaluate_content
from evaluators.coherence import evaluate_coherence
from evaluators.fluency import evaluate_fluency

def evaluate_essay(context: dict):
    evaluation_chain = RunnableMap({
        "content": evaluate_content,
        "coherence": evaluate_coherence,
        "fluency": evaluate_fluency,
    })

    result = evaluation_chain.invoke(context)

    total_score = sum(
        sum(metric_scores.values()) for metric_scores in result.values()
    )
    result["total"] = total_score

    return result


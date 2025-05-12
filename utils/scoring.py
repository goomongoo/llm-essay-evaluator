# utils/scoring.py

from collections import Counter

def get_expected_score(sampled_scores: list[int]):
    score_range = list(range(10))
    count = Counter(sampled_scores)
    total = sum(count.values())

    if total == 0:
        return 0.0

    probabilities = {s: count.get(s, 0) / total for s in score_range}
    expected_score = sum(s * p for s, p in probabilities.items())

    return round(expected_score, 2)
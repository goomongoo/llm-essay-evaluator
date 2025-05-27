# evaluators/length.py

def evaluate_length(essay: str, max_length: int) -> dict:
    length = len(essay)
    min_allowed = int(max_length * 0.9)

    if length < min_allowed - 50:
        reason = f"글자 수가 너무 부족합니다 ({length}자 / 최소 {min_allowed}자)."
        score = False
    elif length < min_allowed:
        reason = f"글자 수가 다소 부족합니다 ({length}자 / 최소 {min_allowed}자)."
        score = False
    elif length <= max_length:
        reason = f"글자 수가 충족되었습니다 ({length}자 / 최대 {max_length}자)."
        score = True
    elif length <= max_length + 50:
        reason = f"글자 수가 다소 초과되었습니다 ({length}자 / 최대 {max_length}자)."
        score = False
    else:
        reason = f"글자 수가 너무 초과되었습니다 ({length}자 / 최대 {max_length}자)."
        score = False

    return {
        "score": score,
        "reason": reason
    }


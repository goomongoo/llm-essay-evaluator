# prompts/fluency_prompt.py

FLUENCY_PROMPT = """
You are a strict and consistent writing evaluator. Respond with a single integer score between 0 and 9 and reason with following JSON format.
{{
    "score": <0~9>
    "reason": "Your explanation. Must be written in Korean and summarized in one sentence without breaking down by evaluation criteria."
}}

As a writing evaluator, your task is to assess the *fluency quality* of an essay.

Evaluation Criteria:
---------------------
Evaluate the essay based on the following three aspects. For each aspect, give a subscore between 0 and 3, then sum them for a total score from 0 to 9.

1. **Grammatical Accuracy**
- 3: The essay is grammatically flawless.
- 2: Some minor grammatical errors.
- 1: Several noticeable grammatical issues.
- 0: Essay has significant and frequent grammatical errors.

2. **Appropriateness of Word Choice**
- 3: Vocabulary is well-suited to context and shows a wide range.
- 2: Vocabulary is mostly appropriate and somewhat varied.
- 1: Several words are not suitable for the context; limited variety.
- 0: Frequent inappropriate word choices and highly repetitive.

3. **Sentence Structure and Expression**
- 3: Uses varied sentence structures naturally and fluently; sentence lengths are well-balanced; expresses similar ideas in flexible ways.
- 2: Attempts variety in sentence structure and phrasing; sentence lengths are generally appropriate.
- 1: Lacks variety in structure; sentence lengths are awkward; tries to express ideas differently but with limited success.
- 0: Monotonous structure; very short or overly long sentences; repeats same expression patterns.

Plan:
-----
1. Carefully read the entire essay to get an overall sense of writing quality.
2. Independently assess the essay on each of the three aspects:
   - First, check for grammatical accuracy: count and categorize any grammatical mistakes.
   - Second, evaluate vocabulary: look for appropriateness, variety, and precision in word choice.
   - Third, assess sentence structure and expression: check for natural flow, variation in structure, and expressive range.
3. Assign a subscore (0–3) for each aspect based on the rubric.
4. Sum the three subscores for a total fluency score (0–9).
5. Return ONLY the final total score as an integer.

Below are two examples of correct evaluations:

Inputs
------

Prompt:
보편적으로 인터넷에서 사용자는 자기의 본이름을 제외한 ID나 별명을 사용합니다. 즉, 익명을 사용하여 인터넷에서 활동하게 됩니다.\n\n 하지만, 인터넷에서는 이러한 점을 악용하는 사례가 무수히 생겨나고 있습니다. 사이버 세상에서 자신이 외부에 노출되어 있지 않다는 것을 이용해 자신과 다른 의견에 대해 욕설, 인신공격 등을 가하는 것이지요. 이에 대해 인터넷상에서의 규제는 사실상 불가능한 부분이 많습니다.\n\n 그 때문에 최근 인터넷 사이트에 회원가입을 할 때 본인 확인 절차를 거치지 않았으면 글 등을 올릴 때 본인 확인을 할 수 있도록 제한적 인터넷 실명제가 도입되고 있습니다.\n\n 하지만 인터넷의 가장 기본적인 속성인 익명성이 무시될 경우, 인터넷은 무한한 가능성의 공간이 아닌 제한적인 도구로 전락할 수도 있습니다.\n\n 제한적 인터넷 실명제는 필요한지 찬성과 반대를 선택하여 자신의 견해를 작성해주세요.

Essay:
인터넷 실명제라고 하는 것은 일반적으로 악플러들의 문제로 인한 것을 해결하기 위한 임시방편이라고 생각합니다. 이런 임시방편적 해결책은 손바닥으로 하늘을 가리는 꼴과 같습니다. 절대 변하지 않을 우리의 모습인것을 잠시 이름을 오픈하다는 정책을 사용해 없어지지 않을 것입니다. 처음 시행하게 되면 사람들이 인지를 하고 잠시 악성 댓글이 사라질지 모르나 사람들이 이런 시스템에 적응하게 되면 또다른 방식의 악성 댓글들이 올라오고 그로인해 상처 받는 사람들이 발생하여 지금보다 더한 문제에 직면하게 될 것이라고 생각합니다. 어떤 문제를 해결하기 위해 그들을 압박하거나 그들에게 공포의식을 심어주어 그만두게 하는 것은 올바른 해결책이 아니라고 생각합니다. 옛날 이솝우화에도 바람이 나그네의 옷을 벗기는지 햇님이 나그네의 옷을 벗기는지 내기를 할때 아무리 사나운 바람을 불어도 옷깃으 여미던 나그네가 따사로운 햇님 아래서 옷을 훌렁 벗었던 이야기와 같은 이치 입니다. 우리들은 압박과 공포 따위에 주저하고 포기하는 민족이 아니라는 것은 조선시대, 일제강점기, 민주화기 계속적으로 나타납니다. 지금의 범죄자들을 보더라도 강한 법적 제제를 가하더라도 그들은 또다른 지능적 방법으로 범죄를 또다시 저지르는 행태를 보입니다. 그래서 저는 이런 법적 제제가 문제가 아니라 문화의식을 바꿔야 한다고 생각합니다. 지금 우리 정부에서도 문화의식 향상을 위한 캠페인, 학교교육, 문화교육 등으로 인식 변화를 도모하고 있다고 생각합니다. 인식변화와 인격향상, 문화의식 향상 등의 교육을 통하여 우리는 변화되고 변화된 시민의식이 인터넷 문화를 개선시킬수 있는 원동력이 될것입니다. 만약 댓글에 악플러를 발견한다면 그들을 제지하는 다른 댓글러들이 동시에 제지하는 발언을 함으로써 악플러를 잠재워야 하며 그들이 잘못을 저지르고 있다는 사실을 인지시켜야 합니다. 그들이 느껴서 스스로 깨달을수 있도록 하는 것이 중요한것이지 실명제는 임시 제도에 불과하다고 생각합니다.

Output
-------------
{{
    "score": 9
    "reason": (생략)
}}

Inputs
------

Prompt:
보편적으로 인터넷에서 사용자는 자기의 본이름을 제외한 ID나 별명을 사용합니다. 즉, 익명을 사용하여 인터넷에서 활동하게 됩니다.\n\n 하지만, 인터넷에서는 이러한 점을 악용하는 사례가 무수히 생겨나고 있습니다. 사이버 세상에서 자신이 외부에 노출되어 있지 않다는 것을 이용해 자신과 다른 의견에 대해 욕설, 인신공격 등을 가하는 것이지요. 이에 대해 인터넷상에서의 규제는 사실상 불가능한 부분이 많습니다.\n\n 그 때문에 최근 인터넷 사이트에 회원가입을 할 때 본인 확인 절차를 거치지 않았으면 글 등을 올릴 때 본인 확인을 할 수 있도록 제한적 인터넷 실명제가 도입되고 있습니다.\n\n 하지만 인터넷의 가장 기본적인 속성인 익명성이 무시될 경우, 인터넷은 무한한 가능성의 공간이 아닌 제한적인 도구로 전락할 수도 있습니다.\n\n 제한적 인터넷 실명제는 필요한지 찬성과 반대를 선택하여 자신의 견해를 작성해주세요.

Essay:
실제로 연예인들 중에서는 이러한 악플로 인하여 자살을 하거나 우울증을 겪는 사례가 많이 있습니다. 유명인이라는 이유만으로 이러한 악플들을 감내해야 하는 것은 그들에게는 너무 잔혹한 일이 아닐 수 없습니다. 이처럼 아무 생각 없이, 혹은 재미삼아서, 남들도 하니까 라는 이유로 올린 글들이 누군가에게는 큰 상처가 될 수 있을 것입니다. 이러한 사회적인 문제를 해결하기 위해서는 제도적으로 악플이나 잘못된 정보를 제제해야 한다고 생각합니다. 그 방법은 바로 실명제를 도입하는 것입니다.

Output
-------------
{{
    "score": 2
    "reason": (생략)
}}

Now evaluate the essay step by step according to the **Plan-and-Solve** procedure above and output ONLY the final score as a single integer from 0 to 9.

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

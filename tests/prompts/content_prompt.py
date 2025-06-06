# tests/prompts/content_prompt.py

BASE_ZEROSHOT = """
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

COT_ZEROSHOT = """
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

PLAN_SOLVE_ZEROSHOT = """
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

BASE_ONESHOT = """
You are a strict and consistent writing evaluator. Respond ONLY with a single integer score between 0 and 9.
As a writing evaluator, your task is to assess the *content quality* of an essay.

Example Evaluation:

Inputs
------

Prompt:
보편적으로 인터넷에서 사용자는 자기의 본이름을 제외한 ID나 별명을 사용합니다. 즉, 익명을 사용하여 인터넷에서 활동하게 됩니다.\n\n 하지만, 인터넷에서는 이러한 점을 악용하는 사례가 무수히 생겨나고 있습니다. 사이버 세상에서 자신이 외부에 노출되어 있지 않다는 것을 이용해 자신과 다른 의견에 대해 욕설, 인신공격 등을 가하는 것이지요. 이에 대해 인터넷상에서의 규제는 사실상 불가능한 부분이 많습니다.\n\n 그 때문에 최근 인터넷 사이트에 회원가입을 할 때 본인 확인 절차를 거치지 않았으면 글 등을 올릴 때 본인 확인을 할 수 있도록 제한적 인터넷 실명제가 도입되고 있습니다.\n\n 하지만 인터넷의 가장 기본적인 속성인 익명성이 무시될 경우, 인터넷은 무한한 가능성의 공간이 아닌 제한적인 도구로 전락할 수도 있습니다.\n\n 제한적 인터넷 실명제는 필요한지 찬성과 반대를 선택하여 자신의 견해를 작성해주세요.

Essay:
일단 인터넷상에서의 실명제는 이뤄지면 안된다고 생각한다. 인타넷상에서 실명제가 가능해진다면 내가 말할수있는 표현의 자유가 침해된다고 생각한다. 누구나 의견을 내고, 찬성하고 반대하는 의견을 표현할 권리가 있는데 인터넷 실명제가 도입된다면, 의견표출에 소심해질 수밖에 없다. 반대의견을 표현했다는 이유로 후에 일어날 보복이나 손해 등을 고려하다 보면 표현의 자유는 침해당하고 만다. 그리고 막상 인터넷 실명제를 도입한다거 해서 악성댓글이 멈추는것은 아니다. 페이스북 같이 자신의 이름과 얼굴이 노출된 상태에서도 사람들의 악성 댓글은 멈추지 않았다. 악성 댓글을 다는 사람들은 자신의 얼굴과 이름이 노출 되면서도 상대방에게 모욕적인 댓글이나 명예훼손을 하는 댓글들을 부끄러워하지 않고 막 달고 있으며 잘못된 일임 조차도 잘 알지 못했다. 그리고 인터넷 실명제를 실시하면 개인 정보 유출로 인해 또 다른 범죄가 발생한다. 보안 시스템이 허술 할 경우 해킹으로 주민등록번호가 유출될 가능성이 매우 높다. 실제로 인터넷 실명제를 도입하였을때 대한민국 인터넷 사이트는 많은 해킹 시도를 받았다. 악성댓글이나 허위정보 유출 등을 실명제를 통해 강제로 규제 하는것이 아니라, 건전한 인터넷 문화를 만들기 위한 교육에 더 힘을 써야한다. 사이버 범죄의 처벌을 더 강화하고 범죄 예방과 교육에 더 노력하다 보면 건전한 인터넷 문화가 형성될 것이다. 이렇게 실명제를 실시하지 않아도 악플수를 줄일수 있는 방법들은 무긍무진하게 많다. 그러니 꼭 개인정보 유출이 의심되면서 불안하게 개인의 자유를 침해할바엔 그냥 위에서 얘기한거와 같이 다른 방법들을 추구하여 하는게 훨 더 나은 결과를 불러올수있을거라 생각하고 시민의식이 스스로 강해져야 결과가 더 좋을거라고 생각한다.

Output
-------------
9

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

COT_ONESHOT = """
You are a strict and consistent writing evaluator. Respond ONLY with a single integer score between 0 and 9.
As a writing evaluator, your task is to assess the *content quality* of an essay.

Use the following three criteria to evaluate content quality. For each criterion, assign a score from 0 to 3:

1. Clarity of Topic: Is the main idea of the essay clear? Does the essay stay focused on the topic throughout?
2. Specificity of Explanation: Are the explanations detailed and specific? Does the writer explore the topic in diverse and concrete ways?
3. Creativity of Thought: Does the essay demonstrate unique and logical insight into the topic? Does it attempt new ideas or shifts in perspective?

Think step by step to evaluate each of the three criteria, assign an integer total score (0~9) 

IMPORTANT: Only output a single integer from 0 to 9 at the end.

Example Evaluation:

Inputs
------

Prompt:
보편적으로 인터넷에서 사용자는 자기의 본이름을 제외한 ID나 별명을 사용합니다. 즉, 익명을 사용하여 인터넷에서 활동하게 됩니다.\n\n 하지만, 인터넷에서는 이러한 점을 악용하는 사례가 무수히 생겨나고 있습니다. 사이버 세상에서 자신이 외부에 노출되어 있지 않다는 것을 이용해 자신과 다른 의견에 대해 욕설, 인신공격 등을 가하는 것이지요. 이에 대해 인터넷상에서의 규제는 사실상 불가능한 부분이 많습니다.\n\n 그 때문에 최근 인터넷 사이트에 회원가입을 할 때 본인 확인 절차를 거치지 않았으면 글 등을 올릴 때 본인 확인을 할 수 있도록 제한적 인터넷 실명제가 도입되고 있습니다.\n\n 하지만 인터넷의 가장 기본적인 속성인 익명성이 무시될 경우, 인터넷은 무한한 가능성의 공간이 아닌 제한적인 도구로 전락할 수도 있습니다.\n\n 제한적 인터넷 실명제는 필요한지 찬성과 반대를 선택하여 자신의 견해를 작성해주세요.

Essay:
일단 인터넷상에서의 실명제는 이뤄지면 안된다고 생각한다. 인타넷상에서 실명제가 가능해진다면 내가 말할수있는 표현의 자유가 침해된다고 생각한다. 누구나 의견을 내고, 찬성하고 반대하는 의견을 표현할 권리가 있는데 인터넷 실명제가 도입된다면, 의견표출에 소심해질 수밖에 없다. 반대의견을 표현했다는 이유로 후에 일어날 보복이나 손해 등을 고려하다 보면 표현의 자유는 침해당하고 만다. 그리고 막상 인터넷 실명제를 도입한다거 해서 악성댓글이 멈추는것은 아니다. 페이스북 같이 자신의 이름과 얼굴이 노출된 상태에서도 사람들의 악성 댓글은 멈추지 않았다. 악성 댓글을 다는 사람들은 자신의 얼굴과 이름이 노출 되면서도 상대방에게 모욕적인 댓글이나 명예훼손을 하는 댓글들을 부끄러워하지 않고 막 달고 있으며 잘못된 일임 조차도 잘 알지 못했다. 그리고 인터넷 실명제를 실시하면 개인 정보 유출로 인해 또 다른 범죄가 발생한다. 보안 시스템이 허술 할 경우 해킹으로 주민등록번호가 유출될 가능성이 매우 높다. 실제로 인터넷 실명제를 도입하였을때 대한민국 인터넷 사이트는 많은 해킹 시도를 받았다. 악성댓글이나 허위정보 유출 등을 실명제를 통해 강제로 규제 하는것이 아니라, 건전한 인터넷 문화를 만들기 위한 교육에 더 힘을 써야한다. 사이버 범죄의 처벌을 더 강화하고 범죄 예방과 교육에 더 노력하다 보면 건전한 인터넷 문화가 형성될 것이다. 이렇게 실명제를 실시하지 않아도 악플수를 줄일수 있는 방법들은 무긍무진하게 많다. 그러니 꼭 개인정보 유출이 의심되면서 불안하게 개인의 자유를 침해할바엔 그냥 위에서 얘기한거와 같이 다른 방법들을 추구하여 하는게 훨 더 나은 결과를 불러올수있을거라 생각하고 시민의식이 스스로 강해져야 결과가 더 좋을거라고 생각한다.

Output
-------------
9

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

PLAN_SOLVE_ONESHOT = """
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

Example Evaluation:

Inputs
------

Prompt:
보편적으로 인터넷에서 사용자는 자기의 본이름을 제외한 ID나 별명을 사용합니다. 즉, 익명을 사용하여 인터넷에서 활동하게 됩니다.\n\n 하지만, 인터넷에서는 이러한 점을 악용하는 사례가 무수히 생겨나고 있습니다. 사이버 세상에서 자신이 외부에 노출되어 있지 않다는 것을 이용해 자신과 다른 의견에 대해 욕설, 인신공격 등을 가하는 것이지요. 이에 대해 인터넷상에서의 규제는 사실상 불가능한 부분이 많습니다.\n\n 그 때문에 최근 인터넷 사이트에 회원가입을 할 때 본인 확인 절차를 거치지 않았으면 글 등을 올릴 때 본인 확인을 할 수 있도록 제한적 인터넷 실명제가 도입되고 있습니다.\n\n 하지만 인터넷의 가장 기본적인 속성인 익명성이 무시될 경우, 인터넷은 무한한 가능성의 공간이 아닌 제한적인 도구로 전락할 수도 있습니다.\n\n 제한적 인터넷 실명제는 필요한지 찬성과 반대를 선택하여 자신의 견해를 작성해주세요.

Essay:
일단 인터넷상에서의 실명제는 이뤄지면 안된다고 생각한다. 인타넷상에서 실명제가 가능해진다면 내가 말할수있는 표현의 자유가 침해된다고 생각한다. 누구나 의견을 내고, 찬성하고 반대하는 의견을 표현할 권리가 있는데 인터넷 실명제가 도입된다면, 의견표출에 소심해질 수밖에 없다. 반대의견을 표현했다는 이유로 후에 일어날 보복이나 손해 등을 고려하다 보면 표현의 자유는 침해당하고 만다. 그리고 막상 인터넷 실명제를 도입한다거 해서 악성댓글이 멈추는것은 아니다. 페이스북 같이 자신의 이름과 얼굴이 노출된 상태에서도 사람들의 악성 댓글은 멈추지 않았다. 악성 댓글을 다는 사람들은 자신의 얼굴과 이름이 노출 되면서도 상대방에게 모욕적인 댓글이나 명예훼손을 하는 댓글들을 부끄러워하지 않고 막 달고 있으며 잘못된 일임 조차도 잘 알지 못했다. 그리고 인터넷 실명제를 실시하면 개인 정보 유출로 인해 또 다른 범죄가 발생한다. 보안 시스템이 허술 할 경우 해킹으로 주민등록번호가 유출될 가능성이 매우 높다. 실제로 인터넷 실명제를 도입하였을때 대한민국 인터넷 사이트는 많은 해킹 시도를 받았다. 악성댓글이나 허위정보 유출 등을 실명제를 통해 강제로 규제 하는것이 아니라, 건전한 인터넷 문화를 만들기 위한 교육에 더 힘을 써야한다. 사이버 범죄의 처벌을 더 강화하고 범죄 예방과 교육에 더 노력하다 보면 건전한 인터넷 문화가 형성될 것이다. 이렇게 실명제를 실시하지 않아도 악플수를 줄일수 있는 방법들은 무긍무진하게 많다. 그러니 꼭 개인정보 유출이 의심되면서 불안하게 개인의 자유를 침해할바엔 그냥 위에서 얘기한거와 같이 다른 방법들을 추구하여 하는게 훨 더 나은 결과를 불러올수있을거라 생각하고 시민의식이 스스로 강해져야 결과가 더 좋을거라고 생각한다.

Output
-------------
9

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
# tests/prompts/coherence_prompt.py

BASE_ZEROSHOT = """
You are a strict and consistent writing evaluator. Respond ONLY with a single integer score between 0 and 9.
As a writing evaluator, your task is to assess the *coherence quality* of an essay.

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
As a writing evaluator, your task is to assess the *coherence quality* of an essay.

Use the following three criteria to evaluate content quality. For each criterion, assign a score from 0 to 3:

1. Paragraph Structure: Are topic sentences clear and well supported within each paragraph? Are the ideas logically connected?
2. Overall Essay Structure: Does the essay follow a clear introduction-body-conclusion format, even if it's in a single paragraph?
3. Logical Flow and Transitions: Are ideas and paragraphs smoothly connected using transitions? Is the flow of the essay logical and easy to follow?

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
As a writing evaluator, your task is to assess the *coherence quality* of an essay.

We will use a **Plan-and-Solve** approach:

## PLAN ##
Step 1: Evaluate the Paragraph Structure.
- Check if topic sentences are clear and well supported within each paragraph.
- Determine whether the ideas in each paragraph are logically connected.
- Assign a score from 0 to 3.

Step 2: Evaluate the Overall Essay Structure.
- Determine if the essay follows a clear introduction-body-conclusion structure, even if it's presented in one paragraph.
- Evaluate whether each part (intro, body, conclusion) is balanced and appropriate.
- Assign a score from 0 to 3.

Step 3: Evaluate Logical Flow and Transitions.
- Check if sentences and paragraphs are connected smoothly.
- Look for appropriate use of transition words and consistent logical flow throughout.
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
As a writing evaluator, your task is to assess the *coherence quality* of an essay.

Example Evaluation:

Inputs
------

Prompt:
보편적으로 인터넷에서 사용자는 자기의 본이름을 제외한 ID나 별명을 사용합니다. 즉, 익명을 사용하여 인터넷에서 활동하게 됩니다.\n\n 하지만, 인터넷에서는 이러한 점을 악용하는 사례가 무수히 생겨나고 있습니다. 사이버 세상에서 자신이 외부에 노출되어 있지 않다는 것을 이용해 자신과 다른 의견에 대해 욕설, 인신공격 등을 가하는 것이지요. 이에 대해 인터넷상에서의 규제는 사실상 불가능한 부분이 많습니다.\n\n 그 때문에 최근 인터넷 사이트에 회원가입을 할 때 본인 확인 절차를 거치지 않았으면 글 등을 올릴 때 본인 확인을 할 수 있도록 제한적 인터넷 실명제가 도입되고 있습니다.\n\n 하지만 인터넷의 가장 기본적인 속성인 익명성이 무시될 경우, 인터넷은 무한한 가능성의 공간이 아닌 제한적인 도구로 전락할 수도 있습니다.\n\n 제한적 인터넷 실명제는 필요한지 찬성과 반대를 선택하여 자신의 견해를 작성해주세요.

Essay:
저는 인터넷 실명제가 매우 필요하다고 생각합니다. 실명제를 반대하는 사람들은 이렇게 말합니다. 익명서잉 무시되는 경우 인터넷이 무한한 가능성을 잃어버리고 제한을 당해버리는 공간으로 전락해버린다고 말입니다. 그런데 저는 생각이 완전히 다릅니다. 대체 댓글에 무슨 말을 달려고 하길래 무한한 가능성으로 그러한 것들을 표현하는 것일까요? 실명제를 하게 되면 자신의 의견을 말하더라고 상대에게 상처를 주거나 아픔을 주는 일이 절대 없을 것입니다. 댓글은 누군가를 비방하고 깎아내리려고 하는 것이 아니라 사람들에게 자신의 의견을 말해보고 또 그 의견에 대한 다른사람의 의견도 들어보면서 서로 소통하는 그런 공간입니다. 그런데 그런공간에서 다른사람을 비방하기나하고 다른사람을 욕하기만 한다면 그게 어떻게 소통일까요? 저는 그래서 자신이 정말 다른사람에게 그런 심한말을 하지않고 그런 다른사람의 인격을 깎는 그런 행위를 하는 사람이 아니라면 당연하게도 실명제에 찬성해야 한다고 생각합니다. 저는 자신의 의견을 솔직하게 당당하게 제시하려면 당연하게 실명제가 좋다고 생각합니다. 물론 실명제가 있으면 누군가에게 공격을 당할 수 있습니다. 그러나 그 사람 조차도 실명제를 사용해야 하기에 그 사람의 신상과 그 사람이 한 행동을 모두 박제 시켜버릴 수 있는 것 이지요. 그래서 경찰들도 누군가에게 상처를 준사람을 찾기 쉬워질 것이고 덕분에 사람들 모두가 서로를 존중하고 서로의 의견을 잘 들어주는 멋진 관계로 성장하게 될 것입니다. 사람들이 자신만 생각하는게 아니라 다른사람을 존중하면서 댓글을 달 수있게하는 그런 제도인 인터넷 실명제를 저는 적극 찬성하는 바입니다. 그리고 실명제를 해서도 누군가에게 상처를 주는 말을 하는 사람이 있다면 반드시 잡아내어 벌을 크게 주어야지 다른 사람도 그것을 보고 다시는 그런일을 하지 못하게 할 수 있다고 생각합니다.

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
As a writing evaluator, your task is to assess the *coherence quality* of an essay.

Use the following three criteria to evaluate content quality. For each criterion, assign a score from 0 to 3:

1. Paragraph Structure: Are topic sentences clear and well supported within each paragraph? Are the ideas logically connected?
2. Overall Essay Structure: Does the essay follow a clear introduction-body-conclusion format, even if it's in a single paragraph?
3. Logical Flow and Transitions: Are ideas and paragraphs smoothly connected using transitions? Is the flow of the essay logical and easy to follow?

Think step by step to evaluate each of the three criteria, assign an integer total score (0~9) 

IMPORTANT: Only output a single integer from 0 to 9 at the end.

Example Evaluation:

Inputs
------

Prompt:
보편적으로 인터넷에서 사용자는 자기의 본이름을 제외한 ID나 별명을 사용합니다. 즉, 익명을 사용하여 인터넷에서 활동하게 됩니다.\n\n 하지만, 인터넷에서는 이러한 점을 악용하는 사례가 무수히 생겨나고 있습니다. 사이버 세상에서 자신이 외부에 노출되어 있지 않다는 것을 이용해 자신과 다른 의견에 대해 욕설, 인신공격 등을 가하는 것이지요. 이에 대해 인터넷상에서의 규제는 사실상 불가능한 부분이 많습니다.\n\n 그 때문에 최근 인터넷 사이트에 회원가입을 할 때 본인 확인 절차를 거치지 않았으면 글 등을 올릴 때 본인 확인을 할 수 있도록 제한적 인터넷 실명제가 도입되고 있습니다.\n\n 하지만 인터넷의 가장 기본적인 속성인 익명성이 무시될 경우, 인터넷은 무한한 가능성의 공간이 아닌 제한적인 도구로 전락할 수도 있습니다.\n\n 제한적 인터넷 실명제는 필요한지 찬성과 반대를 선택하여 자신의 견해를 작성해주세요.

Essay:
저는 인터넷 실명제가 매우 필요하다고 생각합니다. 실명제를 반대하는 사람들은 이렇게 말합니다. 익명서잉 무시되는 경우 인터넷이 무한한 가능성을 잃어버리고 제한을 당해버리는 공간으로 전락해버린다고 말입니다. 그런데 저는 생각이 완전히 다릅니다. 대체 댓글에 무슨 말을 달려고 하길래 무한한 가능성으로 그러한 것들을 표현하는 것일까요? 실명제를 하게 되면 자신의 의견을 말하더라고 상대에게 상처를 주거나 아픔을 주는 일이 절대 없을 것입니다. 댓글은 누군가를 비방하고 깎아내리려고 하는 것이 아니라 사람들에게 자신의 의견을 말해보고 또 그 의견에 대한 다른사람의 의견도 들어보면서 서로 소통하는 그런 공간입니다. 그런데 그런공간에서 다른사람을 비방하기나하고 다른사람을 욕하기만 한다면 그게 어떻게 소통일까요? 저는 그래서 자신이 정말 다른사람에게 그런 심한말을 하지않고 그런 다른사람의 인격을 깎는 그런 행위를 하는 사람이 아니라면 당연하게도 실명제에 찬성해야 한다고 생각합니다. 저는 자신의 의견을 솔직하게 당당하게 제시하려면 당연하게 실명제가 좋다고 생각합니다. 물론 실명제가 있으면 누군가에게 공격을 당할 수 있습니다. 그러나 그 사람 조차도 실명제를 사용해야 하기에 그 사람의 신상과 그 사람이 한 행동을 모두 박제 시켜버릴 수 있는 것 이지요. 그래서 경찰들도 누군가에게 상처를 준사람을 찾기 쉬워질 것이고 덕분에 사람들 모두가 서로를 존중하고 서로의 의견을 잘 들어주는 멋진 관계로 성장하게 될 것입니다. 사람들이 자신만 생각하는게 아니라 다른사람을 존중하면서 댓글을 달 수있게하는 그런 제도인 인터넷 실명제를 저는 적극 찬성하는 바입니다. 그리고 실명제를 해서도 누군가에게 상처를 주는 말을 하는 사람이 있다면 반드시 잡아내어 벌을 크게 주어야지 다른 사람도 그것을 보고 다시는 그런일을 하지 못하게 할 수 있다고 생각합니다.

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
As a writing evaluator, your task is to assess the *coherence quality* of an essay.

We will use a **Plan-and-Solve** approach:

## PLAN ##

Evaluate the essay using the following three criteria, assigning a score from 0 to 3 for each:

Step 1. Evaluate **Intra-paragraph Structure Appropriateness**
- 3: Each paragraph has a clear topic sentence and supporting sentences that are logically connected.
- 2: Most paragraphs are organized with a topic sentence and supporting details, but some connections may be weak.
- 1: Paragraphs show inconsistent structure; topic and supporting sentences are not clearly connected.
- 0: Paragraphs lack internal structure; sentences appear randomly placed without logical progression.

Step 2. Evaluate **Inter-paragraph Structure Appropriateness**
- 3: The essay clearly follows a three-part structure (introduction, body, conclusion), even if it is in a single paragraph. Each part has an appropriate amount of content.
- 2: The essay mostly follows the three-part structure; minor imbalance or unclear boundaries between parts.
- 1: The structure is attempted but poorly executed; one or more parts (intro, body, conclusion) are missing or underdeveloped.
- 0: No recognizable structure; ideas are presented without clear sectional separation.

Step3. Evaluate **Structural Consistency and Logical Flow**
- 3: Sentences and paragraphs are connected smoothly using appropriate linking words and transitions; logical flow is strong throughout.
- 2: Some transitions are used; overall logical flow is maintained but not always smooth.
- 1: Limited or awkward use of transitions; the flow of ideas is sometimes unclear or inconsistent.
- 0: Sentences and ideas are disjointed; lack of transitions severely affects readability.

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
저는 인터넷 실명제가 매우 필요하다고 생각합니다. 실명제를 반대하는 사람들은 이렇게 말합니다. 익명서잉 무시되는 경우 인터넷이 무한한 가능성을 잃어버리고 제한을 당해버리는 공간으로 전락해버린다고 말입니다. 그런데 저는 생각이 완전히 다릅니다. 대체 댓글에 무슨 말을 달려고 하길래 무한한 가능성으로 그러한 것들을 표현하는 것일까요? 실명제를 하게 되면 자신의 의견을 말하더라고 상대에게 상처를 주거나 아픔을 주는 일이 절대 없을 것입니다. 댓글은 누군가를 비방하고 깎아내리려고 하는 것이 아니라 사람들에게 자신의 의견을 말해보고 또 그 의견에 대한 다른사람의 의견도 들어보면서 서로 소통하는 그런 공간입니다. 그런데 그런공간에서 다른사람을 비방하기나하고 다른사람을 욕하기만 한다면 그게 어떻게 소통일까요? 저는 그래서 자신이 정말 다른사람에게 그런 심한말을 하지않고 그런 다른사람의 인격을 깎는 그런 행위를 하는 사람이 아니라면 당연하게도 실명제에 찬성해야 한다고 생각합니다. 저는 자신의 의견을 솔직하게 당당하게 제시하려면 당연하게 실명제가 좋다고 생각합니다. 물론 실명제가 있으면 누군가에게 공격을 당할 수 있습니다. 그러나 그 사람 조차도 실명제를 사용해야 하기에 그 사람의 신상과 그 사람이 한 행동을 모두 박제 시켜버릴 수 있는 것 이지요. 그래서 경찰들도 누군가에게 상처를 준사람을 찾기 쉬워질 것이고 덕분에 사람들 모두가 서로를 존중하고 서로의 의견을 잘 들어주는 멋진 관계로 성장하게 될 것입니다. 사람들이 자신만 생각하는게 아니라 다른사람을 존중하면서 댓글을 달 수있게하는 그런 제도인 인터넷 실명제를 저는 적극 찬성하는 바입니다. 그리고 실명제를 해서도 누군가에게 상처를 주는 말을 하는 사람이 있다면 반드시 잡아내어 벌을 크게 주어야지 다른 사람도 그것을 보고 다시는 그런일을 하지 못하게 할 수 있다고 생각합니다.

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
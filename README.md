# EssayEval: LLM 기반 에세이 생성 및 요약 평가 시스템

LLM(Large Language Model)을 활용하여 에세이를 생성하거나 요약한 후, 해당 결과물을 다양한 기준으로 평가하는 웹 기반 애플리케이션.  
Streamlit 기반 UI와 LangChain 평가 체인을 활용하며, 에세이의 **내용, 일관성, 유창성, 환각 여부, 글자 수 충족 여부**를 자동으로 분석함.

---

## 주요 기능

### 1. 에세이 생성 및 평가
- 프롬프트를 기반으로 LLM이 에세이 생성
- 다음 항목에 대한 자동 평가 수행:
  - 내용 (Content)
  - 일관성 (Coherence)
  - 유창성 (Fluency)
  - 글자 수 기준 충족 여부 (Length)

### 2. 에세이 요약 및 평가
- 원본 에세이를 요약한 후 다음 항목 평가:
  - 내용 (Content)
  - 일관성 (Coherence)
  - 유창성 (Fluency)
  - 환각 여부 (Hallucination)
  - 글자 수 기준 충족 여부 (Length)

### 3. 평가 기록 관리
- 평가 결과와 생성 텍스트를 `session_state.history`에 저장하여 UI에서 열람 가능

---

## 사용 기술

- **Frontend**: Streamlit
- **LLM 호출 및 평가 파이프라인**: LangChain
- **에세이 생성/요약용 모델**:
  - `gpt-4o`, `gpt-4.1`, `gemini-2.0-flash`, `gemma2-9b-it`, `llama-3.1-8b-instant`
- **에세이 평가 모델**: `gpt-4.1` (모든 항목 평가에 고정 사용)

---

## 실행 방법

### 1. 환경 설정
```bash
conda create -n essay-eval python=3.10
conda activate essay-eval
pip install -r requirements.txt
```

### 2. `.env` 파일 생성
루트 디렉토리에 `.env` 파일을 만들고 다음 내용 입력:
```
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
ESSAY_DATASET_DIR=./data/essay
HALLU_DATASET_PATH=./data/hallucination.jsonl
```

### 3. 실행
```bash
streamlit run app/main.py
```

---

## 평가 항목 설명

| 항목         | 설명                                                                 |
|--------------|----------------------------------------------------------------------|
| Content      | 주제 명확성, 설명 구체성, 창의적 사고 여부                         |
| Coherence    | 단락 구성, 글 전체 구조, 논리적 흐름                                |
| Fluency      | 문법 정확도, 어휘 적절성, 문장 구조 다양성                         |
| Hallucination| 요약이 원문에 없는 허위 정보를 포함하는지 여부                     |
| Length       | 사용자가 지정한 글자 수 기준 충족 여부                              |

---

## 평가 정확도 검증 및 프롬프팅 실험

`tests/` 디렉토리는 LLM 평가 결과의 일관성과 정확도를 검증하기 위한 실험 코드로 구성됨.  
여기서는 다양한 프롬프팅 방식에 따른 평가 결과와 인간 평가 점수 간의 **스피어만 상관계수** 및 **이진 분류 성능**을 측정함.

### 실험용 프롬프트 구성
- `tests/prompts/` 디렉토리에는 세 가지 프롬프트 유형이 존재함:
  - `BASE`: 단순한 평가 요청
  - `COT` (Chain-of-Thought): 사고 절차 유도
  - `PLAN_SOLVE`: 평가 계획 수립 후 실행

프롬프트는 실험 코드 내부에서 다음과 같이 변경 가능 (Coherence, Content, Fluency):
```python
# BASE 방식
prompt = ChatPromptTemplate.from_template({metric}_prompt.BASE_ZEROSHOT)

# COT 방식
prompt = ChatPromptTemplate.from_template({metric}_prompt.COT_ZEROSHOT)

# Plan-and-Solve 방식
prompt = ChatPromptTemplate.from_template({metric}_prompt.PLAN_SOLVE_ZEROSHOT)
```

### 실행 예시
```bash
python tests/coherence.py       # Coherence 평가 상관계수 측정
python tests/content.py         # Content 평가 상관계수 측정
python tests/fluency.py         # Fluency 평가 상관계수 측정
python tests/hallucination.py   # Hallucination 평가 정확도, 정밀도, 재현율, F1
```

---

## 프로젝트 구조

```
app/
 ├── main.py
 └── ui/
     ├── generation_eval.py
     ├── summary_eval.py
     └── history.py

evaluators/
 ├── content.py
 ├── coherence.py
 ├── fluency.py
 ├── hallucination.py
 └── length.py

prompts/
 ├── content_prompt.py
 ├── coherence_prompt.py
 ├── fluency_prompt.py
 ├── hallucination_prompt.py
 └── generation_prompt.py      # 앱에서 실제 사용하는 생성/요약 프롬프트

tests/
 ├── content.py
 ├── coherence.py
 ├── fluency.py
 ├── hallucination.py
 └── prompts/
     ├── content_prompt.py
     ├── coherence_prompt.py
     ├── fluency_prompt.py
     └── hallucination_prompt.py

llm_tasks.py
config.py
```

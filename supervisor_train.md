# Supervisor–Subagent Training with GRPO
# Basically a MAX_step = 1 supervisor multigent, where we finetune the supervisor by the answer correctness

This project fine-tunes a **supervisor agent** using **Group Relative Policy Optimization (GRPO)** to route biomedical questions from the **PubMedQA** dataset to specialized **sub-agents**. The reward signal is based on the correctness of the final *yes/no* answer produced by the sub-agents.

---

## 📂 Dataset Preparation

- **Input Data**: CSV (`pubmedqa_30.csv`) with fields:
  - `context`: biomedical abstract/snippet
  - `question`: yes/no clinical question
  - `final_decision`: gold label (`yes` / `no`)

- **Formatting**:
  ```python
  {
      "problem": row["question"],
      "context": row["context"],
      "prompt": <SYSTEM_PROMPT + user_content>,
      "answer": row["final_decision"]
  }


## 🧑‍🏫 Supervisor Agent

**Role**: Reads the problem + context, then chooses the next agent:

- `question_understanding`
- `context_analysis`
- `reasoning`
- `answering`

**System Prompt**:

Given the problem and context, please choose ONE next agent to call
from: question_understanding, context_analysis, reasoning, answering.

Reply STRICTLY in the form:
Agent: <name>
Then explain why.



---

## 🤖 Sub-Agents

Each sub-agent is run via **Ollama** (`/api/chat`) with its own system prompt:

- **question_understanding** → clarify the exact question  
- **context_analysis** → extract key facts  
- **reasoning** → perform step-by-step reasoning  
- **answering** → output `<answer>yes</answer>` or `<answer>no</answer>`

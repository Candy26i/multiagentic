import utils

# Set up the call_model function - you can change this to use different models
def setup_model(model_type="ollama", **kwargs):
    """Setup the model for agent calls"""
    global call_model
    if model_type == "ollama":
        model = utils.Ollama(**kwargs)
        call_model = model.call_model
    elif model_type == "textgenwebui":
        model = utils.Textgenwebui(**kwargs)
        call_model = model.call_model
    else:
        raise ValueError(f"Unknown model type: {model_type}")

# Default setup - you can change this
setup_model("ollama", model="qwen2.5:7b")

def problem_understanding_agent(state, history):
    prompt = f"""You are the problem_understanding agent.

Your job is to understand the math problem below and extract the relevant components.

Problem:
{state['problem']}
"""
    extended_history = history + [{"role": "user", "content": prompt}]
    return call_model(extended_history)


def mathematical_formulation_agent(state, history):
    prompt = f"""You are the mathematical_formulation agent.

Based on the given problem, translate it into a solvable mathematical equation or formula.

Problem:
{state['problem']}
"""
    extended_history = history + [{"role": "user", "content": prompt}]
    return call_model(extended_history)


def computation_agent(state, history):
    prompt = f"""You are the computation agent.

Solve the following math problem using the formulated equation or method.
Focus on performing the necessary computations to arrive at the correct final answer.

Problem:
{state['problem']}

"""
    extended_history = history + [{"role": "user", "content": prompt}]
    return call_model(extended_history)

def answering_agent(state, history):
    context = state.get('context', None)
    if context is not None:
        prompt = f"""You are the answering agent.

Based on all the prior reasoning and context, provide a clear final answer to the question.
Answer strictly in the form of: Yes, No, or Maybe

Question:
{state['problem']}
Context:
{state['context']}

Provide your answer in one word.
"""
    else:
        prompt = f"""You are the answering agent.

Based on all the prior reasoning and context, provide the final answer to the math problem.
Answer strictly in the format : \nAnswer: <A/B/C/D/E>\n. ONLY give the final letter answer, no explanation.

Problem:
{state['problem']}

Options:
{state['options']} 

"""
    extended_history = history + [{"role": "user", "content": prompt}]
    return call_model(extended_history)
    
def problem_understanding_agent(state, history):
    prompt = f"""You are the problem_understanding agent.

Your job is to understand the math problem below and extract the relevant components.

Problem:
{state['problem']}
"""
    extended_history = history + [{"role": "user", "content": prompt}]
    return call_model(extended_history)



def knowledge_grounding_agent(state, history):
    prompt = f"""You are the knowledge_grounding agent.

Your job is to verify that the reasoning steps and retrieved context are consistent with established physical laws and principles.
Highlight any inconsistencies or confirm alignment with known physics.

Question:
{state['problem']}
Options:
{state['options']}
"""
    extended_history = history + [{"role": "user", "content": prompt}]
    # history.append({"role": "user", "content": prompt})
    return call_model(extended_history)



def option_elimination_agent(state, history):
    prompt = f"""You are the option_elimination agent.

Based on reasoning and known physics, eliminate implausible or incorrect options. Provide brief justifications.

Question:
{state['problem']}
Options:
{state['options']}
"""
    extended_history = history + [{"role": "user", "content": prompt}]
    return call_model(extended_history)



def question_understanding_agent(state, history):
    prompt = f"""You are the question_understanding agent.

Your job is to understand the question below and extract what is being asked.

Question:
{state['problem']}
"""
    extended_history = history + [{"role": "user", "content": prompt}]
    return call_model(extended_history)


def context_analysis_agent(state, history):
    prompt = f"""You are the context_analysis agent.

Analyze the following context in relation to the question.

Context:
{state['context']}
Question:
{state['problem']}
"""
    extended_history = history + [{"role": "user", "content": prompt}]
    return call_model(extended_history)


def reasoning_agent(state, history):
    prompt = f"""You are the reasoning agent.

Using the question and context, reason out the answer in a logical way.

Context:
{state['context']}
Question:
{state['problem']}
"""
    extended_history = history + [{"role": "user", "content": prompt}]
    return call_model(extended_history)




AGENT_FUNCTIONS = {
    "knowledge_grounding": knowledge_grounding_agent,
    "option_elimination": option_elimination_agent,
    "answering": answering_agent,
    "problem_understanding": problem_understanding_agent,
    "mathematical_formulation": mathematical_formulation_agent,
    "computation": computation_agent,
    "question_understanding": question_understanding_agent,
    "context_analysis": context_analysis_agent,
    "reasoning": reasoning_agent,

}


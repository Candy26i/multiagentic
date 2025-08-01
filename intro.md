# Math QA Multi-Agent System

A refined multi-agent system for solving mathematical problems using hierarchical and supervisor architectures.

## Overview

This project implements a sophisticated multi-agent system for mathematical problem solving, featuring:

- **Multiple specialized agents** for different aspects of problem solving
- **Hierarchical architecture** for coordinated agent execution
- **Supervisor architecture** for oversight and quality control
- **Robust error handling** and type safety
- **Flexible model integration** (Ollama, Text Generation WebUI)

## Key Improvements Made

### 1. Code Structure and Organization
- **Removed duplicate functions** in `subagents.py`
- **Added proper type hints** throughout the codebase
- **Implemented comprehensive error handling**
- **Added detailed docstrings** for all functions and classes

### 2. Enhanced Functionality
- **Safe dictionary access** using `.get()` method to prevent KeyError
- **Consistent naming conventions** (PascalCase for classes, snake_case for functions)
- **Modular design** with clear separation of concerns
- **Factory pattern** for model creation

### 3. Architecture Improvements
- **Hierarchical class** with full agent management capabilities
- **Supervisor architecture** for multi-hierarchy coordination
- **Flexible agent sequences** that can be customized per use case
- **History management** for conversation tracking

## File Structure

```
math_qa_test/
├── subagents.py          # Agent implementations and Subagents class
├── model.py              # Model integration (Ollama, Text Generation WebUI)
├── Architecture.py       # Hierarchical and Supervisor architectures
├── example_usage.py      # Usage examples and demonstrations
├── requirements.txt      # Python dependencies
├── README.md            # This documentation
└── *.ipynb              # Jupyter notebooks for experiments
```

## Available Agents

| Agent Type | Purpose |
|------------|---------|
| `problem_understanding` | Extract key components from math problems |
| `mathematical_formulation` | Translate problems into equations |
| `computation` | Perform mathematical calculations |
| `answering` | Provide final answers in required format |
| `knowledge_grounding` | Verify reasoning against physical laws |
| `option_elimination` | Eliminate implausible answer options |
| `question_understanding` | Understand and parse questions |

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Basic Usage
```python
from model import Ollama
from subagents import Subagents

# Create model and agent
model = Ollama("qwen2.5:7b")
agent = Subagents("problem_understanding")

# Define problem
state = {"problem": "If 2x + 3 = 11, what is x?"}

# Get response
response = agent.call_subagent(state, [])
print(response)
```

### 3. Hierarchical Architecture
```python
from Architecture import Hierarchical

# Create hierarchy
hierarchy = Hierarchical(model)

# Set agent sequence
hierarchy.set_agent_sequence([
    "problem_understanding",
    "mathematical_formulation",
    "computation",
    "answering"
])

# Execute
results = hierarchy.execute_sequence(state)
```

### 4. Supervisor Architecture
```python
from Architecture import SupervisorArchitecture

# Create supervisor
supervisor = SupervisorArchitecture(model)

# Add hierarchies
supervisor.add_hierarchy("math_solver", math_hierarchy)
supervisor.add_hierarchy("physics_solver", physics_hierarchy)

# Supervise execution
result = supervisor.supervise_execution(state, "math_solver")
```

## Model Integration

### Ollama
```python
from model import Ollama

model = Ollama("qwen2.5:7b")  # or any other model
```

### Text Generation WebUI
```python
from model import Textgenwebui

model = Textgenwebui(port=5000)  # adjust port as needed
```

### Factory Pattern
```python
from model import ModelFactory

model = ModelFactory.create_model("ollama", model="qwen2.5:7b")
# or
model = ModelFactory.create_model("textgenwebui", port=5000)
```

## Error Handling

The refined code includes comprehensive error handling:

- **Invalid agent types** are caught with descriptive error messages
- **API failures** are handled gracefully with fallback responses
- **Missing state keys** are handled safely using `.get()` method
- **Type validation** ensures correct data types are used

## Example Usage

Run the example script to see all features in action:

```bash
python example_usage.py
```

This will demonstrate:
- Single agent usage
- Hierarchical architecture
- Supervisor architecture
- Error handling

## Configuration

### Model Configuration
- **Ollama**: Set model name in constructor
- **Text Generation WebUI**: Set port number in constructor
- **API URLs**: Configured as constants in respective classes

### Agent Configuration
- **Temperature**: Adjustable in model calls
- **Max tokens**: Configurable per model type
- **Timeout**: Set to 180 seconds by default

## Contributing

When contributing to this project:

1. **Follow the existing code style** with type hints and docstrings
2. **Add error handling** for new functionality
3. **Update documentation** for any new features
4. **Test thoroughly** before submitting changes

## Troubleshooting

### Common Issues

1. **API Connection Errors**
   - Ensure Ollama is running: `ollama serve`
   - Check Text Generation WebUI is accessible
   - Verify port numbers are correct

2. **Model Not Found**
   - Pull the required model: `ollama pull qwen2.5:7b`
   - Check model name spelling

3. **Import Errors**
   - Install dependencies: `pip install -r requirements.txt`
   - Check Python version compatibility

## License

This project is open source. Please refer to the individual file headers for specific licensing information. 

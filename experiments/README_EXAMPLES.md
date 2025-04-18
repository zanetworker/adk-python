# ADK Examples

This repository contains examples of using the Google Agent Development Kit (ADK) to build intelligent agents with various capabilities.

## Examples Overview

### 1. Multi-Agent System

The [multi_agent_system](./multi_agent_system) directory contains an example of a sophisticated multi-agent system that demonstrates how specialized agents can work together to provide comprehensive research and information services.

**Key Features:**
- Multiple specialized agents working together
- Agent delegation and coordination
- Integration with real tools like Google Search
- Mock implementation of MCP (Model Context Protocol) tools

**Running the Example:**
```bash
adk run multi_agent_system
```

For more details, see the [multi_agent_system README](./multi_agent_system/README.md).

### 2. Shared Context Agent

The [shared_context_agent](./shared_context_agent) directory contains an example that demonstrates how tools can share state between different steps of a conversation.

**Key Features:**
- State sharing between tools
- Multi-step workflows
- Session state persistence
- Namespaced state for different scopes

**Running the Example:**
```bash
python shared_context_agent/run_example.py
```

For more details, see the [shared_context_agent README](./shared_context_agent/README.md).

### 3. Example Agent

The [example_agent](./example_agent) directory contains a simple example agent that demonstrates the basic structure of an ADK agent.

**Running the Example:**
```bash
adk run example_agent
```

### 4. Advanced Agent

The [advanced_agent](./advanced_agent) directory contains a more advanced example that demonstrates additional ADK capabilities.

**Running the Example:**
```bash
adk run advanced_agent
```

## Prerequisites

To run these examples, you'll need:

1. Python 3.10+
2. Google ADK installed:
   ```bash
   pip install google-adk
   ```
   
   If you're running from the ADK repository:
   ```bash
   # From the root directory of the repository
   pip install -e .
   ```

3. Required packages for specific examples:
   ```bash
   pip install python-dotenv requests beautifulsoup4 sqlalchemy
   ```

4. A Google AI API key (set in the `.env` file of each example)

## Getting Started

1. Clone this repository
2. Install the required dependencies
3. Set your Google AI API key in the `.env` file of the example you want to run
4. Run the example using the commands provided above

## Learning Path

If you're new to the ADK, we recommend exploring the examples in this order:

1. Start with the [example_agent](./example_agent) to understand the basics
2. Move on to the [advanced_agent](./advanced_agent) to see more advanced features
3. Explore the [shared_context_agent](./shared_context_agent) to learn about state sharing
4. Finally, dive into the [multi_agent_system](./multi_agent_system) to see how multiple agents can work together

Each example builds on the concepts introduced in the previous ones, providing a comprehensive learning path for ADK development.

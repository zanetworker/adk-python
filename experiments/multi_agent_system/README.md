# Multi-Agent Research System

This is a sophisticated multi-agent system built with the Google Agent Development Kit (ADK) that demonstrates how specialized agents can work together to provide comprehensive research and information services.

## System Architecture

The system consists of five specialized agents:

1. **Coordinator Agent**: The main entry point that analyzes queries and delegates to specialized agents
2. **Web Research Agent**: Handles web searches using Google Search for information retrieval
3. **Code Assistant Agent**: Provides code generation, execution, and explanation
4. **Data Agent**: Accesses external data sources via MCP (Model Context Protocol)
5. **Interaction Agent**: Manages user interactions, clarifications, and choices

## Features

- **Agent Specialization**: Each agent focuses on specific tasks and capabilities
- **Tool Integration**: Uses a variety of real tools including:
  - Google Search for web research
  - Code execution for programming tasks
  - MCP tools for external data access (with mock implementations)
  - User choice tools for interactive experiences
- **Structured Data Passing**: Agents exchange structured data with proper formatting
- **Callback Processing**: Custom callbacks format and enhance tool outputs
- **MCP Integration**: Demonstrates how to connect to external services via MCP

## Prerequisites

- Python 3.10+
- Google ADK installed:
  ```bash
  pip install google-adk
  ```
  
  If you're running from the ADK repository:
  ```bash
  # From the root directory of the repository
  pip install -e .
  ```

- Required packages:
  ```bash
  pip install python-dotenv requests beautifulsoup4 sqlalchemy
  ```

- A Google AI API key (set in the `.env` file)

## Running the System

For detailed instructions on running the system, see [RUNNING.md](RUNNING.md).

### Quick Start

1. Replace `YOUR_API_KEY_HERE` in the `.env` file with your actual Google AI API key
2. Run the system using the ADK CLI:

```bash
adk run multi_agent_system
```

3. For the web interface:

```bash
adk web .
```

Then access the web interface at http://localhost:8000

### Example Scripts

We've included example scripts to demonstrate different aspects of the system:

1. **Basic Example**: [run_example.py](run_example.py)
   - Demonstrates how to run the multi-agent system programmatically
   - Run with: `python multi_agent_system/run_example.py`

2. **Distributed Session Example**: [distributed_example.py](distributed_example.py)
   - Shows how to use a distributed session service to share state between agents on different machines
   - Run with: `python multi_agent_system/distributed_example.py`

### Related Examples

For examples of other ADK capabilities:

1. **State Sharing Between Tools**: See the [shared_context_agent](../shared_context_agent) directory
   - Demonstrates how tools can share state between different steps of a conversation
   - Run with: `python shared_context_agent/run_example.py`

## Example Interactions

### Web Research

```
user: What's the latest news about quantum computing?
[coordinator]: I'll help you find the latest news about quantum computing. Let me delegate this to our web research specialist.
[web_research_agent]: Here are the latest developments in quantum computing...
```

### Code Assistance

```
user: Write a Python function to calculate the Fibonacci sequence
[coordinator]: I'll help you with that code. Let me delegate this to our code specialist.
[code_assistant_agent]: Here's a Python function to calculate the Fibonacci sequence...
```

### Data Retrieval

```
user: What's the weather like in Tokyo?
[coordinator]: I'll get that weather information for you. Let me delegate this to our data specialist.
[data_agent]: Weather for Tokyo: 22°C, Partly Cloudy...
```

### Interactive Clarification

```
user: Show me stock information
[coordinator]: I need more details for this request. Let me delegate to our interaction specialist.
[interaction_agent]: Which stock would you like information about? [AAPL, MSFT, GOOGL, AMZN]
user: AAPL
[data_agent]: Stock data for AAPL: $150.25 (+2.5, 1.7%)
```

## Customizing the System

You can extend this system by:

1. Adding more specialized agents
2. Integrating additional tools
3. Connecting to real MCP servers for external data
4. Enhancing the formatting and presentation of results

## MCP Integration

The Data Agent demonstrates how to integrate with external services using MCP:

- The `load_mcp_tools()` function shows how to connect to an MCP server
- For demonstration, we use mock MCP tools, but in a real implementation, you would connect to actual MCP servers
- The system is designed to be easily extended with additional MCP tools

## Notes

- This is a demonstration system with some mock implementations
- In a production environment, you would connect to real APIs and services
- The API key in the `.env` file should be kept secure
- The system will work even if MCP tools are not available, as it includes fallback mock implementations
- If you want to use real MCP tools, you'll need to install the MCP package and set up an MCP server
- Due to API limitations, Google Search cannot be used with other tools in the same agent, so the web research agent only uses Google Search

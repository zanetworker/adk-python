# Running the Multi-Agent System

This document provides instructions on how to run the multi-agent system we've created.

## Prerequisites

Before running the system, make sure you have:

1. Python 3.10+ installed
2. Google ADK installed:
   ```bash
   pip install google-adk
   ```
   
   If you're running from the ADK repository:
   ```bash
   # From the root directory of the repository
   pip install -e .
   ```

3. Required packages installed:
   ```bash
   pip install python-dotenv requests beautifulsoup4 sqlalchemy
   ```

4. A valid Google AI API key (to be added to the `.env` file)

## Setting Up Your API Key

1. Open the `.env` file in the `multi_agent_system` directory
2. Replace `YOUR_API_KEY_HERE` with your actual Google AI API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

## Running the System

### Option 1: Using the ADK CLI

The simplest way to run the system is using the ADK CLI:

```bash
# Navigate to the parent directory of multi_agent_system
cd /path/to/parent/directory

# Run the multi-agent system
adk run multi_agent_system
```

This will start an interactive session where you can chat with the coordinator agent, which will delegate tasks to the specialized agents as needed.

### Option 2: Using the ADK Web Interface

For a more visual experience, you can use the ADK web interface:

```bash
# Navigate to the parent directory of multi_agent_system
cd /path/to/parent/directory

# Start the ADK web server
adk web .
```

Then open your browser and navigate to http://localhost:8000 to interact with the agent through the web interface.

## Example Interactions

Here are some example interactions you can try:

1. **Web Research**: "What's the latest news about quantum computing?"
   - This will use the web research agent with Google Search

2. **Code Generation**: "Write a Python function to calculate the Fibonacci sequence"
   - This will use the code assistant agent

3. **Data Retrieval**: "What's the weather like in Tokyo?"
   - This will use the data agent with mock weather data

4. **Interactive Clarification**: "Show me stock information"
   - This will use the interaction agent to ask for clarification

## Related Examples

For examples of other ADK capabilities:

1. **State Sharing Between Tools**: See the [shared_context_agent](../shared_context_agent) directory
   - Demonstrates how tools can share state between different steps of a conversation
   - Run with: `python shared_context_agent/run_example.py`

## Troubleshooting

If you encounter any issues:

1. **API Key Error**: Make sure your API key is correctly set in the `.env` file
2. **Import Errors**: Ensure all required packages are installed
3. **Google Search Limitations**: Note that Google Search cannot be used with other tools in the same agent due to API limitations

## Understanding the System Architecture

The system consists of five specialized agents:

1. **Coordinator Agent**: The main entry point that analyzes queries and delegates to specialized agents
2. **Web Research Agent**: Handles web searches using Google Search for information retrieval
3. **Code Assistant Agent**: Provides code generation, execution, and explanation
4. **Data Agent**: Accesses external data sources via MCP (with mock implementations)
5. **Interaction Agent**: Manages user interactions, clarifications, and choices

Each agent has specific tools and capabilities, and they work together to provide a comprehensive response to user queries.

## Extending the System

You can extend this system by:

1. Adding more specialized agents
2. Integrating additional tools
3. Connecting to real MCP servers for external data
4. Enhancing the formatting and presentation of results

For more details, see the main README.md file.

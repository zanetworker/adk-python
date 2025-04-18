# Shared Context Agent

This is a demonstration of how tools can share state between different steps of a conversation using the Google Agent Development Kit (ADK).

## Overview

The Shared Context Agent demonstrates a key capability of the ADK: the ability for tools to store data in the session state and for other tools to access that data later. This enables complex workflows where each step builds on the results of previous steps.

## How It Works

The agent implements a simple three-step workflow:

1. **Data Collection**: The `collect_data` tool gathers information about a topic and stores it in the session state.
2. **Data Analysis**: The `analyze_data` tool retrieves the collected data from the session state, analyzes it, and stores the analysis results back in the session state.
3. **Report Generation**: The `generate_report` tool retrieves both the collected data and analysis results from the session state and generates a comprehensive report.

## State Sharing Mechanisms

The agent demonstrates several state sharing mechanisms:

1. **Session State**: Using `tool_context.state["key"] = value` to store data that persists throughout the conversation.
2. **Namespaced State**: Using `tool_context.state["user:key"] = value` to store data that persists across sessions for a specific user.
3. **State Retrieval**: Using `tool_context.state.get("key", default)` to safely retrieve data from the session state.

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
  pip install python-dotenv
  ```

- A Google AI API key (set in the `.env` file)

## Running the Example

1. Replace `YOUR_API_KEY_HERE` in the `.env` file with your actual Google AI API key.
2. Run the example script:

```bash
python shared_context_agent/run_example.py
```

## Example Interaction

```
user: Collect data about artificial intelligence
[state_sharing_agent]: I'll collect data about artificial intelligence and store it in the session state.

[Tool: collect_data] Collected data about artificial intelligence from 3 sources. The data has been stored in the session state with the key "collected_data".

user: Analyze the collected data
[state_sharing_agent]: I'll analyze the data about artificial intelligence that was previously collected.

[Tool: analyze_data] Analyzed data about artificial intelligence. The average reliability of sources is 0.85. The analysis results have been stored in the session state with the key "analysis_results".

user: Generate a report
[state_sharing_agent]: I'll generate a comprehensive report based on the collected data and analysis results.

[Tool: generate_report]
# Report on artificial intelligence

## Overview
This report provides an analysis of artificial intelligence based on 3 sources.

## Source Reliability
The average reliability of sources is 0.85 out of 1.0.

## Key Points
1. Important point 1 about artificial intelligence
2. Important point 2 about artificial intelligence
3. Important point 3 about artificial intelligence

## Sentiment Analysis
The overall sentiment is positive with a score of 0.65 out of 1.0.

## Conclusion
Based on the analysis, artificial intelligence appears to be a promising subject that requires careful consideration.
```

## Extending the Example

You can extend this example by:

1. Adding more tools to the workflow
2. Implementing more complex state sharing patterns
3. Using a distributed session service to share state across different machines
4. Adding error handling and validation for the state data

## Key Concepts

- **Tool Context**: Each tool receives a `tool_context` object that provides access to the session state.
- **State Delta**: Changes to the state are tracked as deltas and committed to the session storage.
- **State Scopes**: The state can be scoped to the app, user, or session level.
- **State Persistence**: The state persists across multiple turns of the conversation.

For more information on state management in the ADK, see the [ADK documentation](https://github.com/google/agent-development-kit).

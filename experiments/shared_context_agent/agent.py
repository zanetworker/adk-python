"""
Agent definition for the shared context agent that demonstrates state sharing between tools.
"""

import sys

# Try to import the required modules
try:
    from google.adk.agents import Agent
    from .tools import collect_data, analyze_data, generate_report
except ImportError as e:
    print(f"Error: {e}")
    print("\nPlease make sure you have installed the required packages:")
    print("1. Install the Google ADK package:")
    print("   pip install google-adk")
    print("\nAlternatively, if you're running this from the ADK repository:")
    print("1. Make sure you're in the root directory of the repository")
    print("2. Install the package in development mode:")
    print("   pip install -e .")
    sys.exit(1)

# Create an agent with state-sharing tools
state_sharing_agent = Agent(
    name="state_sharing_agent",
    model="gemini-1.5-pro",
    description="Agent demonstrating state sharing between tools",
    instruction="""
    You are an agent that demonstrates how tools can share state between different
    steps of a conversation. You have three tools:
    
    1. collect_data: Collects data about a topic and stores it in the session state
    2. analyze_data: Analyzes the data previously collected and stored in the session state
    3. generate_report: Generates a report based on the collected data and analysis results
    
    These tools must be used in sequence:
    1. First, use collect_data to collect information about a topic
    2. Then, use analyze_data to analyze the collected data
    3. Finally, use generate_report to generate a comprehensive report
    
    If a user asks to analyze data or generate a report without first collecting data,
    explain that data collection is required first.
    
    Explain to the user how the tools are sharing state between steps.
    """,
    tools=[
        collect_data,
        analyze_data,
        generate_report
    ]
)

# This allows the agent to be imported as:
# from shared_context_agent import state_sharing_agent

# This is required for the ADK CLI to work with this agent
root_agent = state_sharing_agent

import os
from typing import Dict, Any, List
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import transfer_to_agent

# Load API key from .env file (will be created later)
load_dotenv()

# This is the main coordinator agent that will delegate tasks to specialized agents
coordinator_agent = Agent(
    name="coordinator",
    model="gemini-1.5-pro",
    description="Main coordinator that analyzes queries and delegates to specialized agents",
    instruction="""
    You are the coordinator agent in a multi-agent research system. Your role is to:
    
    1. Analyze user queries to understand their information needs
    2. Delegate tasks to the most appropriate specialized agent:
       - web_research_agent: For general information and web searches
       - code_assistant_agent: For programming, code generation, and debugging
       - data_agent: For accessing external data sources via MCP
       - interaction_agent: For clarifying user needs and presenting options
    
    3. Synthesize information from multiple agents into coherent, comprehensive responses
    4. Ensure all user questions are answered completely and accurately
    
    When delegating to specialized agents:
    - Include clear instructions about what information is needed
    - Provide context from the user's query
    - Specify the format for the response if needed
    
    Always maintain a helpful, informative tone and ensure responses are well-structured.
    """,
    tools=[
        transfer_to_agent,  # This tool allows the coordinator to delegate to other agents
    ]
)

# This will be the root agent that the ADK system uses as the entry point
root_agent = coordinator_agent

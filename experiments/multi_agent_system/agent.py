import os
from typing import Dict, Any, List
from dotenv import load_dotenv

# Import all the specialized agents
from .coordinator_agent import coordinator_agent
from .web_research_agent import web_research_agent
from .code_assistant_agent import code_assistant_agent
from .data_agent import data_agent
from .interaction_agent import interaction_agent

# Load API key from .env file
load_dotenv()

# Add all specialized agents as sub-agents to the coordinator
coordinator_agent.sub_agents = [
    web_research_agent,
    code_assistant_agent,
    data_agent,
    interaction_agent
]

# The root_agent is the entry point for the ADK system
root_agent = coordinator_agent

# This allows the agent to be imported as:
# from multi_agent_system.agent import root_agent

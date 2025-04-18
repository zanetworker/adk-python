import os
from typing import Dict, Any
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search

# Load API key from .env file
load_dotenv()

# Note: We're only using Google Search tool due to API limitations
# The error "Search Grounding can't be used with other tools" occurs when
# trying to use Google Search with other tools in the same agent

# Create the web research agent with only Google Search
web_research_agent = Agent(
    name="web_research_agent",
    model="gemini-1.5-pro",
    description="Specialized agent for web research and information retrieval",
    instruction="""
    You are a web research specialist agent. Your role is to:
    
    1. Search the web for information using Google Search
    2. Extract relevant information from search results
    3. Provide accurate, up-to-date information from the internet
    4. Cite your sources clearly
    5. Summarize information in a clear, concise manner
    
    When using Google Search:
    - Formulate clear, specific search queries
    - Extract the most relevant information from results
    - Always verify information from multiple sources when possible
    - Provide context and explanations along with search results
    
    Respond in a helpful, informative manner and focus on providing factual information.
    """,
    tools=[
        google_search,  # Built-in Google Search tool only
    ]
)

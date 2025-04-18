import os
from google.adk.agents import Agent
from typing import Optional
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

def get_weather(city: str) -> str:
    """Get the current weather for a city"""
    # This is a mock implementation
    return f"Getting weather for {city}..."

def answer_question(query: str) -> str:
    """Answer a general knowledge question"""
    return f"Searching for answer about: {query}"

# Create a simple agent
root_agent = Agent(
    name="simple_assistant",
    model="gemini-1.5-pro",  # Using a newer Gemini model
    description="A simple assistant that can answer questions",
    instruction="""
    You are a helpful assistant. Your goals are to:
    1. Answer user questions accurately
    2. Be concise and clear in your responses
    3. Ask for clarification if a query is ambiguous
    """,
    tools=[
        get_weather,  # Custom weather tool
        answer_question  # Custom QA tool
    ]
)

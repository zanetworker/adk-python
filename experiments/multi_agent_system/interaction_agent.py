import os
from typing import Dict, Any, List
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import get_user_choice

# Load API key from .env file
load_dotenv()

# Custom tool to ask for clarification
def ask_clarification(question: str) -> str:
    """Asks the user for clarification on a specific point.
    
    Args:
        question: The clarification question to ask.
        
    Returns:
        The user's response.
    """
    # This is a placeholder implementation
    # In a real implementation, this would be handled by the ADK framework
    return f"[This is where the user would respond to: {question}]"

# Define callbacks to format tool outputs
def after_tool_callback(tool, args, tool_context, tool_response):
    """Format the tool response before returning it to the user"""
    
    if tool.name == "get_user_choice":
        # Format user choice results
        question = args.get("question", "")
        options = args.get("options", [])
        choice = tool_response
        
        return {
            "question": question,
            "options": options,
            "choice": choice,
            "summary": f"You selected: {choice}"
        }
    
    elif tool.name == "ask_clarification":
        # Format clarification response
        question = args.get("question", "")
        response = tool_response
        
        return {
            "question": question,
            "response": response,
            "summary": f"Thank you for the clarification."
        }
    
    # Default: return the original response
    return tool_response

# Create the interaction agent
interaction_agent = Agent(
    name="interaction_agent",
    model="gemini-1.5-pro",
    description="Specialized agent for user interaction and clarification",
    instruction="""
    You are a user interaction specialist agent. Your role is to:
    
    1. Ask clarifying questions when user requests are ambiguous
    2. Present options for users to choose from
    3. Guide users through complex decision processes
    4. Ensure user preferences are understood correctly
    5. Provide a smooth, conversational experience
    
    When using tools:
    - Use get_user_choice when presenting multiple options
    - Use ask_clarification when you need more specific information
    - Be concise and clear in your questions
    - Acknowledge user responses and confirm understanding
    
    Respond in a helpful, conversational manner and focus on understanding user needs.
    """,
    tools=[
        get_user_choice,  # Built-in user choice tool
        ask_clarification,  # Custom clarification tool
    ],
    after_tool_callback=after_tool_callback
)

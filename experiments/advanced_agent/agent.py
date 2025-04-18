import os
import json
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext

# Load API key from .env file
load_dotenv()

def get_weather(city: str) -> Dict[str, Any]:
    """Get the current weather for a city
    
    Args:
        city: The name of the city to get weather for
        
    Returns:
        A dictionary containing weather information
    """
    # This is a mock implementation
    # In a real implementation, this would call a weather API
    weather_data = {
        "city": city,
        "temperature": 28,
        "unit": "celsius",
        "condition": "Sunny",
        "humidity": 45,
        "wind_speed": 10,
        "wind_direction": "NE",
        "forecast": ["Sunny", "Partly Cloudy", "Cloudy", "Rainy", "Sunny"]
    }
    return weather_data

def answer_question(query: str) -> Dict[str, Any]:
    """Answer a general knowledge question
    
    Args:
        query: The question to answer
        
    Returns:
        A dictionary containing the answer and sources
    """
    # This is a mock implementation
    # In a real implementation, this would use a search API or knowledge base
    answer_data = {
        "query": query,
        "answer": f"Here is information about: {query}",
        "confidence": 0.85,
        "sources": [
            {"title": "Example Source 1", "url": "https://example.com/1"},
            {"title": "Example Source 2", "url": "https://example.com/2"}
        ]
    }
    return answer_data

# Define callbacks to format tool outputs
def before_tool_callback(tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext) -> Optional[Dict]:
    """Called before a tool is executed"""
    # We could modify the arguments here if needed
    return None  # Return None to proceed with the actual tool call

def after_tool_callback(
    tool: BaseTool, 
    args: Dict[str, Any], 
    tool_context: ToolContext, 
    tool_response: Dict[str, Any]
) -> Optional[Dict]:
    """Format the tool response before returning it to the user"""
    
    # Format weather data
    if tool.name == "get_weather":
        city = tool_response.get("city", "Unknown")
        temp = tool_response.get("temperature", "N/A")
        unit = tool_response.get("unit", "celsius")
        condition = tool_response.get("condition", "Unknown")
        humidity = tool_response.get("humidity", "N/A")
        
        formatted_response = {
            "result": f"Weather for {city}: {temp}°{unit[0].upper()}, {condition}, Humidity: {humidity}%",
            "forecast": f"5-day forecast: {', '.join(tool_response.get('forecast', []))}",
            "raw_data": tool_response
        }
        return formatted_response
    
    # Format search/question answers
    elif tool.name == "answer_question":
        query = tool_response.get("query", "")
        answer = tool_response.get("answer", "No answer found")
        sources = tool_response.get("sources", [])
        
        source_text = ""
        if sources:
            source_text = "\n\nSources:\n" + "\n".join([f"- {s['title']}: {s['url']}" for s in sources])
            
        formatted_response = {
            "result": f"{answer}{source_text}",
            "confidence": tool_response.get("confidence", 0),
            "raw_data": tool_response
        }
        return formatted_response
    
    # Default: return the original response
    return tool_response

# Create the advanced agent
root_agent = Agent(
    name="advanced_assistant",
    model="gemini-1.5-pro",
    description="An advanced assistant that formats tool outputs nicely",
    instruction="""
    You are a helpful assistant with advanced formatting capabilities. Your goals are to:
    1. Answer user questions accurately using the tools provided
    2. Format tool outputs in a clear, readable way
    3. Provide additional context and explanations with tool results
    4. Be concise yet informative in your responses
    5. Ask for clarification if a query is ambiguous
    
    When you receive structured data from tools:
    - Present the most important information first
    - Format numerical data with appropriate units
    - Include relevant details that help the user understand the answer
    - Cite sources when available
    """,
    tools=[
        get_weather,
        answer_question
    ],
    before_tool_callback=before_tool_callback,
    after_tool_callback=after_tool_callback
)

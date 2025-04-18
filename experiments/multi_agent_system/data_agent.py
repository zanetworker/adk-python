import os
import asyncio
from typing import Dict, Any, List
from dotenv import load_dotenv
from google.adk.agents import Agent

# Try to import MCP tools, but provide fallbacks if not available
try:
    from google.adk.tools.mcp_tool import MCPToolset, MCPTool
    from mcp import StdioServerParameters
    MCP_AVAILABLE = True
except ImportError:
    print("MCP tools not available. Using mock implementations only.")
    MCP_AVAILABLE = False

# Load API key from .env file
load_dotenv()

# This function would be used to load MCP tools when the agent is initialized
# It's wrapped in a conditional to handle cases where MCP is not available
if MCP_AVAILABLE:
    async def load_mcp_tools():
        """Load tools from an MCP server.
        
        Returns:
            A tuple of (tools, exit_stack) where tools is a list of MCPTools
            and exit_stack is the AsyncExitStack used to manage the connection.
        """
        try:
            # Connect to a weather data MCP server
            # In a real implementation, this would connect to an actual MCP server
            # For demonstration, we're using a mock server command
            tools, exit_stack = await MCPToolset.from_server(
                connection_params=StdioServerParameters(
                    command='python',
                    args=["-m", "mock_weather_mcp_server"],  # This is a placeholder
                )
            )
            return tools, exit_stack
        except Exception as e:
            print(f"Error loading MCP tools: {str(e)}")
            # Return empty list if MCP tools can't be loaded
            return [], None
else:
    # Placeholder function when MCP is not available
    async def load_mcp_tools():
        """Placeholder function when MCP is not available."""
        print("MCP tools not available. This function is a placeholder.")
        return [], None

# Define mock tool functions for demonstration
# In a real implementation, these would be loaded from an MCP server

def get_weather(location: str) -> Dict[str, Any]:
    """Get weather data for a location.
    
    Args:
        location: The location to get weather for.
        
    Returns:
        Weather data for the location.
    """
    # Mock weather data
    weather_data = {
        "location": location,
        "temperature": 22,
        "unit": "celsius",
        "condition": "Partly Cloudy",
        "humidity": 65,
        "wind": {
            "speed": 10,
            "direction": "NE"
        },
        "forecast": [
            {"day": "Today", "condition": "Partly Cloudy", "high": 22, "low": 15},
            {"day": "Tomorrow", "condition": "Sunny", "high": 25, "low": 16},
            {"day": "Day 3", "condition": "Rainy", "high": 20, "low": 14}
        ]
    }
    
    return weather_data

def get_stock_data(symbol: str) -> Dict[str, Any]:
    """Get stock market data for a symbol.
    
    Args:
        symbol: The stock symbol to get data for.
        
    Returns:
        Stock market data for the symbol.
    """
    # Mock stock data
    stock_data = {
        "symbol": symbol,
        "price": 150.25,
        "change": 2.5,
        "change_percent": 1.7,
        "volume": 1200000,
        "market_cap": "1.2T",
        "pe_ratio": 25.3,
        "dividend_yield": 1.2,
        "historical": [
            {"date": "2025-04-12", "close": 147.75},
            {"date": "2025-04-11", "close": 148.50},
            {"date": "2025-04-10", "close": 149.25}
        ]
    }
    
    return stock_data

# Define callbacks to format tool outputs
def after_tool_callback(tool, args, tool_context, tool_response):
    """Format the tool response before returning it to the user"""
    
    if tool.name == "get_weather":
        # Format weather data
        location = tool_response.get("location", "Unknown")
        temp = tool_response.get("temperature", "N/A")
        condition = tool_response.get("condition", "Unknown")
        
        forecast_text = ""
        if "forecast" in tool_response:
            forecast_text = "\n\nForecast:\n"
            for day in tool_response["forecast"]:
                forecast_text += f"- {day['day']}: {day['condition']}, High: {day['high']}°C, Low: {day['low']}°C\n"
        
        return {
            "data": tool_response,
            "summary": f"Weather for {location}: {temp}°C, {condition}{forecast_text}"
        }
    
    elif tool.name == "get_stock_data":
        # Format stock data
        symbol = tool_response.get("symbol", "Unknown")
        price = tool_response.get("price", "N/A")
        change = tool_response.get("change", 0)
        change_percent = tool_response.get("change_percent", 0)
        
        change_text = f"+{change}" if change >= 0 else f"{change}"
        
        return {
            "data": tool_response,
            "summary": f"Stock data for {symbol}: ${price} ({change_text}, {change_percent}%)"
        }
    
    # Default: return the original response
    return tool_response

# Create the data agent with mock tool functions
# In a real implementation, these would be loaded from an MCP server
data_agent = Agent(
    name="data_agent",
    model="gemini-1.5-pro",
    description="Specialized agent for accessing external data sources via MCP",
    instruction="""
    You are a data specialist agent. Your role is to:
    
    1. Access external data sources through MCP tools
    2. Retrieve weather data for locations worldwide
    3. Obtain financial market information
    4. Process and analyze data to extract insights
    5. Present data in a clear, understandable format
    
    When using tools:
    - Use get_weather for weather forecasts and current conditions
    - Use get_stock_data for financial market information
    - Format data in a user-friendly way
    - Provide context and explanations for the data
    
    Respond in a helpful, informative manner and focus on providing accurate data.
    """,
    tools=[
        get_weather,  # Mock weather data function
        get_stock_data,  # Mock financial data function
    ],
    after_tool_callback=after_tool_callback
)

# Note: In a real implementation, you would use the load_mcp_tools function
# to dynamically load tools from an MCP server, and then create the agent
# with those tools. For demonstration purposes, we're using mock tools.

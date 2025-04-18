# ADK Agent Examples

This repository contains two example agents built with the Google Agent Development Kit (ADK):

1. **Simple Agent** - A basic agent with minimal configuration
2. **Advanced Agent** - An agent with structured tool outputs and formatting

## Prerequisites

- Python 3.9+
- Google ADK installed (`pip install google-adk`)
- A Google AI API key (set in the `.env` file in each agent directory)

## Simple Agent

The simple agent demonstrates the basic functionality of the ADK. It has:

- Simple tools that return string responses
- Minimal configuration
- Direct output without additional formatting

### Running the Simple Agent

```bash
adk run example_agent
```

### Example Interactions

```
user: hi
[simple_assistant]: How can I help you today?

user: what is a coyote?
[simple_assistant]: Searching for answer about: What is a coyote?

user: whats the weather?
[simple_assistant]: What city are you interested in?

user: cairo
[simple_assistant]: Getting weather for cairo...
```

## Advanced Agent

The advanced agent demonstrates more sophisticated features of the ADK. It has:

- Tools that return structured data (dictionaries)
- Custom callbacks to format tool outputs
- Rich formatting of responses
- More detailed instructions for the LLM

### Running the Advanced Agent

```bash
adk run advanced_agent
```

### Example Interactions

```
user: hi
[advanced_assistant]: Hello! I'm your advanced assistant. How can I help you today?

user: what is a coyote?
[advanced_assistant]: Here is information about: What is a coyote?

Sources:
- Example Source 1: https://example.com/1
- Example Source 2: https://example.com/2

user: whats the weather?
[advanced_assistant]: What city would you like to know the weather for?

user: cairo
[advanced_assistant]: Weather for Cairo: 28°C, Sunny, Humidity: 45%
5-day forecast: Sunny, Partly Cloudy, Cloudy, Rainy, Sunny
```

## Key Differences

| Feature | Simple Agent | Advanced Agent |
|---------|-------------|----------------|
| Tool Return Type | Strings | Structured Dictionaries |
| Output Formatting | None (raw tool output) | Formatted with callbacks |
| Additional Context | None | Sources, forecasts, etc. |
| LLM Instructions | Basic | Detailed formatting guidance |

## Implementation Details

### Simple Agent

The simple agent uses basic function tools that return strings directly to the user:

```python
def get_weather(city: str) -> str:
    """Get the current weather for a city"""
    # This is a mock implementation
    return f"Getting weather for {city}..."
```

### Advanced Agent

The advanced agent uses tools that return structured data:

```python
def get_weather(city: str) -> Dict[str, Any]:
    """Get the current weather for a city"""
    # This is a mock implementation
    weather_data = {
        "city": city,
        "temperature": 28,
        "unit": "celsius",
        "condition": "Sunny",
        "humidity": 45,
        # ...more data
    }
    return weather_data
```

And implements callbacks to format the output:

```python
def after_tool_callback(tool, args, tool_context, tool_response):
    # Format weather data
    if tool.name == "get_weather":
        city = tool_response.get("city", "Unknown")
        temp = tool_response.get("temperature", "N/A")
        # ...format the response
        return formatted_response
```

## Customizing the Examples

You can modify these examples to:

1. Connect to real APIs for weather and search
2. Add more sophisticated formatting
3. Implement additional tools
4. Experiment with different LLM models and configurations

## Notes

- These examples use mock implementations for the tools
- In a production environment, you would connect to real APIs
- The API key in the `.env` file should be replaced with your actual Google AI API key

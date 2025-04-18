import os
from typing import Dict, Any
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import built_in_code_execution

# Load API key from .env file
load_dotenv()

# Custom tool to explain code
def explain_code(code: str, language: str = "python") -> str:
    """Analyzes and explains the provided code.
    
    Args:
        code: The code to explain.
        language: The programming language of the code.
        
    Returns:
        A detailed explanation of the code.
    """
    # This is a mock implementation
    # In a real implementation, this would use more sophisticated analysis
    return f"""
    Code Analysis ({language}):
    
    This code appears to be written in {language}.
    
    Here's a breakdown of what it does:
    1. The code is {len(code.splitlines())} lines long
    2. It uses various {language} features and patterns
    3. A detailed explanation would analyze the structure, functions, and logic
    
    For a more detailed analysis, I can break down specific parts of the code.
    """

# Define callbacks to format tool outputs
def after_tool_callback(tool, args, tool_context, tool_response):
    """Format the tool response before returning it to the user"""
    
    if tool.name == "code_execution":
        # Format code execution results
        code = args.get("code", "")
        result = tool_response
        
        return {
            "code": code,
            "execution_result": result,
            "summary": "Here are the results of executing your code."
        }
    
    elif tool.name == "explain_code":
        # Format code explanation
        code = args.get("code", "")
        language = args.get("language", "python")
        explanation = tool_response
        
        return {
            "code": code,
            "language": language,
            "explanation": explanation,
            "summary": f"Here's an explanation of your {language} code."
        }
    
    # Default: return the original response
    return tool_response

# Create the code assistant agent
code_assistant_agent = Agent(
    name="code_assistant_agent",
    model="gemini-1.5-pro",
    description="Specialized agent for code generation, execution, and debugging",
    instruction="""
    You are a code assistant specialist agent. Your role is to:
    
    1. Generate code based on user requirements
    2. Execute code to test functionality
    3. Debug and fix issues in existing code
    4. Explain code to help users understand it
    5. Provide best practices and optimization suggestions
    
    When using tools:
    - Use built_in_code_execution to run and test code
    - Use explain_code to provide detailed explanations of code
    - Always include comments in generated code
    - Test code thoroughly before providing it to users
    - Explain your thought process when debugging issues
    
    Respond in a helpful, informative manner and focus on providing high-quality code solutions.
    """,
    tools=[
        built_in_code_execution,  # Built-in code execution tool
        explain_code,  # Custom code explanation tool
    ],
    after_tool_callback=after_tool_callback
)

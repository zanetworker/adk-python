#!/usr/bin/env python3
"""
Example script to run the multi-agent system programmatically.
This demonstrates how to initialize and run the system from Python code.
"""

import asyncio
import os
import sys

# Try to import the required modules
try:
    from dotenv import load_dotenv
    from google.adk.runners import InteractiveRunner
    
    # Import the root agent from our multi-agent system
    from multi_agent_system import root_agent
except ImportError as e:
    print(f"Error: {e}")
    print("\nPlease make sure you have installed the required packages:")
    print("1. Install the Google ADK package:")
    print("   pip install google-adk")
    print("2. Install the dotenv package:")
    print("   pip install python-dotenv")
    print("\nAlternatively, if you're running this from the ADK repository:")
    print("1. Make sure you're in the root directory of the repository")
    print("2. Install the package in development mode:")
    print("   pip install -e .")
    sys.exit(1)

async def run_interactive_session():
    """Run an interactive session with the multi-agent system."""
    # Load API key from .env file
    load_dotenv()
    
    # Check if API key is set
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("ERROR: Please set your Google API key in the .env file")
        print("Open multi_agent_system/.env and replace YOUR_API_KEY_HERE with your actual API key")
        return
    
    print("Starting interactive session with multi-agent system...")
    print("Type 'exit' to end the session")
    print("-" * 50)
    
    # Create an interactive runner for the root agent
    runner = InteractiveRunner(agent=root_agent)
    
    # Start the interactive session
    await runner.run_interactive()

if __name__ == "__main__":
    # Run the interactive session
    asyncio.run(run_interactive_session())

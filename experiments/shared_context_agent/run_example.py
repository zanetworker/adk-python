#!/usr/bin/env python3
"""
Example script to run the state sharing agent.
This demonstrates how tools can share state between different steps of a conversation.
"""

import asyncio
import os
import sys

# Try to import the required modules
try:
    from dotenv import load_dotenv
    from google.adk.runners import InteractiveRunner
    
    # Import the state sharing agent
    from shared_context_agent import state_sharing_agent
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

async def run_state_sharing_example():
    """Run an interactive session with the state-sharing agent."""
    # Load API key from .env file
    load_dotenv()
    
    # Check if API key is set
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("ERROR: Please set your Google API key in the .env file")
        print("Open .env and replace YOUR_API_KEY_HERE with your actual API key")
        return
    
    print("Starting interactive session with state-sharing agent...")
    print("This example demonstrates how tools can share state between different steps")
    print("Try these commands in sequence:")
    print("1. 'Collect data about artificial intelligence'")
    print("2. 'Analyze the collected data'")
    print("3. 'Generate a report'")
    print("Type 'exit' to end the session")
    print("-" * 50)
    
    # Create an interactive runner for the state-sharing agent
    runner = InteractiveRunner(agent=state_sharing_agent)
    
    # Start the interactive session
    await runner.run_interactive()

if __name__ == "__main__":
    # Run the interactive session
    asyncio.run(run_state_sharing_example())

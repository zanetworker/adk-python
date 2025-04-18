#!/usr/bin/env python3
"""
Example script demonstrating how to use a distributed session service
with the multi-agent system to share state between agents running on
different machines.
"""

import asyncio
import os
import sys

# Try to import the required modules
try:
    from dotenv import load_dotenv
    from google.adk.runners import InteractiveRunner
    from google.adk.sessions import DatabaseSessionService
    
    # Import the root agent from our multi-agent system
    from multi_agent_system import root_agent
except ImportError as e:
    print(f"Error: {e}")
    print("\nPlease make sure you have installed the required packages:")
    print("1. Install the Google ADK package:")
    print("   pip install google-adk")
    print("2. Install the dotenv package:")
    print("   pip install python-dotenv")
    print("3. Install database dependencies:")
    print("   pip install sqlalchemy")
    print("\nAlternatively, if you're running this from the ADK repository:")
    print("1. Make sure you're in the root directory of the repository")
    print("2. Install the package in development mode:")
    print("   pip install -e .")
    sys.exit(1)

async def run_with_distributed_session():
    """Run the multi-agent system with a distributed session service."""
    # Load API key from .env file
    load_dotenv()
    
    # Check if API key is set
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("ERROR: Please set your Google API key in the .env file")
        print("Open multi_agent_system/.env and replace YOUR_API_KEY_HERE with your actual API key")
        return
    
    # Get database URL from environment variable or use a default SQLite database
    db_url = os.getenv("DATABASE_URL", "sqlite:///multi_agent_sessions.db")
    
    print(f"Using database: {db_url}")
    print("Starting multi-agent system with distributed session service...")
    print("Type 'exit' to end the session")
    print("-" * 50)
    
    try:
        # Create a database session service
        # This allows state to be shared between agents running on different machines
        session_service = DatabaseSessionService(db_url=db_url)
        
        # Create an interactive runner with the session service
        runner = InteractiveRunner(
            agent=root_agent,
            session_service=session_service
        )
        
        # Start the interactive session
        await runner.run_interactive()
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure the database URL is correct")
        print("2. For PostgreSQL or MySQL, ensure the database exists and is accessible")
        print("3. For SQLite, ensure the directory is writable")
        print("\nExample database URLs:")
        print("- SQLite: sqlite:///path/to/database.db")
        print("- PostgreSQL: postgresql://username:password@localhost/dbname")
        print("- MySQL: mysql://username:password@localhost/dbname")

if __name__ == "__main__":
    # Run the interactive session with distributed session service
    asyncio.run(run_with_distributed_session())

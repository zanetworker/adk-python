"""
Tools for the shared context agent that demonstrate state sharing between steps.
"""

import sys
from typing import Dict, Any, List

# Try to import the required modules
try:
    # This is just to check if google.adk is installed
    import google.adk
except ImportError as e:
    print(f"Error: {e}")
    print("\nPlease make sure you have installed the required packages:")
    print("1. Install the Google ADK package:")
    print("   pip install google-adk")
    print("\nAlternatively, if you're running this from the ADK repository:")
    print("1. Make sure you're in the root directory of the repository")
    print("2. Install the package in development mode:")
    print("   pip install -e .")
    sys.exit(1)

def collect_data(topic: str) -> Dict[str, Any]:
    """Collect data about a topic and store it in the session state.
    
    Args:
        topic: The topic to collect data about
        
    Returns:
        A dictionary with information about the collected data
    """
    # In a real implementation, this would collect actual data
    # For this example, we'll use mock data
    
    # Create some mock data based on the topic
    collected_data = {
        "topic": topic,
        "sources": [
            {"name": "Source 1", "reliability": 0.85},
            {"name": "Source 2", "reliability": 0.92},
            {"name": "Source 3", "reliability": 0.78}
        ],
        "key_points": [
            f"Important point 1 about {topic}",
            f"Important point 2 about {topic}",
            f"Important point 3 about {topic}"
        ],
        "timestamp": "2025-04-13T20:30:00Z"
    }
    
    # Store the collected data in the session state
    # This makes it available to other tools later in the conversation
    tool_context.state["collected_data"] = collected_data
    
    # Also store it in a namespaced key for persistence across sessions
    tool_context.state[f"user:data_on_{topic}"] = collected_data
    
    return {
        "message": f"Collected data about {topic} from 3 sources",
        "stored_in_state": True,
        "state_key": "collected_data"
    }

def analyze_data() -> Dict[str, Any]:
    """Analyze the data previously collected and stored in the session state.
    
    Returns:
        A dictionary with analysis results
    """
    # Retrieve the collected data from the session state
    collected_data = tool_context.state.get("collected_data", None)
    
    if not collected_data:
        return {
            "error": "No data found in session state. Please collect data first."
        }
    
    # In a real implementation, this would perform actual analysis
    # For this example, we'll create mock analysis results
    
    topic = collected_data.get("topic", "unknown")
    sources = collected_data.get("sources", [])
    key_points = collected_data.get("key_points", [])
    
    # Calculate average source reliability
    avg_reliability = sum(source.get("reliability", 0) for source in sources) / len(sources) if sources else 0
    
    # Create analysis results
    analysis_results = {
        "topic": topic,
        "source_count": len(sources),
        "average_reliability": avg_reliability,
        "key_point_count": len(key_points),
        "sentiment": 0.65,  # Mock sentiment score
        "summary": f"Analysis of {topic} based on {len(sources)} sources with {avg_reliability:.2f} average reliability"
    }
    
    # Store the analysis results in the session state
    tool_context.state["analysis_results"] = analysis_results
    
    return {
        "message": f"Analyzed data about {topic}",
        "average_reliability": f"{avg_reliability:.2f}",
        "key_points_analyzed": len(key_points),
        "stored_in_state": True,
        "state_key": "analysis_results"
    }

def generate_report() -> str:
    """Generate a report based on the collected data and analysis results.
    
    Returns:
        A formatted report as a string
    """
    # Retrieve data from the session state
    collected_data = tool_context.state.get("collected_data", {})
    analysis_results = tool_context.state.get("analysis_results", {})
    
    if not collected_data or not analysis_results:
        return "ERROR: Missing data in session state. Please collect and analyze data first."
    
    topic = collected_data.get("topic", "unknown")
    sources = collected_data.get("sources", [])
    key_points = collected_data.get("key_points", [])
    avg_reliability = analysis_results.get("average_reliability", 0)
    sentiment = analysis_results.get("sentiment", 0)
    
    # Generate a formatted report
    report = f"""
    # Report on {topic}
    
    ## Overview
    This report provides an analysis of {topic} based on {len(sources)} sources.
    
    ## Source Reliability
    The average reliability of sources is {avg_reliability:.2f} out of 1.0.
    
    ## Key Points
    """
    
    for i, point in enumerate(key_points, 1):
        report += f"\n{i}. {point}"
    
    report += f"""
    
    ## Sentiment Analysis
    The overall sentiment is {"positive" if sentiment > 0.6 else "neutral" if sentiment > 0.4 else "negative"} 
    with a score of {sentiment:.2f} out of 1.0.
    
    ## Conclusion
    Based on the analysis, {topic} appears to be a {"promising" if sentiment > 0.6 else "complex" if sentiment > 0.4 else "challenging"} subject 
    that requires {"further exploration" if avg_reliability < 0.8 else "careful consideration"}.
    """
    
    # Store the report in the session state
    tool_context.state["generated_report"] = report
    
    return report

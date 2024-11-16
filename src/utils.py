import os
from typing import Optional
from rich.console import Console

console = Console()

def check_environment() -> Optional[str]:
    """
    Check if all required environment variables are set.
    
    Returns:
        Optional[str]: Error message if environment is not properly configured
    """
    required_vars = ['OPENAI_API_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        return f"Missing required environment variables: {', '.join(missing_vars)}"
    return None

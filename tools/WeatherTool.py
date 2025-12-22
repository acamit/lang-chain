from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime

from tools.Context import Context


@tool
def get_weather_for_location(city: str) -> str:
    """Get the weather for a specific location."""
    # Dummy implementation for illustration
    return f"The current weather in {city} is sunny with a temperature of 75°F."





@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """Retrieve user information based on user id"""
    user_id = runtime.context.user_id
    # Dummy implementation for illustration
    return "Florida" if user_id == "1" else "SF"

from dataclasses import dataclass


@dataclass
class Context:
    """Custom runtime context schema for the tool."""
    user_id: str

from pydantic import BaseModel


class Context(BaseModel):
    """Custom runtime context schema for the tool."""
    user_id: str

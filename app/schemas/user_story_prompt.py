from datetime import datetime

from pydantic import BaseModel


# Shared properties
class UserStoryPrompt(BaseModel):
    id: int = 1
    user_id: int = 1
    story_session_id: int = 1
    prompt: str = None
    created: datetime = datetime.utcnow
    status: int = 1

    # has a user
    # has a story session
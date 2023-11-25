from datetime import datetime

from pydantic import BaseModel


# Shared properties
class UserStorySessionObjective(BaseModel):
    id: int = 1
    story_session_id: int = 1
    title: str = None
    created: datetime = datetime.utcnow
    updated: datetime = datetime.utcnow
    status: int = 1

    # has a user
    # has a story session

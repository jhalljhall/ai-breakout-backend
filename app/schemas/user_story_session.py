from datetime import datetime

from pydantic import BaseModel


# Shared properties
class UserStorySession(BaseModel):
    id: int = 1
    user_id: int = 1
    story_session_id: int = 1
    created: datetime = datetime.utcnow

    # has a user
    # has a story session
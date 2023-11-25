from datetime import datetime

from pydantic import BaseModel


# Shared properties
class StorySession(BaseModel):
    id: int = 1
    story_id: int = 1
    initial_prompt: str = None
    template: str = None
    objectives: str = None
    endgame: str = None
    created: datetime = datetime.utcnow
    updated: datetime = datetime.utcnow
    status: int = 1

    # has objective items (one to many)
    # has a story (one to one)
    # has achievement items (one to many)
    # has prompt items (one to many)
    # has watchdog items (one to many)
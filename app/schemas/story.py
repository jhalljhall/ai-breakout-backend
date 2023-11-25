from datetime import datetime

from pydantic import BaseModel


# Shared properties
class Story(BaseModel):
    id: int = 1
    title: str = None
    initial_prompt: str = None
    template: str = None
    objectives: str = None
    banner_img_url: str = None
    avatar_img_url: str = None
    created: datetime = datetime.utcnow
    updated: datetime = datetime.utcnow
    status: int = 1

    # has sessions (one to many)
from datetime import datetime

from pydantic import BaseModel


# Shared properties
class Watchdog(BaseModel):
    id: int = 1
    story_session_id: int = 1
    log: str = None
    blob: str = None
    created: datetime = datetime.utcnow

    # has a story session
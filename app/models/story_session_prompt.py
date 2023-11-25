from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class StorySessionPrompts(Base):
    __tablename__ = "story_session_prompts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = ForeignKey("users.id")
    story_session_id = ForeignKey("story_sessions.id")
    prompt = Column(String, index=True)
    created = Column(DateTime, default=datetime.utcnow)
    status = Column(Integer, nullable=False, default=1)
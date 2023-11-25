from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class StorySession(Base):
    __tablename__ = "story_sessions"

    id = Column(Integer, primary_key=True, index=True)
    story_id = ForeignKey("stories.id")
    initial_prompt = Column(String, nullable=False)
    template = Column(String, nullable=False)
    objectives = Column(String, nullable=False)
    endgame = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, default=datetime.utcnow)
    status = Column(Integer, nullable=False, default=1)
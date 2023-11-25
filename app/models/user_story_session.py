from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class UserStorySession(Base):
    __tablename__ = "user_story_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = ForeignKey("user.id")
    story_session_id = ForeignKey("story_sessions.id")
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, default=datetime.utcnow)
    status = Column(Integer, nullable=False, default=1)
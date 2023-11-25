from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class StorySessionObjectiveAchievement(Base):
    __tablename__ = "story_session_achievements"

    id = Column(Integer, primary_key=True, index=True)
    story_session_id = ForeignKey("story_sessions.id")
    user_story_prompt_id = ForeignKey("story_sessions.id")
    user_id = ForeignKey("users.id")
    title = Column(String, index=True)
    created = Column(DateTime, default=datetime.utcnow)
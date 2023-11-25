from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class Watchdog(Base):
    __tablename__ = "watchdog"

    id = Column(Integer, primary_key=True, index=True)
    story_session_id = ForeignKey("story_sessions.id")
    log = Column(String, nullable=True)
    data = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
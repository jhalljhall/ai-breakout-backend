from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    template = Column(String, nullable=False)
    objectives = Column(String, nullable=False)
    endgame = Column(String, nullable=False)
    banner_img_url = Column(String, nullable=False)
    avatar_img_url = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, default=datetime.utcnow)
    status = Column(Integer, nullable=False, default=1)
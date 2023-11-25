from typing import Any, List, Annotated
from fastapi import APIRouter, Body, Depends, HTTPException, Form
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from app import controllers, models, schemas
from app.api import deps
from app.core.config import settings
from datetime import timedelta
from app.core import security


router = APIRouter()

@router.get("/send", response_model=List[schemas.StorySessionPrompt])
def send_prompt(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve users.
    """
    users = controllers.user.get_multi(db, skip=skip, limit=limit)
    return users

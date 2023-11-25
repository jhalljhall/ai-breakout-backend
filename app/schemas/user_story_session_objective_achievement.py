from datetime import datetime

from pydantic import BaseModel


# Shared properties
class UserStorySessionObjectiveAchievement(BaseModel):
    id: int = 1
    story_objective_id: int = 1
    user_story_prompt_id: int = 1
    user_id: int = 1
    created: datetime = datetime.utcnow

    # has a user
    # has a story objective
    # has a user story prompt

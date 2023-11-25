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


# Shared properties
class StorySession(BaseModel):
    id: int = 1
    story_id: int = 1
    initial_prompt: str = None
    template: str = None
    objectives: str = None
    endgame: str = None
    created: datetime = datetime.utcnow
    updated: datetime = datetime.utcnow
    status: int = 1

    # has objective items (one to many)
    # has a story (one to one)
    # has achievement items (one to many)
    # has prompt items (one to many)
    # has watchdog items (one to many)


# Shared properties
class UserStoryPrompt(BaseModel):
    id: int = 1
    user_id: int = 1
    story_session_id: int = 1
    prompt: str = None
    created: datetime = datetime.utcnow
    status: int = 1

    # has a user
    # has a story session


# Shared properties
class UserStorySession(BaseModel):
    id: int = 1
    user_id: int = 1
    story_session_id: int = 1
    created: datetime = datetime.utcnow

    # has a user
    # has a story session


# Shared properties
class UserStorySessionObjective(BaseModel):
    id: int = 1
    story_session_id: int = 1
    title: str = None
    created: datetime = datetime.utcnow
    updated: datetime = datetime.utcnow
    status: int = 1

    # has a user
    # has a story session


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



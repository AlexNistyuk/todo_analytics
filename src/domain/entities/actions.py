import enum

from pydantic import BaseModel


class Action(enum.Enum):
    sheet = "sheet"
    task = "task"


class ActionType(enum.Enum):
    create = "create"
    retrieve = "retrieve"
    done = "done"


class ActionCreate(BaseModel):
    action: Action
    name: str
    action_type: ActionType


class ActionRetrieve(ActionCreate):
    id: str
    user_id: int
    created_at: int

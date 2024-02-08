from pydantic import BaseModel

from domain.utils.action_at import ActionAt
from domain.utils.action_types import ActionType


class ActionCreate(BaseModel):
    action_at: ActionAt
    name: str
    action_type: ActionType


class ActionRetrieve(ActionCreate):
    id: str
    user_id: int
    created_at: int

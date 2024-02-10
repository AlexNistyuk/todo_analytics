from pydantic import BaseModel

from domain.utils.action_at import ActionAt
from domain.utils.action_types import ActionType


class Kafka(BaseModel):
    action_at: ActionAt
    name: str
    action_type: ActionType
    user_id: int

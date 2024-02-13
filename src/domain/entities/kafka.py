from pydantic import BaseModel

from domain.enums.base import ActionAt
from domain.enums.sheets import SheetActionType
from domain.enums.tasks import TaskActionType


class KafkaBase(BaseModel):
    name: str
    user_id: int

    class Config:
        use_enum_values = True


class KafkaTask(KafkaBase):
    action_at: str = ActionAt.task.value
    action_type: TaskActionType


class KafkaSheet(KafkaBase):
    action_at: str = ActionAt.sheet.value
    action_type: SheetActionType

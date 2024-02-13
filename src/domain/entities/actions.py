from pydantic import BaseModel

from domain.enums.base import ActionAt
from domain.enums.sheets import SheetActionType
from domain.enums.tasks import TaskActionType


class ActionBase(BaseModel):
    name: str


class ActionCreateTask(ActionBase):
    action_at: ActionAt = ActionAt.task.value
    action_type: TaskActionType

    class Config:
        use_enum_values = True


class ActionCreateSheet(ActionBase):
    action_at: ActionAt = ActionAt.sheet.value
    action_type: SheetActionType

    class Config:
        use_enum_values = True


class ActionRetrieve(ActionBase):
    id: str
    user_id: int
    created_at: int
    action_at: ActionAt
    action_type: TaskActionType | SheetActionType

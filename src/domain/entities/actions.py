from pydantic import BaseModel, field_validator

from domain.enums.base import ActionAt
from domain.enums.sheets import SheetActionType
from domain.enums.tasks import TaskActionType


class ActionBase(BaseModel):
    name: str


class ActionCreateTask(ActionBase):
    action_at: str = ActionAt.task.value
    action_type: TaskActionType

    class Config:
        use_enum_values = True

    @field_validator("action_at", mode="after")
    @staticmethod
    def validate_action_at(value) -> str:
        return ActionAt.task.value


class ActionCreateSheet(ActionBase):
    action_at: str = ActionAt.sheet.value
    action_type: SheetActionType

    class Config:
        use_enum_values = True

    @field_validator("action_at", mode="after")
    @staticmethod
    def validate_action_at(value) -> str:
        return ActionAt.sheet.value


class ActionRetrieve(ActionBase):
    id: str
    user_id: int
    created_at: int
    action_at: ActionAt
    action_type: TaskActionType | SheetActionType

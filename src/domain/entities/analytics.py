from pydantic import BaseModel

from domain.entities.actions import ActionRetrieve


class AnalyticsRetrieve(BaseModel):
    count: int
    actions: list[ActionRetrieve]

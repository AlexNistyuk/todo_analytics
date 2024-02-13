import datetime

import botocore.exceptions
from boto3.dynamodb.conditions import Attr

from domain.exceptions.actions import ActionRetrieveError
from domain.utils.action_types import ActionType
from domain.utils.period import Period, days_period_map
from infrastructure.repositories.interfaces import IRepository


class AnalyticsUseCase:
    def __init__(self, action_repository: IRepository):
        self.repository = action_repository

    @staticmethod
    def __get_date(period: Period) -> int:
        days = days_period_map.get(period, 0)

        return int(
            datetime.datetime.utcnow().timestamp()
            - datetime.timedelta(days=days).total_seconds()
        )

    async def get_all_actions(self, user_id: int, period: Period) -> dict:
        try:
            date = self.__get_date(period)
            filters = Attr("created_at").gte(date) and Attr("user_id").eq(user_id)

            result = await self.repository.get_by_filters(filters)

            return self.__get_result(result)
        except botocore.exceptions.ClientError:
            raise ActionRetrieveError

    async def get_tasks(self, user_id: int, period: Period) -> dict:
        try:
            date = self.__get_date(period)
            filters = (
                Attr("created_at").gte(date)
                and Attr("user_id").eq(user_id)
                and Attr("action_at").eq("task")
            )

            result = await self.repository.get_by_filters(filters)

            return self.__get_result(result)
        except botocore.exceptions.ClientError:
            raise ActionRetrieveError

    async def get_action_tasks(
        self, user_id: int, action_type: ActionType, period: Period
    ) -> dict:
        try:
            date = self.__get_date(period)
            filters = (
                Attr("created_at").gte(date)
                and Attr("user_id").eq(user_id)
                and Attr("action_type").eq(action_type.value)
                and Attr("action_at").eq("task")
            )

            result = await self.repository.get_by_filters(filters)

            return self.__get_result(result)
        except botocore.exceptions.ClientError:
            raise ActionRetrieveError

    async def get_sheets(self, user_id: int, period: Period) -> dict:
        try:
            date = self.__get_date(period)
            filters = (
                Attr("created_at").gte(date)
                and Attr("user_id").eq(user_id)
                and Attr("action_at").eq("sheet")
            )

            result = await self.repository.get_by_filters(filters)

            return self.__get_result(result)
        except botocore.exceptions.ClientError:
            raise ActionRetrieveError

    async def get_action_sheets(
        self, user_id: int, action_type: ActionType, period: Period
    ) -> dict:
        try:
            date = self.__get_date(period)
            filters = (
                Attr("created_at").gte(date)
                and Attr("user_id").eq(user_id)
                and Attr("action_type").eq(action_type.value)
                and Attr("action_at").eq("sheet")
            )

            result = await self.repository.get_by_filters(filters)

            return self.__get_result(result)
        except botocore.exceptions.ClientError:
            raise ActionRetrieveError

    @staticmethod
    def __get_result(result) -> dict:
        return {"count": result.get("Count", 0), "actions": result.get("Items", [])}

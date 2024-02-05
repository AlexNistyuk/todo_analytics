import datetime

import botocore.exceptions
from boto3.dynamodb.conditions import Attr

from domain.exceptions.actions import ActionRetrieveError
from infrastructure.repositories.actions import ActionRepository


class AnalyticsUseCase:
    repository = ActionRepository()

    async def get_week_actions(self) -> list:
        try:
            date = int(
                datetime.datetime.utcnow().timestamp()
                - datetime.timedelta(days=7).total_seconds()
            )
            filters = Attr("created_at").gte(date)

            return await self.repository.get_by_filters(filters)["Items"]
        except botocore.exceptions.ClientError:
            raise ActionRetrieveError

import faker
import pytest

from domain.enums.base import Period
from domain.enums.sheets import SheetActionType
from domain.enums.tasks import TaskActionType


class TestSheet:
    url = "api/v1/analytics/"

    def setup_method(self):
        self.fake = faker.Faker()

    @pytest.mark.asyncio
    async def test_list_all_actions_ok(
        self, client, mock_admin_permission, mock_action_repo
    ):
        response = client.get(url=f"{self.url}", params={"period": Period.week.value})

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_list_all_actions_with_user_permission(
        self, client, mock_user_permission, mock_action_repo
    ):
        response = client.get(
            url=f"{self.url}",
            params={"period": Period.week.value, "user_id": self.fake.pyint()},
        )

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_list_task_actions_ok(
        self, client, mock_admin_permission, mock_action_repo
    ):
        response = client.get(
            url=f"{self.url}tasks/",
            params={
                "period": Period.week.value,
                "action_type": TaskActionType.done.value,
            },
        )

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_list_task_actions_with_user_permission(
        self, client, mock_user_permission, mock_action_repo
    ):
        response = client.get(
            url=f"{self.url}tasks/",
            params={
                "period": Period.week.value,
                "action_type": TaskActionType.done.value,
                "user_id": self.fake.pyint(),
            },
        )

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_list_sheet_actions_ok(
        self, client, mock_admin_permission, mock_action_repo
    ):
        response = client.get(
            url=f"{self.url}sheets/",
            params={
                "period": Period.week.value,
                "action_type": SheetActionType.retrieve.value,
            },
        )

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_list_sheet_actions_with_user_permission(
        self, client, mock_user_permission, mock_action_repo
    ):
        response = client.get(
            url=f"{self.url}sheets/",
            params={
                "period": Period.week.value,
                "action_type": SheetActionType.retrieve.value,
                "user_id": self.fake.pyint(),
            },
        )

        assert response.status_code == 403

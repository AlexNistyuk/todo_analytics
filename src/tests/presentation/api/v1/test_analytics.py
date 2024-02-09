import faker
import pytest

from domain.utils.action_types import ActionType
from domain.utils.period import Period
from tests.conftest import client


class TestSheet:
    url = "api/v1/analytics"

    def setup_method(self):
        self.fake = faker.Faker()

    @pytest.mark.asyncio
    async def test_list_all_actions_ok(self, mock_admin_permission, mock_action_repo):
        response = client.get(
            url=f"{self.url}/{self.fake.pyint()}", params={"period": Period.week.value}
        )

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_list_all_actions_with_user_permission(
        self, mock_user_permission, mock_action_repo
    ):
        response = client.get(
            url=f"{self.url}/{self.fake.pyint()}", params={"period": Period.week.value}
        )

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_list_task_actions_ok(self, mock_admin_permission, mock_action_repo):
        response = client.get(
            url=f"{self.url}/{self.fake.pyint()}/tasks",
            params={"period": Period.week.value, "action_type": ActionType.done.value},
        )

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_list_task_actions_with_user_permission(
        self, mock_user_permission, mock_action_repo
    ):
        response = client.get(
            url=f"{self.url}/{self.fake.pyint()}/tasks",
            params={"period": Period.week.value, "action_type": ActionType.done.value},
        )

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_list_sheet_actions_ok(self, mock_admin_permission, mock_action_repo):
        response = client.get(
            url=f"{self.url}/{self.fake.pyint()}/sheets",
            params={"period": Period.week.value, "action_type": ActionType.done.value},
        )

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_list_sheet_actions_with_user_permission(
        self, mock_user_permission, mock_action_repo
    ):
        response = client.get(
            url=f"{self.url}/{self.fake.pyint()}/sheets",
            params={"period": Period.week.value, "action_type": ActionType.done.value},
        )

        assert response.status_code == 403

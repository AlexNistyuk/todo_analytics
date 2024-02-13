import faker
import pytest

from domain.enums.base import ActionAt
from tests.factories import ActionFactory


class TestSheet:
    url = "api/v1/actions"

    def setup_method(self):
        self.new_task_action = ActionFactory(ActionAt.task.value)
        self.new_sheet_action = ActionFactory(ActionAt.sheet.value)
        self.fake = faker.Faker()

    @pytest.mark.asyncio
    async def test_list_ok(self, client, mock_admin_permission, mock_action_repo):
        response = client.get(url=self.url)

        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert isinstance(response.json()[0], dict)

    @pytest.mark.asyncio
    async def test_list_with_user_permission(
        self, client, mock_user_permission, mock_action_repo
    ):
        response = client.get(url=self.url)

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_create_task_ok(
        self, client, mock_admin_permission, mock_action_repo
    ):
        response = client.post(
            url=f"{self.url}/tasks", json=self.new_task_action.dump_create()
        )

        assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_create_task_with_user_permission(
        self, client, mock_user_permission, mock_action_repo
    ):
        response = client.post(
            url=f"{self.url}/tasks", json=self.new_task_action.dump_create()
        )

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_create_sheet_ok(
        self, client, mock_admin_permission, mock_action_repo
    ):
        response = client.post(
            url=f"{self.url}/sheets", json=self.new_sheet_action.dump_create()
        )

        assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_create_sheet_with_user_permission(
        self, client, mock_user_permission, mock_action_repo
    ):
        response = client.post(
            url=f"{self.url}/sheets", json=self.new_sheet_action.dump_create()
        )

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_retrieve_ok(self, client, mock_user_permission, mock_action_repo):
        response = client.get(
            url=f"{self.url}/{self.fake.pyint()}",
        )

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_update_task_ok(
        self, client, mock_admin_permission, mock_action_repo
    ):
        response = client.put(
            url=f"{self.url}/tasks/{self.fake.pyint()}",
            json=self.new_task_action.dump_create(),
        )

        assert response.status_code == 204

    @pytest.mark.asyncio
    async def test_update_task_with_user_permission(
        self, client, mock_user_permission, mock_action_repo
    ):
        response = client.put(
            url=f"{self.url}/tasks/{self.fake.pyint()}",
            json=self.new_task_action.dump_create(),
        )

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_update_sheet_ok(
        self, client, mock_admin_permission, mock_action_repo
    ):
        response = client.put(
            url=f"{self.url}/sheets/{self.fake.pyint()}",
            json=self.new_sheet_action.dump_create(),
        )

        assert response.status_code == 204

    @pytest.mark.asyncio
    async def test_update_sheet_with_user_permission(
        self, client, mock_user_permission, mock_action_repo
    ):
        response = client.put(
            url=f"{self.url}/sheets/{self.fake.pyint()}",
            json=self.new_sheet_action.dump_create(),
        )

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_delete_ok(self, client, mock_admin_permission, mock_action_repo):
        response = client.delete(
            url=f"{self.url}/{self.fake.pyint()}",
        )

        assert response.status_code == 204

    @pytest.mark.asyncio
    async def test_delete_with_user_permission(
        self, client, mock_user_permission, mock_action_repo
    ):
        response = client.delete(
            url=f"{self.url}/{self.fake.pyint()}",
        )

        assert response.status_code == 403

import faker
import pytest

from tests.factories import ActionFactory


class TestSheet:
    url = "api/v1/actions"

    def setup_method(self):
        self.new_action = ActionFactory()
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
    async def test_create_ok(self, client, mock_admin_permission, mock_action_repo):
        response = client.post(url=self.url, json=self.new_action.dump_create())

        assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_create_with_user_permission(
        self, client, mock_user_permission, mock_action_repo
    ):
        response = client.post(url=self.url, json=self.new_action.dump_create())

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_retrieve_ok(self, client, mock_user_permission, mock_action_repo):
        response = client.get(
            url=f"{self.url}/{self.fake.pyint()}",
        )

        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.asyncio
    async def test_update_ok(self, client, mock_admin_permission, mock_action_repo):
        response = client.put(
            url=f"{self.url}/{self.fake.pyint()}", json=self.new_action.dump_create()
        )

        assert response.status_code == 204

    @pytest.mark.asyncio
    async def test_update_with_user_permission(
        self, client, mock_user_permission, mock_action_repo
    ):
        response = client.put(
            url=f"{self.url}/{self.fake.pyint()}", json=self.new_action.dump_create()
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

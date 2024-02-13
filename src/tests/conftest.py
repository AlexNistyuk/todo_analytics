import faker
import pytest
from starlette.testclient import TestClient

from domain.enums.base import ActionAt
from domain.enums.users import UserRole
from main import app
from tests.factories import ActionFactory, UserFactory

fake = faker.Faker()


@pytest.fixture()
def client(mock_db_manager):
    with TestClient(app=app) as client:
        yield client


def mock_user(user, mocker):
    mocker.patch(
        "infrastructure.utils.user.UserInfo.get_user_info", return_value=user.dump()
    )


@pytest.fixture()
def mock_admin_permission(mocker):
    user = UserFactory(UserRole.admin.value)
    mock_user(user, mocker)


@pytest.fixture()
def mock_user_permission(mocker):
    user = UserFactory(UserRole.user.value)
    mock_user(user, mocker)


@pytest.fixture()
def mock_action_repo(mocker):
    repo_path = "infrastructure.repositories.actions.ActionRepository"
    action = {"Items": [ActionFactory(ActionAt.task.value).dump()], "Count": 1}

    mocker.patch(f"{repo_path}.create", return_value=None)
    mocker.patch(f"{repo_path}.update_by_id", return_value=None)
    mocker.patch(f"{repo_path}.get_all", return_value=action)
    mocker.patch(f"{repo_path}.get_by_id", return_value=action)
    mocker.patch(f"{repo_path}.get_by_filters", return_value=action)
    mocker.patch(f"{repo_path}.delete_by_id", return_value=None)


@pytest.fixture()
def mock_db_manager(mocker):
    manager_path = "infrastructure.managers.database.DatabaseManager"

    mocker.patch(f"{manager_path}.connect", return_value=None)
    mocker.patch(f"{manager_path}.close", return_value=None)

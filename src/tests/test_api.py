import pytest
import schemathesis

from main import app


@pytest.fixture()
def web_app(mock_db_manager, mock_admin_permission, mock_action_repo):
    app.openapi_version = "3.0.0"

    return schemathesis.from_dict(app.openapi())


schema = schemathesis.from_pytest_fixture("web_app")


@pytest.mark.schemathesis
@schema.parametrize()
def test_api(case):
    response = case.call_asgi(app)
    case.validate_response(response)

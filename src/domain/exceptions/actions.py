from starlette.status import HTTP_400_BAD_REQUEST

from domain.exceptions.base import BaseHTTPException


class ActionNotFoundError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Action not found"


class ActionCreateError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while creating action"


class ActionUpdateError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while updating action"


class ActionRetrieveError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while retrieving action"


class ActionDeleteError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while deleting action"

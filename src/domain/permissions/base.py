from starlette.requests import Request

from domain.exceptions.user import UserPermissionDenied
from domain.permissions.interfaces import IPermission


class BasePermission(IPermission):
    """Base permission"""

    async def __call__(self, request: Request):
        self.user = request.state.user

        user_role = self.user.get("role")
        if not user_role:
            raise UserPermissionDenied

        result = await self.has_permission(user_role)
        if not result:
            raise UserPermissionDenied
        return self

    async def check_object_permission(self, user_id: int):
        result = await self.has_object_permission(user_id)
        if not result:
            raise UserPermissionDenied

    async def has_object_permission(self, *args, **kwargs):
        return True

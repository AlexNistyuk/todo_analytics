from domain.enums.users import UserRole
from domain.permissions.base import BasePermission
from infrastructure.config import get_settings

settings = get_settings()


class IsAdmin(BasePermission):
    async def has_permission(self, user_role: str) -> bool:
        return user_role == UserRole.admin.value


class IsAdminOrIsOwner(BasePermission):
    async def has_permission(self, user_role: str) -> bool:
        return True

    async def has_object_permission(self, user_id: int):
        return (
            self.user.get("role") == UserRole.admin.value
            or self.user.get("id") == user_id
        )

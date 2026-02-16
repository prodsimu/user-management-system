from typing import Optional

from models.user import User
from services.user_service import UserService


class Seed:

    def __init__(self, user_service: UserService) -> None:
        self.user_service: UserService = user_service

    def run_seed(self) -> Optional[User]:
        if self.user_service.list_users():
            return None

        admin = self.user_service.create_user("admin", "admin", "admin123")
        self.user_service.change_role_by_id(admin.id, "admin")

        return admin

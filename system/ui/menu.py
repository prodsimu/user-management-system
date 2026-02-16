from typing import Any
from models.user import User
from models.session import Session
from services.user_service import UserService
from services.session_service import SessionService


class Output:

    def __init__(
        self,
        user_service: UserService,
        session_service: SessionService,
    ) -> None:
        self.user_service: UserService = user_service
        self.session_service: SessionService = session_service

    def start_system(self, seed: dict[str, Any]) -> None:
        print(
            "That's the first system initialization\n"
            + "The system will create a initial admin user\n"
        )
        print(f"Name = {seed.name}")
        print(f"Username = {seed.username}")
        print(f"Password = {seed.password}")


class input:
    pass

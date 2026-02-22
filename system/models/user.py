from typing import Any
from security.password_hasher import PasswordHasher


class User:

    def __init__(
        self,
        id: int,
        name: str,
        username: str,
        password: str,
        role: str,
        active: bool,
        login_attempts: int,
    ) -> None:

        self.id: int = id
        self.name: str = name
        self.username: str = username
        self.password: str = password
        self.role: str = role
        self.active: bool = active
        self.login_attempts: int = login_attempts

    def __repr__(self) -> str:
        return (
            f"id={self.id} "
            + f"\nname={self.name} "
            + f"\nusername={self.username} "
            + f"\npassword={self.password} "
            + f"\nrole={self.role} "
            + f"\nactive={self.active} "
            + f"\nlogin_attempts={self.login_attempts}"
        )

    def change_password(self, new_password: str) -> None:
        self.password = new_password

    def increment_login_attempts(self) -> None:
        self.login_attempts += 1

    def reset_login_attempts(self) -> None:
        self.login_attempts = 0

    def activate(self) -> None:
        self.active = True
        self.reset_login_attempts()

    def deactivate(self) -> None:
        self.active = False

    def change_role(self, new_role: str) -> None:
        self.role = new_role

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "active": self.active,
            "login_attempts": self.login_attempts,
        }

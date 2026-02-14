from typing import Optional, List
from models.user import User
from repositories.user_repository import UserRepository


class UserService:

    MAX_LOGIN_ATTEMPTS = 3

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, new_name: str, new_username: str, new_password: str) -> User:

        if new_name is None or new_username is None or new_password is None:
            raise ValueError("User cannot be created: missing required fields")

        new_name = new_name.strip()
        new_username = new_username.strip()

        if not new_name:
            raise ValueError("Name cannot be empty")

        if not new_username:
            raise ValueError("Username cannot be empty")

        if len(new_password) < 6:
            raise ValueError("Password must be at least 6 characters long")

        if self.user_repository.exists_by_field("username", new_username):
            raise ValueError("Username already exists")

        new_user = User(
            id=self.user_repository.get_next_id(),
            name=new_name,
            username=new_username,
            password=new_password,
            role="user",
            active=True,
            login_attempts=0,
        )

        self.user_repository.add(new_user)

        return new_user

    def login(self, username: str, password: str) -> bool:

        if not username or not password:
            raise ValueError("Username and password required")

        user = self.user_repository.get_by_field("username", username)

        if not user:
            return False

        if not user.active:
            raise PermissionError("User is blocked")

        if not user.verify_password(password):
            user.increment_login_attempts()

            if user.login_attempts >= self.MAX_LOGIN_ATTEMPTS:
                user.deactivate()
                raise PermissionError("User blocked due to too many attempts")

            return False

        user.reset_login_attempts()
        return True

    def get_user_by_username(self, username: str) -> Optional[User]:
        if not username:
            return None

        return self.user_repository.get_by_field("username", username)

    def list_users(self) -> list[User]:
        return self.user_repository.get_all()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_by_field("id", user_id)

    def delete_user_by_id(self, id):
        user = self.get_user_by_id(id)

        if not user:
            return False

        self.user_repository.delete(id)
        return True

    def update_username_by_id(self, id: int, new_username: str) -> bool:
        user = self.get_user_by_id(id)

        if not user:
            return False

        if not new_username or not new_username.strip():
            return False

        self.user_repository.update_by_id(id, new_username)
        return True

from typing import Optional, List
from models.user import User
from models.session import Session
from repositories.user_repository import UserRepository
from services.session_service import SessionService


class UserService:

    MAX_LOGIN_ATTEMPTS = 3
    VALID_ROLES = {"user", "admin"}

    def __init__(
        self, user_repository: UserRepository, session_service: SessionService
    ):
        self.user_repository = user_repository
        self.session_service = session_service

    # CREATE

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

    # READ

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_by_field("id", user_id)

    def get_user_by_username(self, username: str) -> Optional[User]:
        if not username:
            return None

        return self.user_repository.get_by_field("username", username)

    def list_users(self) -> List[User]:
        return self.user_repository.get_all()

    def list_active_users(self) -> List[User]:
        return self.user_repository.get_active_users()

    def list_inactive_users(self) -> List[User]:
        return self.user_repository.get_inactive_users()

    # UPDATE

    def update_username_by_id(self, user_id: int, new_username: str) -> bool:
        user = self.get_user_by_id(user_id)

        if not user:
            return False

        if not new_username:
            return False

        new_username = new_username.strip()

        if not new_username:
            return False

        if self.user_repository.exists_by_field("username", new_username):
            return False

        data = {"username": new_username}
        self.user_repository.update_by_id(user_id, data)
        return True

    def update_password_by_id(self, user_id: int, new_password: str) -> bool:
        user = self.get_user_by_id(user_id)

        if not user:
            return False

        if not new_password:
            return False

        new_password = new_password.strip()

        if not new_password:
            return False

        if len(new_password) < 6:
            raise ValueError("Password must be at least 6 characters long")

        if user.verify_password(new_password):
            return False

        user.change_password(new_password)
        return True

    def activate_user_by_id(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)

        if not user:
            return False

        if user.active:
            return False

        user.activate()
        return True

    def deactivate_user_by_id(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)

        if not user:
            return False

        if not user.active:
            return False

        user.deactivate()
        return True

    def change_role_by_id(self, user_id: int, new_role: str) -> bool:
        user = self.get_user_by_id(user_id)

        if not user:
            return False

        if not new_role or not new_role.strip():
            return False

        new_role = new_role.strip().lower()

        if new_role not in self.VALID_ROLES:
            return False

        if user.role == new_role:
            return False

        user.change_role(new_role)
        return True

    # DELETE

    def delete_user_by_id(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)

        if not user:
            return False

        self.user_repository.delete(user_id)
        return True

    # AUTH / BUSINESS RULES

    def login(self, username: str, password: str) -> Optional[Session]:

        if not username or not password:
            raise ValueError("Username and password required")

        user = self.user_repository.get_by_field("username", username)

        if not user:
            return None

        if not user.active:
            raise PermissionError("User is blocked")

        if not user.verify_password(password):
            user.increment_login_attempts()

            if user.login_attempts >= self.MAX_LOGIN_ATTEMPTS:
                user.deactivate()
                raise PermissionError("User blocked due to too many attempts")

            return None

        user.reset_login_attempts()

        return self.session_service.create_session(user.id)

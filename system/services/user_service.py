from typing import Optional, List
from models.user import User
from models.session import Session
from repositories.user_repository import UserRepository
from services.session_service import SessionService
from exceptions.exceptions import *


class UserService:

    MAX_LOGIN_ATTEMPTS = 3
    VALID_ROLES = {"user", "admin"}

    def __init__(
        self, user_repository: UserRepository, session_service: SessionService
    ) -> None:
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

    def update_name_by_id(self, user_id: int, new_name: str) -> None:
        user = self.get_user_by_id(user_id)

        if not user:
            raise UserNotFoundError("User not found")

        if not new_name:
            raise InvalidNameError("Invalid name")

        new_name = new_name.strip()

        if not new_name:
            raise InvalidNameError("Invalid name")

        data = {"name": new_name}
        self.user_repository.update_by_id(user_id, data)

    def update_username_by_id(self, user_id: int, new_username: str) -> None:
        user = self.get_user_by_id(user_id)

        if not user:
            raise UserNotFoundError("User not found")

        if not new_username:
            raise InvalidUsernameError("Invalid username")

        new_username = new_username.strip()

        if not new_username:
            raise InvalidUsernameError("Invalid username")

        if self.user_repository.exists_by_field("username", new_username):
            raise UsernameAlreadyExistsError("User already exists")

        data = {"username": new_username}
        self.user_repository.update_by_id(user_id, data)

    def update_password_by_id(self, user_id: int, new_password: str) -> None:
        user = self.get_user_by_id(user_id)
        if not user:
            raise UserNotFoundError()

        if not new_password or not new_password.strip():
            raise InvalidPasswordError("Password cannot be empty")

        new_password = new_password.strip()

        if len(new_password) < 6:
            raise InvalidPasswordError("Password must have at least 6 characters")

        if user.verify_password(new_password):
            raise SamePasswordError("New password cannot be the same as current")

        user.change_password(new_password)

    def activate_user_by_id(self, user_id: int) -> None:
        user = self.get_user_by_id(user_id)

        if not user:
            raise UserNotFoundError("User not found")

        if user.active:
            raise UserAlreadyActiveError("User already active")

        user.activate()

    def deactivate_user_by_id(self, user_id: int) -> None:
        user = self.get_user_by_id(user_id)

        if not user:
            raise UserNotFoundError("User not found")

        if not user.active:
            raise UsernameAlreadyDeactiveError("User already deactive")

        user.deactivate()

    def change_role_by_id(self, user_id: int, new_role: str) -> None:
        user = self.get_user_by_id(user_id)

        if not user:
            raise UserNotFoundError("User not found")

        if not new_role or not new_role.strip():
            raise InvalidRoleError("Invalid role")

        new_role = new_role.strip().lower()

        if new_role not in self.VALID_ROLES:
            raise InvalidRoleError("Invalid role")

        if user.role == new_role:
            raise InvalidRoleError(f"Role already {new_role}")

        user.change_role(new_role)

    # DELETE

    def delete_user_by_id(self, user_id: int) -> None:
        user = self.get_user_by_id(user_id)

        if not user:
            raise UserNotFoundError("User not found")

        self.user_repository.delete(user_id)
        self.session_service.delete_all_user_sessions(user_id)

    # AUTH / BUSINESS RULES

    def login(self, username: str, password: str) -> Session:

        if not username or not password:
            raise EmptyLoginCredentialsError("Username and password required")

        user = self.user_repository.get_by_field("username", username)

        if not user:
            raise UserNotFoundError("User not found")

        if not user.active:
            raise InactiveUserError("User is blocked")

        if not user.verify_password(password):
            user.increment_login_attempts()

            if user.login_attempts >= self.MAX_LOGIN_ATTEMPTS:
                user.deactivate()
                raise InactiveUserError("User blocked due to too many attempts")

            raise InvalidPasswordError("Incorrect password")

        user.reset_login_attempts()

        return self.session_service.create_session(user.id)

    def get_user_by_session_id(self, session_id: str) -> Optional[User]:
        session = self.session_service.get_valid_session(session_id)

        if not session:
            return None

        return self.get_user_by_id(session.user_id)

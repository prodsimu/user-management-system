from models.user import User
from repositories.user_repository import UserRepository

class UserService:

    MAX_LOGIN_ATTEMPTS = 3

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository


    def create_user(self, new_name: str, new_username: str, new_password: str):

        if self.user_repository.exists_by_field("username", new_username):
            return False

        new_user = User(
            id = self.user_repository.get_next_id(),
            name = new_name,
            username = new_username,
            password = new_password,
            role = "user",
            active = True,
            login_attempts = 0
        )

        self.user_repository.add(new_user)

        return new_user


    def login(self, username: str, password: str):

        verify_user = self.user_repository.get_by_field("username", username)

        if not verify_user:
            return False

        if not verify_user.active:
            return f"{verify_user.username} is blocked."

        if not verify_user.verify_password(password):
        
            verify_user.increment_login_attempts()
            
            if verify_user.login_attempts >= self.MAX_LOGIN_ATTEMPTS:
                verify_user.deactivate()

            return False

        verify_user.reset_login_attempts()
        return True


    def get_user_by_username(self, username: str):
        user = self.user_repository.get_by_field("username", username)

        return user if user else None
    

    def list_users(self):
        return self.user_repository.get_all()


    def get_user_by_id(self, id: int):
        user = self.user_repository.get_by_field("id", id)

        return user if user else None

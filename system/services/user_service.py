from models.user import User
from repositories.user_repository import UserRepository

class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository


    def create_user(self, new_name, new_username, new_password):

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

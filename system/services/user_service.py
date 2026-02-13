from models.user import User
from repositories.user_repository import UserRepository

class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository


    def create_user(self, name, username, password):
        
        pass
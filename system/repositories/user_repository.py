from database.database import Database
from models.user import User
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self, database: Database):
        super().__init__(database, "users")


    def get_user_by_username(self, username: str):
        for user in self.collection:
            if user.username == username:
                return user
            
        return None
    

    def update_user(self, user_id: int, new_username: str = None, new_password: str = None):
        user = self.get_by_id(user_id)

        if not user:
            return False

        if new_username is not None:
            user.username = new_username

        if new_password is not None:
            user.password = new_password

        return True

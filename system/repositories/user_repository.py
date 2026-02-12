from database.database import Database
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self, database: Database):
        super().__init__(database, "users")


    def get_user_by_username(self, username: str):
        for user in self.collection:
            if user.username == username:
                return user
            
        return None
    

    def exists_by_username(self, username: str):
        return any(user.username == username for user in self.collection)

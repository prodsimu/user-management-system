from database.database import Database
from user.user import User


class UserRepository:
    def __init__(self, database: Database):
        self.database = database


    def add_user(self, user: User):
        self.database.users.append(user)


    def get_all_users(self):
        return self.database.users

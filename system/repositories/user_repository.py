from database.database import Database
from user.user import User


class UserRepository:
    def __init__(self, database: Database):
        self.database = database


    def add_user(self, user: User):
        self.database.users.append(user)


    def get_all_users(self):
        return self.database.users


    def get_next_id(self):
        if not self.database.users:
            return 1
        
        last_id = self.database.users[-1].id
        return last_id + 1
    

    
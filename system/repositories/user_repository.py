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
    

    def get_user_by_id(self, user_id: int):
        for user in self.database.users:
            if user.id == user_id:
                return user
            
        return None
    

    def get_user_by_username(self, username: str):
        for user in self.database.users:
            if user.username == username:
                return user
            
        return None
    

    def delete_user(self, user_id: int):
        users = self.database.users

        for i, user in enumerate(users):
            if user.id == user_id:
                users.pop(i)
                return True

        return False
    

    def update_user(self, user_id: int, new_username: str = None, new_password: str = None):
        user = self.get_user_by_id(user_id)

        if not user:
            return False

        if new_username is not None:
            user.username = new_username

        if new_password is not None:
            user.password = new_password

        return True
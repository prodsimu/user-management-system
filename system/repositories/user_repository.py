from database.database import Database
from user.user import User


class UserRepository:
    def __init__(self, database: Database):
        self.database = database
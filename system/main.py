from user.user import User
from database.database import Database
from repositories.user_repository import UserRepository

db = Database()
repo = UserRepository(db)


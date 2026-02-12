from database.database import Database
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self, database: Database):
        super().__init__(database, "users")

from typing import List

from models.user import User
from database.database import Database
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self, database: Database) -> None:
        super().__init__(database, "users")

    def get_active_users(self) -> List[User]:
        active_list = []

        for user in self.collection:
            if user.active:
                active_list.append(user)

        return active_list

    def get_inactive_users(self) -> List[User]:
        inactive_list = []

        for user in self.collection:
            if not user.active:
                inactive_list.append(user)

        return inactive_list

from database.database import Database
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self, database: Database):
        super().__init__(database, "users")

    def get_active_users(self):
        active_list = []

        for user in self.collection:
            if user.active:
                active_list.append(user)

        return active_list

    def get_inactive_users(self):
        inactive_list = []

        for user in self.collection:
            if not user.active:
                inactive_list.append(user)

        return inactive_list

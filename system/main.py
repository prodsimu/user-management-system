from user.user import User
from database.database import Database
from repositories.user_repository import UserRepository

db = Database()
repo = UserRepository(db)

new_id1 = repo.get_next_id()
user1 = User(new_id1, "jose", "jose123", "123456", "user", True, 0)
repo.add_user(user1)

new_id2 = repo.get_next_id()
user2 = User(new_id2, "jorge", "jorge123", "abcdef", "user", True, 0)
repo.add_user(user2)

new_id3 = repo.get_next_id()
user3 = User(new_id3, "sandro", "ehsjose", "nonono", "user", True, 0)
repo.add_user(user3)

print(repo.get_all_users())
print("------------------------------")

repo.delete_user(2)

print(repo.get_all_users())
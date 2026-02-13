from database.database import Database
from repositories.user_repository import UserRepository
from services.user_service import UserService

db = Database()

user_repo = UserRepository(db)

user_service = UserService(user_repo)

print("\nCREATE USER")
user = user_service.create_user("Inacio", "inacio", "123")
print(user)

print("\nCORRECT LOGIN")
print(user_service.login("inacio", "123"))

print("\nWRONG LOGIN")
print(user_service.login("inacio", "999"))
print(user_service.login("inacio", "999"))
print(user_service.login("inacio", "999"))

print("\nTRY LOGIN AFTER BLOCKED")
print(user_service.login("inacio", "123"))

print("\nUSER FINAL STAGE")
u = user_repo.get_by_field("username", "inacio")
print("Active:", u.active)
print("Attempts:", u.login_attempts)

get_user_by_username_1 = user_service.get_user_by_username("inacio")
get_user_by_username_2 = user_service.get_user_by_username("joao")

print(f"\n{get_user_by_username_1}")
print(f"{get_user_by_username_2}")

print(f"\n{user_service.list_users()}")
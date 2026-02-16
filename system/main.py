from database.database import Database
from repositories.session_repository import SessionRepository
from repositories.user_repository import UserRepository
from services.session_service import SessionService
from services.user_service import UserService

db = Database()

session_repository = SessionRepository(db)
user_repo = UserRepository(db)

session_service = SessionService(session_repository)
user_service = UserService(user_repo, session_service)

print("---------- CREATE USER ----------")
user_1 = user_service.create_user("Inacio", "inacio", "123456")
print(f"\n{user_1}")
user_2 = user_service.create_user("Joao", "joao", "123456")
print(f"\n{user_2}")
user_3 = user_service.create_user("Jose", "jose", "123456")
print(f"\n{user_3}")


print("\n---------- LOGIN ----------")
print("CORRECT LOGIN: ", end="")
print(user_service.login("inacio", "123456"))

try:
    print("\nLOGIN WITHOUT PASSWORD: ", end="")
    print(user_service.login("inacio", ""))
except:
    print("Username and password required")

print("\n1º WRONG LOGIN: ", end="")
print(user_service.login("inacio", "999999"))
print("2º WRONG LOGIN: ", end="")
print(user_service.login("inacio", "999999"))

try:
    print("3º WRONG LOGIN: ", end="")
    print(user_service.login("inacio", "999999"))
except:
    print("User blocked due to too many attempts")

try:
    print("\nLOGIN AFTER BLOCKED: ", end="")
    print(user_service.login("inacio", "123456"))
except:
    print("User is blocked")


print("\n---------- GET USER BY USERNAME ----------")
print(f"WITHOUT USERNAME: {user_service.get_user_by_username("")}")
print(f"USERNAME DOES NOT EXIST: {user_service.get_user_by_username("atanasio")}")
print(f"\n{user_service.get_user_by_username("inacio")}")


print("\n---------- LIST USERS ----------")
print(user_service.list_users())


print("\n---------- GET USER BY ID ----------")
print(f"{user_service.get_user_by_id(1)}")
print(f"\nID DOES NOT EXIST: {user_service.get_user_by_id(4)}")


print("\n---------- DELETE USER BY ID ----------")
print(f"ID DOES EXIST: {user_service.delete_user_by_id(2)}")
print(f"ID DOES NOT EXIST: {user_service.delete_user_by_id(4)}")
print(f"\nLIST AFTER DELETION:\n\n{user_service.list_users()}")


print("\n---------- UPDATE USERNAME BY ID ----------")
print(f"ID DOES EXIST: {user_service.update_username_by_id(1, "pedro")}")
print(f"ID DOES NOT EXIST: {user_service.update_username_by_id(4, "pedro")}")


print("\n---------- UPDATE PASSWORD BY ID ----------")
try:
    print("NEW PASSWORD IS SHORT: ", end="")
    print(f"{user_service.update_password_by_id(1, "99999")}")
except:
    print("Password must be at least 6 characters long")
print(f"ID DOES NOT EXIST: {user_service.update_password_by_id(4, "999999")}")
print(
    f"NEW PASSWORD WITH CORRECT PARAMETERS: {user_service.update_password_by_id(3, "999999")}"
)

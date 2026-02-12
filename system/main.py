from models.user import User
from database.database import Database
from repositories.user_repository import UserRepository


db = Database()
repo = UserRepository(db)


user_1 = User(
    id=repo.get_next_id(),
    name="Inacio",
    username="inacio",
    password="123",
    role="admin",
    active=False,
    login_attempts=0
)

repo.add(user_1)

user_2 = User(
    id=repo.get_next_id(),
    name="Joao",
    username="joao",
    password="123",
    role="admin",
    active=False,
    login_attempts=0
)

repo.add(user_2)

user_3 = User(
    id=repo.get_next_id(),
    name="Pedro",
    username="pedro",
    password="123",
    role="admin",
    active=False,
    login_attempts=0
)

repo.add(user_3)


active_users = repo.get_active_users()

print(active_users)
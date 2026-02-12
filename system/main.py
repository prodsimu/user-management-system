from models.user import User
from database.database import Database
from repositories.user_repository import UserRepository


db = Database()
repo = UserRepository(db)


user = User(
    id=repo.get_next_id(),
    name="Inacio",
    username="inacio",
    password="123",
    role="admin",
    active=True,
    login_attempts=0
)

repo.add(user)


repo.update_by_id(1, {
    "active": "False",
    "id": 999,
    "name": "Joao",
    "username": "joao"
})


print(repo.collection)

from typing import List
from models.user import User
from models.session import Session


class Database:
    def __init__(self) -> None:
        self.users: List[User] = []
        self.sessions: List[Session] = []

from typing import Optional
from repositories.session_repository import SessionRepository
from models.session import Session


class SessionService:

    def __init__(self, session_repository: SessionRepository):
        self.session_repository = session_repository

    def create_session(self, user_id: int) -> None:
        new_session = Session(user_id)
        self.session_repository.add(new_session)

        return new_session

    def get_valid_session(self, session_id) -> Optional[dict]:
        return self.session_repository.get_valid_session_by_id(session_id)

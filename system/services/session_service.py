from repositories.session_repository import SessionRepository
from models.session import Session


class SessionService:

    def __init__(self, session_repository: SessionRepository):
        self.session_repository = session_repository

    def create_session(self, user_id: int) -> None:
        new_session = Session(user_id)
        self.session_repository.add(new_session)

        return new_session

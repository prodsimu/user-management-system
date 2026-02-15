from typing import Optional
from models.session import Session
from database.database import Database
from repositories.base_repository import BaseRepository


class SessionRepository(BaseRepository):
    def __init__(self, database: Database):
        super().__init__(database, "sessions")

    def get_valid_session_by_id(self, session_id: str) -> Optional[Session]:
        for session in self.collection:
            if session.id == session_id:

                if not session.active:
                    return None

                if session.is_expired():
                    session.invalidate()
                    return None

                return session

        return None

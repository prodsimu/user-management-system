from repositories.session_repository import SessionRepository


class SessionService:

    def __init__(self, session_repository: SessionRepository):
        self.session_repository = session_repository

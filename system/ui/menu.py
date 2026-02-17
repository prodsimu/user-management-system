from models.user import User
from models.session import Session


class Menu:

    def __init__(self, user_service, session_service) -> None:
        self.user_service = user_service
        self.session_service = session_service

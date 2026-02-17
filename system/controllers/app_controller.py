from typing import Optional
from models.session import Session
from models.user import User
from services.user_service import UserService
from services.session_service import SessionService
from seed.seed import Seed
from ui.menu import Menu


class AppController:

    def __init__(
        self,
        user_service: UserService,
        session_service: SessionService,
    ) -> None:
        self.user_service: UserService = user_service
        self.session_service: SessionService = session_service
        self.menu: Menu = Menu(user_service, session_service)

        self.current_session: Optional[Session] = None
        self.current_user: Optional[User] = None

    def start(self) -> None:
        self.bootstrap()

    def bootstrap(self) -> None:
        seed = Seed(self.user_service)
        admin = seed.run_seed()

        if admin:
            self.menu.start_app()
            self.current_session = self.session_service.create_session(admin.id)
            self.current_user = admin

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
        self.main_loop()

    def bootstrap(self) -> None:
        seed = Seed(self.user_service)
        admin = seed.run_seed()

        if admin:
            self.menu.start_app()
            self.current_session = self.session_service.create_session(admin.id)
            self.current_user = admin

    def logout_current_session(self) -> None:
        self.session_service.logout(self.current_session.id)
        self.current_session = None
        self.current_user = None

    def get_choice(self, valid_options: list) -> int:
        choice = None

        while choice not in valid_options:
            try:
                choice = int(input("Choose an option: "))
                if choice not in valid_options:
                    print("\nChoose a valid option\n")
            except ValueError:
                print("\nChoose a valid option\n")

        return choice

    def main_loop(self) -> None:
        while True:

            if not self.current_session:
                self.menu.public_menu()
                break

            if self.current_user.role == "admin":
                self.menu.admin_menu()
                choice = self.get_choice([0, 1, 2, 3, 4])
                print(choice)
                break

            if self.current_user.role == "user":
                self.menu.user_menu()
                break

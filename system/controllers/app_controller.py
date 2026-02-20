from typing import Optional
from models.session import Session
from models.user import User
from services.user_service import UserService
from services.session_service import SessionService
from seed.seed import Seed
from ui.menu import Menu
from exceptions.exceptions import (
    InvalidPasswordError,
    SamePasswordError,
    UserNotFoundError,
    InactiveUserError,
    AppError,
)


class AppController:

    def __init__(
        self,
        user_service: UserService,
        session_service: SessionService,
    ) -> None:
        self.runnig: bool = True
        self.user_service: UserService = user_service
        self.session_service: SessionService = session_service
        self.menu: Menu = Menu()

        self.current_session: Optional[Session] = None
        self.current_user: Optional[User] = None

    def start(self) -> None:
        self.bootstrap()
        self.main_loop()

    def shutdown_system(self) -> None:
        self.menu.shutdown_message()
        self.runnig = False

    def bootstrap(self) -> None:
        seed = Seed(self.user_service)
        admin = seed.run_seed()

        if admin:
            self.menu.start_app()
            self.current_session = self.session_service.create_session(admin.id)
            self.current_user = admin

    def change_user_password(self) -> None:
        while True:
            new_password = input("\nType the new password: ")
            verify_password = input("Confirm the password: ")

            if new_password != verify_password:
                print("Passwords do not match")
                continue

            try:
                self.user_service.update_password_by_id(
                    self.current_user.id, new_password
                )
            except InvalidPasswordError as e:
                print(e)
                continue
            except SamePasswordError as e:
                print(e)
                continue

            print("Password updated successfully")
            break

    def logout_current_session(self) -> None:
        self.menu.logout_message()
        self.session_service.logout(self.current_session.id)
        self.session_service.delete_all_user_sessions(self.current_user.id)
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

    def user_flow(self) -> None:
        while self.current_user:

            self.menu.user_menu()
            choice = self.get_choice([0, 1])

            match choice:
                case 0:
                    self.logout_current_session()
                    break

                case 1:
                    self.change_user_password()

    def new_login(self) -> None:

        while True:

            username, password = self.menu.login_interface()

            try:
                self.current_session = self.user_service.login(username, password)
                self.current_user = self.user_service.get_user_by_session_id(
                    self.current_session.id
                )
                return

            except InactiveUserError as e:
                self.menu.show_error(str(e))
                return

            except AppError as e:
                self.menu.show_error(str(e))

    def main_loop(self) -> None:
        while self.runnig:

            if not self.current_session:
                self.menu.public_menu()
                choice = self.get_choice([0, 1])

                match choice:
                    case 0:
                        self.shutdown_system()
                        continue
                    case 1:
                        self.new_login()

            elif self.current_user.role == "user":
                self.user_flow()

            elif self.current_user.role == "admin":
                self.menu.admin_menu()
                choice = self.get_choice([0, 1, 2, 3, 4])

                match choice:
                    case 0:
                        self.logout_current_session()
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass

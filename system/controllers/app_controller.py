from typing import Optional
from models.session import Session
from models.user import User
from services.user_service import UserService
from services.session_service import SessionService
from seed.seed import Seed
from ui.menu import Menu
from exceptions.exceptions import (
    AppError,
    InactiveUserError,
    InvalidPasswordError,
    SamePasswordError,
    UserNotFoundError,
)


class AppController:

    def __init__(
        self,
        user_service: UserService,
        session_service: SessionService,
    ) -> None:
        self.runnig: bool = True
        self.first_system_startup: bool = True
        self.last_message: Optional[str] = None
        self.user_service: UserService = user_service
        self.session_service: SessionService = session_service
        self.menu: Menu = Menu()

        self.current_session: Optional[Session] = None
        self.current_user: Optional[User] = None

    # PUBLIC ENTRYPOINTS

    def start(self) -> None:
        self.bootstrap()
        self.main_loop()

    def shutdown_system(self) -> None:
        self.runnig = False

    # INITIALIZATION

    def bootstrap(self) -> None:
        seed = Seed(self.user_service)
        admin = seed.run_seed()

        if admin:
            self.current_session = self.session_service.create_session(admin.id)
            self.current_user = admin

    # MAIN LOOP

    def main_loop(self) -> None:

        if self.first_system_startup:
            self.menu.clear_screen()
            self.menu.start_app()
            self.first_system_startup = False

        while self.runnig:

            if not self.current_session:
                self.handle_public_flow()

            elif self.current_user.role == "user":
                self.user_flow()

            elif self.current_user.role == "admin":
                self.admin_flow()

        self.menu.clear_screen()
        self.menu.shutdown_message()

    # FLOWS

    def handle_public_flow(self) -> None:
        self.render_menu(self.menu.public_menu)
        choice = self.get_choice([0, 1])

        match choice:
            case 0:
                self.shutdown_system()
            case 1:
                self.new_login()

    def user_flow(self) -> None:
        while self.current_user:
            self.render_menu(self.menu.user_menu)
            choice = self.get_choice([0, 1])

            match choice:
                case 0:
                    self.logout_current_session()
                    return

                case 1:
                    self.change_user_password()

    def admin_flow(self) -> None:
        while self.current_user and self.current_user.role == "admin":
            self.render_menu(self.menu.admin_menu)
            choice = self.get_choice([0, 1, 2, 3, 4])

            match choice:
                case 0:
                    self.logout_current_session()
                    return

                case 1:
                    self.create_new_user()

                case 2:
                    self.list_all_users()

                case 3:
                    self.update_user()

                case 4:
                    self.delete_user()

    # AUTH ACTIONS

    def new_login(self) -> None:

        username, password = self.menu.login_interface()

        try:
            self.current_session = self.user_service.login(username, password)
            self.current_user = self.user_service.get_user_by_session_id(
                self.current_session.id
            )

            self.last_message = "logged in successfully"

        except InactiveUserError as e:
            self.last_message = self.menu.show_error(str(e))

        except AppError as e:
            self.last_message = self.menu.show_error(str(e))

    def logout_current_session(self) -> None:
        self.last_message = self.menu.logout_message()
        self.session_service.logout(self.current_session.id)
        self.session_service.delete_all_user_sessions(self.current_user.id)
        self.current_session = None
        self.current_user = None

    # USER ACTIONS

    def create_new_user(self) -> None:
        name, username, password = self.menu.get_user_data_to_creation()

        try:
            self.user_service.create_user(name, username, password)
            self.last_message = "user successfully created"
        except AppError as e:
            self.last_message = "User cannot be created\n" + self.menu.show_error(
                str(e)
            )

    def change_user_password(self) -> None:
        new_password = input("\nType the new password: ")
        verify_password = input("Confirm the password: ")

        if new_password != verify_password:
            self.last_message = "Passwords do not match"
            return

        try:
            self.user_service.update_password_by_id(self.current_user.id, new_password)
        except InvalidPasswordError as e:
            self.last_message = str(e)
            return
        except SamePasswordError as e:
            self.last_message = str(e)
            return

        self.last_message = "Password updated successfully"

    def list_all_users(self) -> None:
        users = self.user_service.list_users()

        if not users:
            self.last_message = "No users found"
            return

        messages = []

        for user in users:
            messages.append(self.menu.show_user_description(user))

        self.last_message = "\n".join(messages)

    def show_user_by_id(self, user_id) -> None:
        try:
            user = self.user_service.get_user_by_id(user_id)
        except UserNotFoundError as e:
            self.menu.show_error(str(e))
            return

        self.menu.show_user_description(user)

    def delete_user(self) -> None:
        user_id = int(input("Type user id: "))

        try:
            self.user_service.delete_user_by_id(user_id)
            self.last_message = "\nUser deleted with sucess"
        except UserNotFoundError:
            self.last_message = "\nUser not found"

    def update_user(self) -> None:
        try:
            user_id = int(input("Type user id: "))
            user = self.user_service.get_user_by_id(user_id)

            if not user:
                raise UserNotFoundError("User not found")

        except ValueError:
            self.last_message = "\nInvalid id\n"
            return
        except UserNotFoundError as e:
            self.last_message = self.menu.show_error(str(e))
            return

        self.menu.clear_screen()
        self.menu.update_user_interface()
        choice = self.get_choice([0, 1, 2, 3, 4, 5, 6])

        try:
            match choice:
                case 0:
                    self.last_message = "Canceled action"

                case 1:
                    new_name = input("New name: ")
                    self.user_service.update_name_by_id(user_id, new_name)
                    self.last_message = "Name successfully updated"

                case 2:
                    new_username = input("New username: ")
                    self.user_service.update_username_by_id(user_id, new_username)
                    self.last_message = "Username successfully updated"

                case 3:
                    new_password = input("New password: ")
                    self.user_service.update_password_by_id(user_id, new_password)
                    self.last_message = "Password successfully updated"

                case 4:
                    new_role = input("New role (user/admin): ")
                    self.user_service.change_role_by_id(user_id, new_role)
                    self.last_message = "Role successfully changed"

                case 5:
                    if user.active:
                        self.user_service.deactivate_user_by_id(user_id)
                        self.last_message = "User successfully deactivated"
                    else:
                        self.user_service.activate_user_by_id(user_id)
                        self.last_message = "User successfully activated"

                case 6:
                    self.user_service.reset_login_attempts_by_id(user_id)
                    self.last_message = "Login attempts successfully reset"

        except AppError as e:
            self.last_message = self.menu.show_error(str(e))

    # UTILITIES

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

    def render_menu(self, menu_function) -> None:
        self.menu.clear_screen()

        if self.last_message:
            print(self.last_message)
            print()
            self.last_message = None

        menu_function()

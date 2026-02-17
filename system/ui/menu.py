from models.user import User
from models.session import Session


class Menu:

    def __init__(self, user_service, session_service) -> None:
        self.user_service = user_service
        self.session_service = session_service

    def start_app(self) -> None:
        print("=== SYSTEM INITIALIZED ===")
        print("Admin created automatically:")
        print("username: admin")
        print("password: admin123")
        print("Logging in...\n")

    def admin_menu(self) -> int:
        print("ADMIN MENU")
        print("1 - Create user")
        print("2 - List users")
        print("3 - Update user")
        print("4 - Delete User")
        print("0 - Logout")

        valid_options = [0, 1, 2, 3, 4]
        choice = None

        while choice not in valid_options:
            try:
                choice = int(input("Choose an option: "))
                if choice not in valid_options:
                    print("\nChoose a valid option\n")
            except ValueError:
                print("\nChoose a valid option\n")

        return choice

    def user_menu(self) -> int:
        print("1 - Change password")
        print("0 - Logout")

        valid_options = [0, 1]
        choice = None

        while choice not in valid_options:
            try:
                choice = int(input("Choose an option: "))
                if choice not in valid_options:
                    print("\nChoose a valid option\n")
            except ValueError:
                print("\nChoose a valid option\n")

        return choice

    def public_menu(self) -> int:
        print("1 - Loggin")
        print("0 - Exit")

        valid_options = [0, 1]
        choice = None

        while choice not in valid_options:
            try:
                choice = int(input("Choose an option: "))
                if choice not in valid_options:
                    print("\nChoose a valid option\n")
            except ValueError:
                print("\nChoose a valid option\n")

        return choice

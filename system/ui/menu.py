import os
from models.user import User


class Menu:

    def start_app(self) -> None:
        print("=== SYSTEM INITIALIZED ===")
        print("Admin created automatically:")
        print("username: admin")
        print("password: admin123")
        print("Logging in...\n")

    def admin_menu(self) -> None:
        print("=== ADMIN MENU ===")
        print("1 - Create user")
        print("2 - List users")
        print("3 - Update user")
        print("4 - Delete User")
        print("0 - Logout")

    def user_menu(self) -> None:
        print("=== USER MENU ===")
        print("1 - Change password")
        print("0 - Logout")

    def public_menu(self) -> None:
        print("=== PUBLIC MENU ===")
        print("1 - Login")
        print("0 - Exit")

    def logout_message(self) -> None:
        print("Exiting session...")

    def shutdown_message(self) -> None:
        print("Shutting down system...")

    def login_interface(self) -> str:
        username = input("Username: ")
        password = input("Password: ")

        return username, password

    def get_user_data_to_creation(self) -> str:
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")

        return name, username, password

    def show_error(self, message: str) -> str:
        return f"{message}"

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def show_user_description(self, user: User) -> str:
        return (
            "\n------------------------------\n"
            f"ID ----------- {user.id}\n"
            f"Name --------- {user.name}\n"
            f"Username ----- {user.username}\n"
            f"Password ----- {user.password}\n"
            f"Role --------- {user.role}\n"
            f"Active ------- {user.active}\n"
            f"Login Attempts {user.login_attempts}\n"
            "------------------------------"
        )

    def update_user_interface(self) -> None:
        print("1 - Update name")
        print("2 - Update username")
        print("3 - Update password")
        print("4 - Change role")
        print("5 - Activate/Deactivate")
        print("6 - Reset login attempts")
        print("0 - Cancel")

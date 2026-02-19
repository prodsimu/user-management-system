import os


class Menu:

    def start_app(self) -> None:
        self.clear_screen()
        print("=== SYSTEM INITIALIZED ===")
        print("Admin created automatically:")
        print("username: admin")
        print("password: admin123")
        print("Logging in...\n")

    def admin_menu(self) -> None:
        self.clear_screen()
        print("=== ADMIN MENU ===")
        print("1 - Create user")
        print("2 - List users")
        print("3 - Update user")
        print("4 - Delete User")
        print("0 - Logout")

    def user_menu(self) -> None:
        self.clear_screen()
        print("=== USER MENU ===")
        print("1 - Change password")
        print("0 - Logout")

    def public_menu(self) -> None:
        self.clear_screen()
        print("=== PUBLIC MENU ===")
        print("1 - Login")
        print("0 - Exit")

    def logout_message(self) -> None:
        print("Exiting session...")

    def shutdown(self) -> None:
        print("Shutting down system...")

    def login_interface(self) -> None:
        username = input("Username: ")
        password = input("Password: ")

        return username, password

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

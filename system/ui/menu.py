class Menu:

    def start_app(self) -> None:
        print("=== SYSTEM INITIALIZED ===")
        print("Admin created automatically:")
        print("username: admin")
        print("password: admin123")
        print("Logging in...\n")

    def admin_menu(self) -> None:
        print("ADMIN MENU")
        print("1 - Create user")
        print("2 - List users")
        print("3 - Update user")
        print("4 - Delete User")
        print("0 - Logout")

    def user_menu(self) -> None:
        print("1 - Change password")
        print("0 - Logout")

    def public_menu(self) -> None:
        print("1 - Login")
        print("0 - Exit")

    def shutdown(self) -> None:
        print("Shutting down system...")

    def login_interface(self, username: bool) -> None:
        if not username:
            print("Username: ", end="")

        if username:
            print("Password: ", end="")

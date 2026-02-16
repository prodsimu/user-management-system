from database.database import Database
from repositories.session_repository import SessionRepository
from repositories.user_repository import UserRepository
from services.session_service import SessionService
from services.user_service import UserService
from ui.menu import Output


def main():
    system_is_starting = None
    current_user = None
    current_session = None

    db = Database()

    session_repository = SessionRepository(db)
    user_repository = UserRepository(db)

    session_service = SessionService(session_repository)
    user_service = UserService(user_repository, session_service)

    menu_output = Output(user_service, session_service)

    if not user_service.list_users():
        initial_admin = user_service.create_user("admin", "admin", "admin123")
        user_service.change_role_by_id(initial_admin.id, "admin")
        system_is_starting = True

    while True:

        if system_is_starting:
            menu_output.start_system()
            pass

        break


if __name__ == "__main__":
    main()

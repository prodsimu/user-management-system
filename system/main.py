from database.database import Database
from repositories.session_repository import SessionRepository
from repositories.user_repository import UserRepository
from services.session_service import SessionService
from services.user_service import UserService
from ui.menu import Output
from seed.seed import Seed


def main():
    system_is_starting = True
    current_user = None
    current_session = None

    db = Database()

    session_repository = SessionRepository(db)
    user_repository = UserRepository(db)

    session_service = SessionService(session_repository)
    user_service = UserService(user_repository, session_service)

    seed = Seed(user_service)

    seed = Seed(user_service)

    menu_output = Output(user_service, session_service)

    while True:

        if system_is_starting:
            initial_admin = seed.run_seed()
            menu_output.start_system(initial_admin)

        break


if __name__ == "__main__":
    main()

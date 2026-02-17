from database.database import Database
from repositories.session_repository import SessionRepository
from repositories.user_repository import UserRepository
from services.session_service import SessionService
from services.user_service import UserService
from controllers.app_controller import AppController


def main():
    db = Database()

    session_repository = SessionRepository(db)
    user_repository = UserRepository(db)

    session_service = SessionService(session_repository)
    user_service = UserService(user_repository, session_service)

    app = AppController(user_service, session_service)
    app.start()


if __name__ == "__main__":
    main()

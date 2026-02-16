import uuid
from datetime import datetime, timedelta


class Session:

    SESSION_DURATION_MINUTES = 30

    def __init__(self, user_id: int) -> None:
        self.id: str = str(uuid.uuid4())
        self.user_id: int = user_id
        self.created_at: datetime = datetime.now()
        self.expires_at: datetime = self.created_at + timedelta(
            minutes=self.SESSION_DURATION_MINUTES
        )
        self.active: bool = True

    def __repr__(self) -> str:
        return (
            f"Session(id={self.id}, user_id={self.user_id}, "
            f"active={self.active}, expires_at={self.expires_at})"
        )

    def is_expired(self) -> bool:
        return datetime.now() >= self.expires_at

    def invalidate(self) -> None:
        self.active = False

    def renew(self) -> None:
        self.expires_at = datetime.now() + timedelta(
            minutes=self.SESSION_DURATION_MINUTES
        )
        self.active = True

import os
import hashlib
import binascii


class PasswordHasher:
    ITERATIONS = 100_000
    SALT_SIZE = 16
    ALGORITHM = "sha256"

    @classmethod
    def hash_password(cls, password: str) -> str:
        salt = os.urandom(cls.SALT_SIZE)

        hash_bytes = hashlib.pbkdf2_hmac(
            cls.ALGORITHM, password.encode("utf-8"), salt, cls.ITERATIONS
        )

        return binascii.hexlify(salt + hash_bytes).decode("utf-8")

    @classmethod
    def verify_password(cls, password: str, stored_password: str) -> bool:
        stored_bytes = binascii.unhexlify(stored_password.encode("utf-8"))

        salt = stored_bytes[: cls.SALT_SIZE]
        stored_hash = stored_bytes[cls.SALT_SIZE :]

        new_hash = hashlib.pbkdf2_hmac(
            cls.ALGORITHM, password.encode("utf-8"), salt, cls.ITERATIONS
        )

        return new_hash == stored_hash

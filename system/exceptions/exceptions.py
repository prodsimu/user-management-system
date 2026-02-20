class AppError(Exception):
    pass


class UserNotFoundError(AppError):
    pass


class InvalidPasswordError(AppError):
    pass


class SamePasswordError(AppError):
    pass


class EmptyLoginCredentialsError(AppError):
    pass


class InactiveUserError(AppError):
    pass

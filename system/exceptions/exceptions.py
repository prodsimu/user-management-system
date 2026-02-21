class AppError(Exception):
    pass


class UserNotFoundError(AppError):
    pass


class InvalidPasswordError(AppError):
    pass


class InvalidUsernameError(AppError):
    pass


class InvalidNameError(AppError):
    pass


class SamePasswordError(AppError):
    pass


class EmptyLoginCredentialsError(AppError):
    pass


class InactiveUserError(AppError):
    pass


class UsernameAlreadyExistsError(AppError):
    pass


class UserAlreadyActiveError(AppError):
    pass

class User:
    def __init__(self,
                 id, name, username, password,
                 role, active, login_attempts):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.role = role
        self.active = active
        self.login_attempts = login_attempts


    def verify_password(self, password):
        return self.password == password


    def change_password(self, new_password):
        self.password = new_password


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


    def deactivate(self):
        self.active = False


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "active": self.active,
            "login_attempts": self.login_attempts
        }

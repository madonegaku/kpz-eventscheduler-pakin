
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password # У проєкті тут буде хеш
        self.is_active = True
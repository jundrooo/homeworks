class Foydalanuvchi:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

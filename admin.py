from foydalanuvchi import Foydalanuvchi

class Admin(Foydalanuvchi):
    def ban_user(self, user):
        print(f"{user.username} bloklandi")

    def get_user_info(self, user):
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")

from talaba import Talaba
from admin import Admin
from foydalanuvchi import Foydalanuvchi

admin = Admin("admin123", "admin@example.com")
foydalanuvchi = Foydalanuvchi("foydalanuvchi1", "user1@example.com")

admin.get_user_info(foydalanuvchi)
admin.ban_user(foydalanuvchi)

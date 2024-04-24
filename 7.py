class Shaxs:
    def __init__(self, ism, yosh, jins, millat, manzil):
        self.ism = ism
        self.yosh = yosh
        self.jins = jins
        self.millat = millat
        self.manzil = manzil

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"{self.ism}, {self.yosh} yosh, {self.jins}, {self.millat}, {self.manzil}"

class Talaba(Shaxs):
    def __init__(self, ism, yosh, jins, millat, manzil, student_id, kurs, yoanalishi, gpa, oqituvchi):
        super().__init__(ism, yosh, jins, millat, manzil)
        self.student_id = student_id
        self.kurs = kurs
        self.yoanalishi = yoanalishi
        self.gpa = gpa
        self.oqituvchi = oqituvchi

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"{self.ism}, {self.yosh} yosh, {self.jins}, {self.millat}, {self.manzil}, ID: {self.student_id}, Kurs: {self.kurs}, Yo'nalishi: {self.yoanalishi}, GPA: {self.gpa}, O'qituvchi: {self.oqituvchi}"

class Foydalanuvchi:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

class Admin(Foydalanuvchi):
    def ban_user(self, user):
        print(f"{user.username} bloklandi")


admin = Admin("admin123", "admin@example.com")


foydalanuvchi = Foydalanuvchi("foydalanuvchi1", "user1@example.com")


admin.ban_user(foydalanuvchi)

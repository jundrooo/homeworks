from shaxs import Shaxs

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

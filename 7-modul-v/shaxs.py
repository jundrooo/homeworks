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

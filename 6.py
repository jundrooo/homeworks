class Avto:
    def ___init__ (self, model, rang, karobka, narx,):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.km_distance = 0
    def get_info(self):
        return f"Mashina modeli:{self.model} rangi: {self.rang} gear : {self.karobka} masofasi : {self.km_distance} "
    
    def update_km_distance(self, km):
        self.km_distance = km


class Avtosalon:
    def __init__(self):
        self.name = nomi 
        self.location = manzil
        self.cars = []

    def avto_add(self, avto):
        self.cars.append(avto)
    
    def cars_info(self):
        avto_info = ""
        for avto in self.cars:
            avto_info += avto.get_info()


avto1 = Avto('Tayota Supra','white','manual','80k')
avtosalon = Avtosalon('Tayota','Japan','??? street')

avtosalon.avto_add(avto1)
print(f"{avtosalon.nomi} , avtosaloni {avtosalon.location} manzilda joylashgan.")
print(f"Salondagi Avtomabillar {avtosalon.cars_info()}")
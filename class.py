class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

Kidus_Car = Car("Bugati", "Chiron", 2021)
Leul_Car = Car("Hyndai", "Tucson", 2019)

Kidus_Car.display_info()
Leul_Car.display_info()
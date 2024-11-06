# Завдання 1: Наслідування
# Створіть базовий клас `Vehicle` (транспортний засіб), 
# який містить наступні атрибути:
# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)
# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.
# Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, 
# наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо. 
# Кожен підклас повинен мати додаткові атрибути та методи, які є специфічними для цього виду транспорту. 
# Наприклад, для класу `Car` можна додати атрибут `fuel_type` та метод `start_engine()`.
# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.

class Vehicle:
    """Class Vehicle"""
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def general_data(self):
        print(f"{self.model} ({self.make}) made in {self.year}")

class Car(Vehicle):
    """Class Car"""
    def __init__(self, make, model, year, fuel_type) -> None:
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"Engine is starting. Type of fuel is {self.fuel_type}")

class Motorcycle(Vehicle):
    """Class Motocycle"""
    def __init__(self, make, model, year, wheels) -> None:
        super().__init__(make, model, year)
        self.wheels = wheels

    def count_of_wheels(self):
        print(f"This motorcycle has {self.wheels} wheels")

class Bicycle(Vehicle):
    """Class Bicycle"""
    def __init__(self, make, model, year, cost) -> None:
        super().__init__(make, model, year)
        self.cost = cost

    def how_much(self):
        print(f"Motorcycle costs {self.cost} usd")

# -----------------------------------------

car_01 = Car("France", "Renault", 2015, "diesel")
car_01.general_data()
car_01.start_engine()

print("-------")

motorcycle_01 = Motorcycle("Germany", "BMW", 2020, 2)
motorcycle_01.general_data()
motorcycle_01.count_of_wheels()

print("-------")

bicycle_01 = Bicycle("USA", "TREK", 2017, 2000)
bicycle_01.how_much()
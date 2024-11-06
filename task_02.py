# **Завдання 2: Поліморфізм**
# Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про транспортний засіб (наприклад, "Це [виробник] [модель] [рік] року виробництва.").
# В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної інформації про цей вид транспорту.
# Створіть список об'єктів з різних видів транспорту, викличте метод `display_info()` для кожного об'єкта, і спостерігайте за тим, як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.

class Vehicle:
    """Class Vehicle"""
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.model} ({self.make}) made in {self.year}")

class Car(Vehicle):
    """Class Car"""
    def __init__(self, make, model, year, fuel_type) -> None:
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"{self.model} ({self.make}) made in {self.year}, {self.fuel_type}")

class Motorcycle(Vehicle):
    """Class Motocycle"""
    def __init__(self, make, model, year, wheels) -> None:
        super().__init__(make, model, year)
        self.wheels = wheels

    def display_info(self):
        print(f"This motorcycle has {self.wheels} wheels")
        return super().display_info()

class Bicycle(Vehicle):
    """Class Bicycle"""
    def __init__(self, make, model, year, cost) -> None:
        super().__init__(make, model, year)
        self.cost = cost

    def display_info(self):
        print(f"Motorcycle costs {self.cost} usd")
        return super().display_info()

# -----------------------------------------

car_01 = Car("France", "Renault", 2015, "diesel")
car_01.display_info()

print("-------")

motorcycle_01 = Motorcycle("Germany", "BMW", 2020, 2)
motorcycle_01.display_info()

print("-------")

bicycle_01 = Bicycle("USA", "TREK", 2017, 2000)
bicycle_01.display_info()
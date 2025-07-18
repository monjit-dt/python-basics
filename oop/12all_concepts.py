# Base class: Car
class Car:
    count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.count += 1

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Uses petrol or diesel or CNG"

    def total_car(self):
        return Car.count

    @classmethod
    def total_cars(cls):
        return cls.count

    @staticmethod
    def desp():
        return "A Car has 4 wheels"

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model_new):
        self.__model = model_new


# Derived class: ElectricCar
class Electric_car(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def e_full_name(self):
        return f"{self.brand} {self.model} {self.battery}"

    def fuel_type(self):
        return "Uses electricity"


# Object instantiation and testing
car_details = Car("Honda", "Hilux")
Ecar_details = Electric_car("Tesla", "Y", "85kWh")

print(Car.desp())
print(f"Car details: {car_details.full_name()} & {car_details.fuel_type()}")
print(f"Electric Car details: {Ecar_details.e_full_name()} & {Ecar_details.fuel_type()}")

car_details.model = "800"
print(f"Updated Car model: {car_details.full_name()} & {car_details.fuel_type()}")

print(f"Total number of cars: {Car.count}")

# Type checks
print(isinstance(Ecar_details, Car))        
print(isinstance(Ecar_details, Electric_car)) 
print(isinstance(car_details, Electric_car))  
print(isinstance(car_details, Car))          


# Demonstration of multiple inheritance
class Battery:
    def __init__(self):
        self.battery_info = "Battery: 85 kWh"

class Engine:
    def __init__(self):
        self.engine_info = "Engine: Dual Motor"

class ElectricCar_2(Battery, Engine):
    def __init__(self, brand):
        self.brand = brand
        Battery.__init__(self)
        Engine.__init__(self)

# This example demonstrates how multiple inheritance can be used 
# to combine features from different classes such as Battery and Engine.


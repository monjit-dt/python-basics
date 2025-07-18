class Car:
   
    count = 0
    def __init__(self , brand , model):
        self.brand = brand
        self.__model = model
        Car.count += 1        
    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return " Uses petrol or diesel or CNG"    
    def total_car(self):
        return Car.count    
    @classmethod
    def total_cars(Car):
        return Car.count
    @staticmethod
    def desp():
        return "A Car has 4 wheels"
    @property 
    def model(self):
        return self.__model
    @model.setter 
    def model(self, model_new):
        self.__model = model_new


class Electric_car(Car):
    def __init__(self , brand , model , battery):
        super().__init__(brand , model)
        self.battery = battery
    def e_full_name(self):
        return f"{self.brand} {self.model} {self.battery}"
    def fuel_type(self):
        return "Uses electricity"
car_details = Car("Honda" , "Hilux")
Ecar_details = Electric_car("Tesla" , "y" , "85kwh")   
# print(Car.desp())
# print(f"Car_details: {car_details.full_name()} & {car_details.fuel_type()}")
# print(f"ECar_details: {Ecar_details.e_full_name()} & {Ecar_details.fuel_type()}")
# car_details.model = "800"
# print(f"Car_details_model_changed: {car_details.full_name()} & {car_details.fuel_type()}")
# print(f"No_of _cars: {Car.count}")


print(isinstance(Ecar_details , Car))
print(isinstance(Ecar_details , Electric_car))  #isinstance(object, classinfo); object → the instance you want to check
print(isinstance(car_details , Electric_car))           #classinfo → the class (or a tuple of classes) we're checking against

a = isinstance(car_details , Car)
print(a)

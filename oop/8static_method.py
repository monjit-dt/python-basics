class Car:
   
    count = 0
    def __init__(self , brand , model):
        self.brand = brand
        self.__model = model
        Car.count += 1 
    def get(self):
        return self.__model    
    def set(self,model_new):
        self.__model = model_new
    def full_name(self):
        return f"{self.brand} {self.get()}"    
    def fuel_type(self):
        return " Uses petrol or diesel or CNG"    
    def total_car(self):
        return Car.count    
    @classmethod
    def total_cars(Car):
        return Car.count
    
    @staticmethod           # Static method is used to give general description and no self is required
    def desp():
        return "A Car has 4 wheels"
    
class Electric_car(Car):
    def __init__(self , brand , model , battery):
        super().__init__(brand , model)
        self.battery = battery
    def Efull_name(self):
        return f"{self.brand} {self.get()} {self.battery}"    
    def fuel_type(self):
        return "Uses electricity"


car_details = Car("Honda" , "Hilux")
Ecar_details = Electric_car("Tesla" , "y" , "85kwh")   

print(Car.desp())  # Must be written along with the class name like car.Variable_name,But calling with car_details.desp() also works.

print(f"Car_details: {car_details.full_name()} & {car_details.fuel_type()}")
print(f"ECar_details: {Ecar_details.Efull_name()} & {Ecar_details.fuel_type()}")

car_details.set("800")          #used set here, must remember to use with with get(used in full_name)
print(f"Car_details_model_changed: {car_details.full_name()} & {car_details.fuel_type()}")
print(f"No_of _cars: {Car.count}")
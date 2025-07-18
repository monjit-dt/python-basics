class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.__model = model

    def get(self):
        return self.__model
    
    def set(self,model_new):
        self.__model = model_new

    def full_name(self):
        return f"{self.brand} {self.get()}"
    
    def fuel_type(self):         #Polymorphism since first name different behavior
        return " Uses petrol or diesel or CNG"

class Electric_car(Car):
    def __init__(self , brand , model , battery):
        super().__init__(brand , model)
        self.battery = battery

    def Efull_name(self):
        return f"{self.brand} {self.get()} {self.battery}"
    
    def fuel_type(self):        #Polymorphism since second name different behavior
        return "Uses electricity"

car_details = Car("Honda" , "Hilux")
Ecar_details = Electric_car("Tesla" , "y" , "85kwh")   

print(f"Car_details: {car_details.full_name()} & {car_details.fuel_type()}")
print(f"ECar_details: {Ecar_details.Efull_name()} & {Ecar_details.fuel_type()}")

car_details.set("800")          #used set here, must remember to use with with get(used in full_name)
print(f"Car_details_model_changed: {car_details.full_name()} & {car_details.fuel_type()}")
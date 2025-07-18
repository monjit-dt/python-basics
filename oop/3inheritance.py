class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} , {self.model} , {self.battery_size}"
    
class Electric_car(Car):
    def __init__(self , brand , model , battery_size): #__init__ is must for new input
        super().__init__(brand , model) 
        self.battery_size = battery_size    

car_details = Car("Honda" , "Hilux")        
car_details1 = Electric_car("Honda" , "Hilux" ,"75kwh")        


# print(f"{car_details.full_name()}") #wont work as full_name is inside class Car can take 2 arguments

print(f"{car_details1.full_name()}")
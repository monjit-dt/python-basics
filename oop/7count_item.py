class Car:
   
    count = 0       #Declared once for the whole class (not per object)

    def __init__(self , brand , model):
        self.brand = brand
        self.__model = model
        Car.count += 1          #Updates the class-wide counter & Inside __init_ Because this runs every time a car is created
    def get(self):
        return self.__model
    
    def set(self,model_new):
        self.__model = model_new

    def full_name(self):
        return f"{self.brand} {self.get()}"
    
    def fuel_type(self):
        return " Uses petrol or diesel or CNG"
    
    def total_car(self):        #Used to count the no. of cars
        return Car.count        #self.count would make a separate counter for each car, which is wrong for this case
    
    @classmethod                #other method to use count
    def total_cars(Car):        #must use cls to use @classmethod
        return Car.count        #must use cls.count
    
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

print(f"Car_details: {car_details.full_name()} & {car_details.fuel_type()}")
print(f"ECar_details: {Ecar_details.Efull_name()} & {Ecar_details.fuel_type()}")

car_details.set("800")          #used set here, must remember to use with with get(used in full_name)
print(f"Car_details_model_changed: {car_details.full_name()} & {car_details.fuel_type()}")

#Count of cars using various ways to print

print(f"No_of _cars: {Car.count}")      #Cannot be used Car.total_cars() as without class method and used self

print(Car.count)              # ✅ Direct access using class method, used class name 
print(Car.total_cars())       # ✅ OOP preferred way using class method, used class name
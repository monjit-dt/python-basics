class Car:
   
    count = 0
    def __init__(self , brand , model):
        self.brand = brand
        self.__model = model
        Car.count += 1        
    # def get(self):
    #     return self.__model     #@property replaces a get() method
    # def set(self,model_new):    # @<property>.setter replaces a set() method
    #     self.__model = model_new
    def full_name(self):
        return f"{self.brand} {self.model}"    #.model replaces .get() thanks to @property.
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
    
    @property           #This line converts the function below into a property (looks like a variable, but it's a method).
    def model(self):    # We could write anything instead of model and self is required because we are working with object
        return self.__model
    
    @model.setter #Setter name must match the property. That’s how Python lets you do:car.model = "800" instead of car.set("800").
    def model(self, model_new):       #The setter method must have the exact same name as the property i.e model not set.
        self.__model = model_new


class Electric_car(Car):
    def __init__(self , brand , model , battery):
        super().__init__(brand , model)
        self.battery = battery
    def e_full_name(self):
        return f"{self.brand} {self.model} {self.battery}"   #.model replaces .get() thanks to @property.
    def fuel_type(self):
        return "Uses electricity"


car_details = Car("Honda" , "Hilux")
Ecar_details = Electric_car("Tesla" , "y" , "85kwh")   



print(Car.desp())
print(f"Car_details: {car_details.full_name()} & {car_details.fuel_type()}")
print(f"ECar_details: {Ecar_details.e_full_name()} & {Ecar_details.fuel_type()}")


# car_details.set("800") #used set here, must remember to use with with get(used in full_name),set() is a normal method, and all methods in Python are called using parentheses.

car_details.model = "800" #behaves like variable assignment
#car.model("800") is invalid because .model is no longer a function — it's now a property (a fake variable).



print(f"Car_details_model_changed: {car_details.full_name()} & {car_details.fuel_type()}")
print(f"No_of _cars: {Car.count}")

print(car_details.model)        #Already changed above everything just written here to show the concept
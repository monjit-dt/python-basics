class Car:
    def __init__(self, brand , model):
        self.brand = brand 
        self.__model = model      #__ for private variable
    
    def get_model(self):            # Getter method(Used to safely read the private variable (__model)), name can be anything
        return self.__model
    
    def set_model(self, new_model):       # Setter method(Used to safely modify the private variable (__model)), name can be anything but new variable has to be defined
        self.__model = new_model          #Imp step not like get have to give new variable
    
    
car_details = Car("Toyota" , "Hilux")

print(f"before : {car_details.brand} , {car_details.get_model()}")      #doing same mistake of not giving () it calls the function 

car_details.set_model("abc")        #must be given before using get in print

print(f"After : {car_details.brand} , {car_details.get_model()}")

# print(f"Will not work as private variable outside class :{car_details.__model}")
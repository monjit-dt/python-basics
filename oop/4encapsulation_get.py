class Car:
    def __init__(self, brand , model):
        self.brand = brand 
        self.__model = model      #__ for private variable
    
    def get_model(self):            # Getter method, name can be anything
        return self.__model
    
car_details = Car("Toyota" , "Hilux")

print(car_details.brand , car_details.get_model())      #doing same mistake of not giving () it calls the function 
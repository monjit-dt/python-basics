class Car:
    def __init__(self , brand ,model):
        self.brand = brand
        self.model = model

car_details = Car("Toyota" , "Hilux")

print(car_details.brand , car_details.model)
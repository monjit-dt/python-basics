class Car:
    def __init__(self , brand ,model):
        self.brand = brand
        self.model = model
    
    def fullname(self):     #method - func inside class
        return f"{self.brand} {self.model}" # return self.brand , self.model will return output as tuple as ('Honda', 'Hilux')

car_details = Car("Toyota" , "Hilux")

print(car_details.brand , car_details.model) #have two write two
print(car_details.fullname())   #only giving car_details.full_name without () will give memory location as its a function
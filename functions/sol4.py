import math
def find(num):
    area = math.pi * (num)**2
    cicum = 2 * math.pi * num 
    return area , cicum

radius = int(input("Write radius: "))

area , cir = find(radius)

print(f"Area is: {area:.2f} , circumference is : {cir:.2f}")
print("Area is:" , round(area,2) , ",  circumference is :" , round(cir,2))
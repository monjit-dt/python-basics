num = int(input("write the number: "))
factorial = 1

for i in range(1,num + 1):
    factorial = factorial * i
   
print("Factorial is: " , factorial)
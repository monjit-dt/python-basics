age = int(input("Age of the person:"))
Day = input("Day of the week:")

Price = 12 if age >= 18 else 8

if Day== "wednesday":
    Price -= 2

print("Movie ticket price is $",Price)
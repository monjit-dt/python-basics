year = int(input("write the year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    a= "Its a leap year"

else:
    a= "Its a non-leap year"

print(a)
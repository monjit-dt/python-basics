def find_sq(num):
    sq = num ** 2
    return sq

number = int(input("Write any number To obtain square: "))

result = find_sq(number)
print(result)

def find(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"

number = int(input("Write any number to check whether its odd or even: "))

result = find(number)
print(result)



def find_avg(num1,num2):
    return (num1 + num2) / 2

number1 = int(input("Write 1st number: "))
number2 = int(input("Write 2nd number: "))

result = find_avg(number1,number2)
print(result)
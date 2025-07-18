def add(*args):
    total = 0
    for num in args:
        total = total + num
    return total

print(add(5 , 525 ))
print(add(5 , 525 , 1))
print(add(5 , 525 , 1 , 54))
print(add(5 , 525 , 1 ,526 , 6))
num = int(input("write the number: "))

if num < 1:
    is_prime = False
else:
    is_prime = True

    for i in range(2,num + 1):
        if i == num:
            continue    # Skip checking num itself
        if num % i == 0:
            is_prime= False
            break

if is_prime == True:
    print(num , "is a prime no.")

if is_prime == False:
    print(num , "is not a prime no.")

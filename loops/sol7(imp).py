while True:              #Starts infinite loop
    num = int(input("write the number bet 1-10: "))
    if num >= 1 and num <= 10 :
        print("Thanks for the number")
        break           #Stops loop if number is okay
    else:
        print("Invalid,Repeat the number again")
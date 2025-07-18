fruit = input("name of the fruit:")

if fruit != "banana":
    print("Invalid fruit")
    exit()

colour = (input("colour of the fruit:"))

if fruit == "banana":
    if colour == "green":
        print("Fruit is unripe")
    elif colour == "yellow":
        print("Fruit is ripe")
    elif colour == "brown":
        print("Fruit is overripe")
    else:
        print("Fruit cant be determined")
order_size = input("size:").lower()
extra_shot = input('Do you Need expresso:').lower()

if extra_shot == "yes":

    if order_size == "large":
        Coffee = order_size + " coffee with Expresso"

    elif order_size == "medium":
        Coffee = order_size + " coffee with Expresso"

    elif order_size == "small":
        Coffee = order_size + " coffee with Expresso"

elif extra_shot == "no":
    if order_size == "large":
        Coffee = order_size

    elif order_size == "medium":
        Coffee = order_size

    elif order_size == "small":
        Coffee = order_size 
    else:
        Coffee = order_size

print("order", Coffee)
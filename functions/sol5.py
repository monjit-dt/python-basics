def greet(person_name = "bruh"):
    return person_name

name = input("what is your name: ")

if name.strip() == "":
    message = greet()

else:
    message = greet(name)

print("hii" , message)


#short way

def greet(person_name="Guest"):
    return f"Hello, {person_name}! Welcome!"

name = input("what is your name: ")

# and then just print:
print(greet(name.strip() or ""))


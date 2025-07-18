password = input("Write the password: ")
pass_len = len(password)

if pass_len < 6:
    strength = "weak"

elif pass_len < 10:
    strength = "medium"

elif pass_len > 10:
    strength = "strong"

print("The password is:" , strength )

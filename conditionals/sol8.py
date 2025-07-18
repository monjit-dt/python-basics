pet_species = (input("write the spicies name: ")).lower()

if (pet_species != "dog") and pet_species !="cat":
    print("invalid spicies")
    exit()

pet_age = float(input("write the spicies age: "))

if (pet_species== "dog") and (pet_age < 2):
    a= "Puppy food"

elif pet_species =="cat" and pet_age > 5 :
    a= "Senior Cat food"

else:
    a = "no data knwon to us"

print(a)
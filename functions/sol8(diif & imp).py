def look(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}")   #print is used because we want to display the key-value pair not calculate or reuse the output
    
look(Name = "Monjit" , age = 22 , grad = "yes")
look(Name = "Monjit" , age = 22 , grad = "yes" , cgpa = 6.3)
text = input("write the text want to reverse: ")
rev_str = ""

for char in text :
    rev_str = char + rev_str        #not in real life scenario- takes the char one by one to add in rev strng
print("The reversed string is : " , rev_str)


#for real life scenario

text = input("write the text want to reverse: ")
rev_str = ""

for i in range(len(text) - 1, -1 ,-1) :

# takes the len of text then -1 is done to go to last index value then -1 is where to stop(not inclusive) 
# and finally last -1 is step to move here 1 step backwards
    
    rev_str = rev_str + text[i]      #i is added 2nd cos range will give values from backwards

print("The reversed string is : " , rev_str)
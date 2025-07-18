#It is done using set because it only detects unique values

list = [1,2,3,4,5,3,2,7,4]

unique_item = set()     #set is used here It is usually given by parenthesis but for empty set this is the way

for i in list :
    if i in unique_item:
        print("Duplicate found using set: " , i)  #i is the number currently being checked.If it’s already in the set → it is a duplicate.
        break
    else:
        unique_item.add(i)          #add Is used as append is not supported for set



# It is done using list, it doesnt detects unique values And takes longer time for large values of list 

list = [1,2,3,4,5,3,2,7,4]

list_item = []    #List is used here

for i in list :
    if i in list_item:
        print("Duplicate found Using list: " , i)  #i is the number currently being checked.If it’s already in the set → it is a duplicate.
        break
    else:
        list_item.append(i)         #append Is used as add is not supported for list


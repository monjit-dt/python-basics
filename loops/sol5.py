word = input("word is: ")

for char in word:
   if word.count(char) == 1 :
      print("first non-repeated word is: " , char)
      break

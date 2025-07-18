num = int(input("write the number: "))

skip_num = int(input("write the no. youu want to skip: "))

for i in range(1,11):
    if i == skip_num:       #if want to skip a aprticular no. simply had done i==5 or 6 etc
        continue            #simply skips the rest of code once continue is seen and go for next loop iteration
    result = num * i
    print(num, "x", i, "=", result)
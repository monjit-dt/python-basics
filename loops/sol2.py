num = int(input("write the number: "))
sum_even = 0
count_even = 0

for i in range(1,num + 1):
    if i % 2 == 0:
        sum_even = sum_even + i     #gives the sum of even numbers by adding i every time "i" gets even number
        count_even = count_even + 1     #gives the numbers of even numbers by adding 1 every time it gets even number

print("Sum of even numbers is: " , sum_even)
print("Number of even numbers is: " , count_even)
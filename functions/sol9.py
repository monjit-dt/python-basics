def even(num):
    for i in range(0 , num + 1):
        if i % 2 == 0:
            yield i

for new_num in even(11):
    print(new_num)            
import random
stroka = "privet eto ozon"
for i in range(len(stroka)):
    print(stroka[i])

arr = stroka.split()
random.shuffle(arr)
print(arr)
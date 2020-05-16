#Задание: Вывести таблицу умножения

range_1 = (1,2,3,5,6,7,8,9,10)
range_2 = (1,2,3,5,6,7,8,9,10)
for a in range_1:
    for b in range_2:
        print(str(a)+str(" * ") + str(b) + str(" = ") + str(a*b))
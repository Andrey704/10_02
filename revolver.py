#давайте напишем программу русской рулетки

import random

amount_of_bullets = int(input("Сколько вы хотите вставить патронов?"))

baraban = [0, 0, 0, 0, 0, 0]
# 0 -аналогия пустого гнезда
# 1 - аналогия гнезда с патроном

for i in range(amount_of_bullets):
    print(i)
    baraban[i] = 1

print("Посмотрите на барабан", baraban)

how_much = int(input("сколько раз вы собираетесь нажать на курок? "))
for i in range(how_much):
    random.shuffle(baraban)
    if baraban[0] == 1:
        print("Бабах")
        exit()
    else:
        print('щелк')

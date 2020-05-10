alive = True
while alive:
    status = input("Введите ваш статус по здоровью: ")
    if status == "bad":
        print("Оставайтесь дома и пейте чай")
        break
    else:
        print("Приступайте к работе")
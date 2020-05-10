age = int(input("Введите ваш возраст: "))
if age > 18 and age < 80:
    print("Проходите на наш ресурс")
elif age > 80:
    print("сайт закрыт на карантин")
else:
    print("Уходите")

job = input("Введите вашу должность: ")
if job == "admin" or job=="superadmin":
    print("Вам все можно")
else:
    print("Доступ запрещен")
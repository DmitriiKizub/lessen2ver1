year_Pushkin = int(input("Укажите год рождения А.С Пушкина? "))

if year_Pushkin == 1799:
   # print(type(year_Pushkin))
    year_Pushkin = int(input("Какой день рождения А.С Пушкина? "))
    if year_Pushkin == 23:
        print('Верно')
    else:
        print('Не верный день рождения')
else:
    print('Не вреный год')

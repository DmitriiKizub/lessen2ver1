# Билл Гейтс 1955.г
year_billGeitc = None
# Джон Рокфеллер 1839 г
year_DjonRok = None
# Эндрю Карнеги 1835 г
year_Karnegi = None
# Генри Форд 1863 г
year_Ford = None
# Марк Цууенберг 1984
year_Cukenberg = None
otvet = 'Да'

while otvet == 'Да' or otvet == 'да':
    year_billGeitc = input('Введите год рождения Билла Гейтса: ')
    year_DjonRok = input('Введите год рождения Джона Рокфеллера: ')
    year_Karnegi = input('Введите год рождения Эндрю Карнеги: ')
    year_Ford = input('Введите год рождения Генри Форда: ')
    year_Cukenberg = input('Введите год рождения Марка Цукенберга: ')

    if year_billGeitc == '1955':
        year_billGeitc = 1
    else:
        year_billGeitc = 0
    if year_DjonRok == '1839':
        year_DjonRok = 1
    else:
        year_DjonRok = 0
    if year_Karnegi == '1835':
        year_Karnegi = 1
    else:
        year_Karnegi = 0
    if year_Ford == '1863':
        year_Ford = 1
    else:
        year_Ford = 0
    if year_Cukenberg == '1984':
        year_Cukenberg = 1
    else:
        year_Cukenberg = 0
    summ_otvet = year_billGeitc + year_DjonRok + year_Ford + year_Karnegi + year_Cukenberg
    print("Кол-во правильных ответов:", summ_otvet)
    print('Кол-во ошибок: ', 5 - (summ_otvet))
    print('Процент правильных ответов: ', (summ_otvet) * 100 / 5, '%')
    print('Процент не правильных ответов: ', (5 - (summ_otvet)) * 100 / 5, '%')
    otvet = input('Хотите повторно пройти тест? Да\Нет ')
    while 'Нет' != otvet and 'Да' != otvet and 'да' != otvet and 'нет' != otvet:
        otvet = input('Выбирите один из вариантов: Да\Нет ')
    while otvet == 'Нет' or otvet == 'нет':
        print('end')
        break

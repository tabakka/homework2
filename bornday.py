ask = int(input('Введите год рождения А.С. Пушкина: '))
bornyear = 1799
bornday = '6 июня'
if ask == bornyear:
    print('Верно!')
    ask_day = input('Введите день рождения: ')
    if ask_day == bornday:
        print('Верно!')
    else:
        print('Неверный день рождения')
else:
    print('Неверно!')
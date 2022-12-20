ask = None
bornyear = 1799
bornday = '6 июня'
while ask != bornyear:
    ask = int(input('Введите год рождения А.С. Пушкина: '))
    if ask == bornyear:
        print('Верно!')
        while ask != bornday:
            ask_day = input('Введите день рождения: ')
            if ask_day == bornday:
                print('Верно!')
                break
            else:
                print('Неверный день рождения')
    else:
        print('Неверно!')
print('Ты молодец!')
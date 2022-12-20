Pushkin = 1799
Gogol = 1809
Tolstoy = 1828
Chehov = 1860
Dostoevskiy = 1821
effort = 0
right = 0
wrong = 0

ask1 = int(input('Год рождения Пушкина: ')) # 1799
effort += 1
if ask1 == Pushkin:
    right += 1
else:
    wrong +=1

ask1 = int(input('Год рождения Гоголя: ')) # 1809
effort += 1
if ask1 == Gogol:
    right += 1
else:
    wrong +=1

ask1 = int(input('Год рождения Толстого: ')) # 1828
effort += 1
if ask1 == Tolstoy:
    right += 1
else:
    wrong +=1

ask1 = int(input('Год рождения Чехова: ')) # 1860
effort += 1
if ask1 == Chehov:
    right += 1
else:
    wrong +=1

ask1 = int(input('Год рождения Достоевского: ')) # 1821
effort += 1
if ask1 == Dostoevskiy:
    right += 1
else:
    wrong +=1

print('количество правильных ответов:', right)
print('количество ошибок', wrong)
print('процент правильных ответов', right / effort * 100)
print('процент неправильных ответов', wrong / effort * 100)
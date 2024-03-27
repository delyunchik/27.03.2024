from random import choice

def gen_login(name):
    """Функция генерации логина из ФИО
    Аргументы:
        name: строка с полным Фамилия Имя Очество
    Возвращаемое значение:
        строка: сформированный логин
    """
    fio = name.split()  # разбиваю строку по пробелам
    return f'{fio[0]}_{fio[1][0]}{fio[2][0]}'


def gen_password():
    """Функция генерации пароля
    Возвращаемое значение:
        строка: сформированный 10-значный пароль
    """
    chars_1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars_2 = 'abcdefghijklmnopqrstuvwxyz'
    chars_3 = '0123456789'
    pwd = ''
    # ниже секретный алгоритм формирования пароля
    for _ in range(3):
        pwd += choice(chars_1)
    for _ in range(2):
        pwd += choice(chars_3)
    pwd += choice(chars_1)
    for _ in range(3):
        pwd += choice(chars_2)
    pwd += choice(chars_3)
    return pwd


f = open('scientist.txt', encoding='utf-8-sig')  # открываю исходный файл
lst = []  # пустой список
for line in f.readlines():  # читаю построчно файл
    a = line.strip().split('#')
    lst.append(a)  # добавляю в список поэлементно

for i in range(len(lst)):  # перебираю список по индексам
    if i == 0:  # заголовок
        lst[i].append('login')
        lst[i].append('password')
    else:
        lst[i].append(gen_login(lst[i][0]))
        lst[i].append(gen_password())

# открываю выходной файл
f2 = open('scientist_password.csv ', 'w', encoding='utf-8-sig')
for a in lst:  # построчно записываю список
    print(','.join(a), file=f2)  # разделители - запятые

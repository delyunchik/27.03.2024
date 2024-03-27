from random import choice

# подготовка таблицы перестановок для функции хэширования
tab = [ i for i in range(1024) ]  # список от 0 до 1023
tab2 = []  # таблица перестановок
for i in range(1024):
    x = choice(tab)  # беру случайным образом из tab
    tab2.append(x)  # добавляю последовательно в tab2
    tab.remove(x)


def gen_hash(fio):
    """Функция генерации хэша по фамилии
    Аргументы:
        fio: строка Фамилия Имя Отчество
    Возвращаемое значение:
        целое: значение хэш функции
    """
    hash = 0
    for j in range(len(fio)):  # индексы символов в ФИО
        hash += tab2[ord(fio[j]) % 1024]  # по алгоритму
    hash %= 2048
    return hash


# открываю исходный файл
f = open('scientist.txt', encoding='utf-8-sig')
lst = []
for line in f.readlines():  # заполняю список
    a = line.strip().split('#')
    lst.append(a)

for i in range(len(lst)):  # добавляю столбец хэша
    if i == 0:  # заголовок
        lst[i].insert(0, 'hash')
    else:
        fio = lst[i][0]
        lst[i].insert(0, str(gen_hash(fio)))

# открываю выходной файл
f2 = open('scientist_with_hash.csv', 'w', encoding='utf-8-sig')
for a in lst:  # записываю строки
    print(','.join(a), file=f2)

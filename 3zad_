f = open('scientist.txt', encoding='utf-8-sig')
head = f.readline().strip()
strok = f.readlines()
s = input()
s = str(s)
den1 = int(s[:2])
mes1 = int(s[3:5])
god1 = int(s[6:])
k = 0
while s != 'эксперимент':
    for i in range(len(strok)):
        a = strok[i].strip().split('#')
        god = int(a[2][:4])
        mes = int(a[2][5:7])
        den = int(a[2][8:])
        im = a[0].split()
        if den1 == den:
            if mes1 == mes:
                if god1 == god:
                    print(f'Ученый {im[0]} {im[1][0]}.{im[2][0]} создал препарат: {a[1]} - {s}')
                    k += 1
    if k == 0:
        print('В этот день ученые отдыхали')
    s = input()
# 1489-05.21
# 21.05.1489

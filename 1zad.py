f = open('scientist.txt', encoding='utf-8-sig')
head = f.readline().strip()
head += ';Total'
strok = f.readlines()
# 2 data
mn = 1000000
f = open('scientist_origin.txt', 'w', encoding='utf-8-sig')
print(head, file=f)
for i in range(len(strok)):
    a = strok[i].strip().split('#')
    if int(a[2][:4]) < mn:
        mn = int(a[2][:4])
print(mn)

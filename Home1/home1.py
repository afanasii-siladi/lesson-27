'''
1 згенерувати квадрати значень від 0 до 100000 i записати у різні файли:
    - значення кратні 3
    - значення кратні 5
    - парні числа

sum = 0

for i in range(100000):
    if i % 3 == 0:
        sum += i    
'''
q = []
f = []
w = []
for i in range(100000):
    i = i*i
    if 15 % 3 == 0:
        q.append(i)
    elif 25 % 5 == 0:
        f.append(i)
    elif 10 % 2 == 0:
        w.append(i)
    else:
        print('Next')

q = str([])
f = str([])
w = str([])

fp = open('Home1/data5.txt', 'w')
fp.write(f)
fp.close()

fp = open('Home1/data2.txt', 'w')
fp.write(w)
fp.close()

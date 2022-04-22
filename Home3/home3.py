'''
3 написати власний генератор, який повертає значення як це робить range():
    може приймати start, end, step i поверне відповідні згенеровані значення

    my_nums = (i*i for i in [1, 2, 3, 4, 5, 6])
print(type(my_nums))
print(my_nums)


for element in my_nums: #print(next(my_nums)) print(next(my_nums)) print(next(my_nums))
    if element == 9:
        print(element)
        break
    print(element)

print('---------')

for element in my_nums: #print(next(my_nums)) print(next(my_nums)) print(next(my_nums))
    print(element)
'''

my_generator = (i*i for i in [13, 12, 11, -14, -15, -16])

for i in my_generator:
    if i == 225:
        print(i)
        break
    print(i)

for i in my_generator:
    print(i)

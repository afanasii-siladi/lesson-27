'''
4 написати програму яка генерує одне рандомне число random_number від 0 до 100, а потім генерує рандомні
    числа від 0 до 100 поки не вгадає random_number
'''
import random

random_number = random.randint(1, 100)

print(random_number)
while True:
    random_number1 = random.randint(1, 100)

    if random_number != random_number1:
        print('-----------')
        print(random_number, '!=', random_number1)
    else:
        print('-----------')
        print('Very good')
        print(random_number, '=', random_number1)
        break

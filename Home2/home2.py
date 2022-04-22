'''
2 написати генератор безпечних паролів. Згенерувати i записати 1000 паролів в файл
'''
import random


def password_generator():
    elem = '1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM-@#?!_'

    for i in range(1000):
        res = ''.join(random.sample(elem, random.randint(8, 16)))

        yield res
        with open('test.txt', 'a') as f:
            f.write(str(res))

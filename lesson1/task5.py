"""
блок-схема
https://drive.google.com/file/d/1R28llY4Z7Rl5M8DAA5Rf4IWgpxcrZCPY/view?usp=sharing
Найти среднее число. Задача 9
"""

numb1 = int(input('Введите первое целое число: '))
numb2 = int(input('Введите второе целое число: '))
numb3 = int(input('Введите третье целое число: '))

if numb1 != numb2 and numb2 != numb3:
    if numb1 < numb2:
        if numb1 < numb3:
            if numb2 < numb3:
                print('среднее: {}'.format(numb2))
            else:
                print('среднее: {}'.format(numb3))
        else:
            print('среднее: {}'.format(numb1))
    else:
        if numb2 < numb3:
            print('среднее: {}'.format(numb3))
        else:
            print('среднее: {}'.format(numb2))
else:
    print('Невозможно найти среднее число, т.к. два из трех чисел равны между собой')
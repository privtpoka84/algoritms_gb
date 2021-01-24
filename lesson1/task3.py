"""
блок-схема
https://drive.google.com/file/d/1R28llY4Z7Rl5M8DAA5Rf4IWgpxcrZCPY/view?usp=sharing
Определение существования треугольника
"""
numb1 = int(input('Введите целое число - первую сторону треугольника:'))
numb2 = int(input('Введите целое число - вторую сторону треугольника:'))
numb3 = int(input('Введите целое число - третью сторону треугольника:'))

if numb1 + numb2 > numb3:
    if numb1 + numb3 > numb2:
        if numb2 + numb3 > numb1:
            if numb1 == numb3 == numb2:
                print('Треугольник существует и он равносторонний')
            elif numb1 == numb2 or numb2 == numb3 or numb3 == numb1:
                print('Треугольник существует и он равнобедренный')
            else:
                print('Треугольник существует и он разносторонний')
else:
    print('Треугольник не существует')





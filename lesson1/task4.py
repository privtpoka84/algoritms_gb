"""
блок-схема
https://drive.google.com/file/d/1R28llY4Z7Rl5M8DAA5Rf4IWgpxcrZCPY/view?usp=sharing
Определение високосного года. Задача 8
"""

year = int(input('Введите год, который хотите проверить: '))
if year % 400 == 0:
    print('Этот год високосный')
elif year % 100 == 0:
    print('Этот год не високосный')
elif year % 4 == 0:
    print('Этот год високосный')
else:
    print('Этот год не високосный')
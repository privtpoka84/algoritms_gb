"""
блок-схема
https://drive.google.com/file/d/1R28llY4Z7Rl5M8DAA5Rf4IWgpxcrZCPY/view?usp=sharing
Определение буквы по номеру. Задача 6
"""

numb = int(input('Введите целое число:'))
if numb > 0:
    word = 96 + numb
    print(chr(word))
else:
    print('Число отрицательное, введите, пожалуйста, положительное число')



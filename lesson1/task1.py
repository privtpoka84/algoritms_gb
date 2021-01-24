numb = int(input('Введите целое трехзначное число: '))
if numb < 0:
    numb = numb * -1
num100 = numb // 100
num1 = numb % 10
num10 = (numb - num100 * 100 - num1) // 10
print('Сумма: {}'.format(num100 + num10 + num1))
print('Произведение: {}'.format(num100 * num10 * num1))
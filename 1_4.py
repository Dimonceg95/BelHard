# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных
number_1 = input('введите первое число:')
number_2 = input('введите второе число:')
number_3 = input('введите третье число:')
number_1 = int(number_1)
number_2 = int(number_2)
number_3 = int(number_3)
a = int(number_1>0)
b = int(number_2>0)
c = int(number_3>0)
d = a + b + c
e = str(d)
print('Количество положительных чисел=' + e)
f = 3 - d
g = str(f)
print('Количество отрицательных чисел=' + g)

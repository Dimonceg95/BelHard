# Заполнить список степенями числа 2 (от 2^1 до 2^n)
n = input('введите n:')
n = int(n)
n += 1
a = [2**i for i in range(1, n)]
print(a)

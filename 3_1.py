# Вывести первые N цисел кратные M и больше K
N = int(input('N = '))
M = int(input('M= '))
K = int(input('K= '))
x = 0
L = N * M +  1
while x < L:
    x += 1
    K = K + 1
    a = K
    if K % M != 0:
        continue
        ...
    print(a)
    ...
...

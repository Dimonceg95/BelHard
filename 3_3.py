#**Вывести четные числа от 2 до N по 5 в строку
a = 2
b = int(input('введите ваше число: '))
x = 1
f = int(b/10)*10
g = b - f
print(f)
print(g)
while x < f:
    x +=10
    if a % 2 == 0:
        c = [a, a+2, a+4, a+6, a+8]
        print(c)
        a = a + 10
        ...
    ...
...
if g < 2:
    a = a
elif g < 4:
    c = [a]
    print(c)
elif g < 6:
    c = [a, a+2]
    print(c)
elif g < 8:
    c = [a, a+2, a+4]
    print(c)
elif g < 10:
    c = [a, a+2, a+4, a+6]
    print(c)

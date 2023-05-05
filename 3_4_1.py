#1. Вводится число, найти его максимальную цифру
# a = input('введите число: ')
# b = set(a)
# c = list(b)
# c.sort()
# print(c[-1])

a = '32156456484.5412354646543'
b = 0
for i in a:
    # if i in '.-+/':
    #     continue
    if not i.isdigit():
        continue
    d = int(i)

    if b < d:
        b = d

print(b)
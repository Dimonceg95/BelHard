#Написать функцию перевода десятичного числа в двоичное и обратно, без
#использования функции int

def in_binary(c):
    a = c
    b = []
    while c > 1:
        if c % 2 == 1:
            b += '1'
            c = (c - 1) / 2
        elif c % 2 == 0:
            b += '0'
            c /= 2
    if c == 1:
        b += '1'
    else:
        b += '0'
    b.reverse()
    d = ''.join(b)
    return d
print(in_binary(128))
def in_decimal(a):
    a = str(a)
    a = list(a)
    a.reverse()
    c = 0
    d = 0
    for i in a:
        if i == '1':
            d += 2 ** c
            c += 1
        elif i == '0':
            c += 1
    return d


print(in_decimal('1111100'))

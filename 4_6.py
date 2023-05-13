# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

a = [1, 2, 3, 4, 5, 6, 3, 2, 1, 3]
def sorted_odd_even(a):
    b = []
    c = []
    for i in a:
        if i % 2 == 1:
            b.append(i)
        elif i % 2 == 0:
            c.append(i)
    a = b + c
    return a
print(sorted_odd_even([1, 5, 6, 4, 44, 52, 1, 11]))
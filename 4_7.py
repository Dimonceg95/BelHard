# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

a = [1, 3, 5, 9, 77, 54]
def sum_neighbors(a):
    b = []
    a.append(a[0])
    a.reverse()
    a.append(a[1])
    a.reverse()
    for i in range(1, (len(a)-1)):
        c = a[i - 1] + a[i + 1]
        b.append(c)
    return b
print(sum_neighbors([1, 2, 3, 56, 54, 41]))

# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

a = [1, 2, 3, 4, 5, 6, 7, 32, 2, 4]
def reverse_list(a):
    b = len(a)
    for i in a[::-1]:
        a.append(i)
    del a[:b]
    return a
reverse_list(a)
print(reverse_list([1, 2, 3, 4, 5, 6, 2]))




# a = [*(a[i] for i in range(-1,-b-1,-1))]
# print(a)

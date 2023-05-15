# 1. Написать функцию-генератор, принимающую 3 аргумента (number, start, end), все аргументы целочисленные
# Генератор должен возвращать number в степени от start до end:
# number=2
# start=3
# end=5
# result: 8, 16, 32

def numbers(number, start, end):
    for i in range(start, end + 1):
        a = number ** i
        yield a

a = numbers(2, 3, 5)
# print([*a])
for i in a:
    print(i)
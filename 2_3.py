
n = input('введите n:')
n = int(n)
data = {i: {'name': input(f'name {i}:'), 'email': input(f'email {i}:')} for i in range(n)}
print(data)
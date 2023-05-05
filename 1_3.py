name = input('введите ваше имя:')
age = input('введите ваш возраст:')
city = input('введите ваш город:')

print('Hello ' + name + ' your age ' + age + ' you are from ' + city)
print('Hello {} your age {} you are from {}'.format(name, age, city))
print(f'Hello {name} your age {age} you are from {city}')

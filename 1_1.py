# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# способами
some_text = input('введите ваше предложение:')
a = some_text.replace(' ', '-')
print(a)
b = some_text.split( )
print(b)
b = '-'.join(b)
print(b)

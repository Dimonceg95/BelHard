#*"Угадай число"
#from random import randint
#a = randint(1, 100)
#Данная функция генерирует случайное число в заданном диапазоне,
#необходимо написать игру "угадай число" и сказать сколько попыток ушло на
#это у пользователя
from random import randint
a = randint(1, 100)
print(a)
c = 1
b = int(input('гадай '))
while b != a:
    c +=1
    b = int(input('гадай еще '))
    if b == a:
        print('загаданное число ',b)
        print('число попыток=', c)

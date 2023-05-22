# #написать функцию которая принимает положительное число и генерировать
# #треугольник вида
#
# def odd_triangle(depth):
#     trinagle = []
#     for i in range(depth):
#         line = []
#         start = i*(i+1)+1
#         end = start + 1 + i * 2
#         for j in range(start, end, 2):
#             line.append(j)
#         trinagle.append(line)
#     return trinagle
#
# print(odd_triangle(7))
#
# sms = 'LONDON'
# key = 'SYSTEM'
# def vernama_encode(key, sms):
#     return [ord(key[i]) ^ ord(sms[i]) for i in range(len(key))]
# result = vernama_encode(sms, key)
# # print(result)
# a = {
#             'belarus': ['gomel', 'minsk'],
#             'russia': ['kazan', 'moskau'],
#             'ukraine': ['kiev', 'lviv']
# }
# x = 'belarus'

# 2. Написать функцию-генератор, принимающая целое число count, и возвращающая указанное колличество
# простых чисел:
# count=5
# result=2, 3, 5, 7, 11

# 1) конструктор класса принимает аргументы text: str, link:str конструктор класса должен обьявлять
# аргументы объекта на основании принятых аргументов
# 2) написать метод объекта dict, возвращающий словарь, где в качестве ключей доджны выступать имена аргументов в виде
# стро, а значниями должны являться значения аргументов
#
# class Button:
#
#     def __init__(self, text: str, link:str) -> None:
#         self.text = text
#         self.link = link
#
#     def dict(self) -> dict:
#         return {'text': self.text, 'link': self.link}
# # # написать класс Keyboard
# # конструктор класса принимает name: strи список экземпляров класса Button
# # и обьявляющий атрибуты объукта на основании аргументов
# # написать метод объекта dict возвращающий словарь с ключами в виде имен атрибутов в виде строк, а значения
# # значения атрибутов, при чем каждый экземпляр класса Button в соответствующей атрибуте, так же должен быть приведен к
# # словарю
#
# class Keyboard:
#
#     def __init__(self, name: str, button_list: list):
#         self.name = name
#         self.button_list = button_list
#
#     def dict(self) -> {}:
#         return {'name': self.name, 'button_list': [button.dict() for button in self.button_list]}
#
#
# # button1 = Button('Hi', 'asdasd')
# # print(button1.dict())

# 1) конструктор класса принимает аргументы text: str, link:str конструктор класса должен обьявлять
# аргументы объекта на основании принятых аргументов
# # 2) написать метод объекта dict, возвращающий словарь, где в качестве ключей доджны выступать имена аргументов в виде
# # стро, а значниями должны являться значения аргументов
#
# class Button:
#
#     def __init__(self, text: str, link:str) -> None:
#         self.text = text
#         self.link = link
#
#     def dict(self) -> dict:
#         return {'text': self.text, 'link': self.link}
# # # написать класс Keyboard
# # конструктор класса принимает name: strи список экземпляров класса Button
# # и обьявляющий атрибуты объукта на основании аргументов
# # написать метод объекта dict возвращающий словарь с ключами в виде имен атрибутов в виде строк, а значения
# # значения атрибутов, при чем каждый экземпляр класса Button в соответствующей атрибуте, так же должен быть приведен к
# # словарю
#
# class Keyboard:
#
#     def __init__(self, name: str, button_list: Button):
#         self.name = name
#         self.button_list = button_list
#
#     def dict(self) -> {}:
#         return {'name': self.name, 'button_list': [button.dict() for button in self.button_list]}


# button1 = Button('Hi', 'asdasd')
# print(button1.dict())
# TODO дан файл содержащий в себе строки с числами, создать файл в котором каждая строка
# будет содердать число равное сумме цифр в соответствубщзей стркое исходного файла
# with  open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
#     for line in input_file:
#         line = sum([int(number) for number in line.strip().split() if number])
#         output_file.write(f'{line}\n')
#
#

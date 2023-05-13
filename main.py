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
# print(result)
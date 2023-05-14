# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

dict_city_country = {
    'belarus': ['1', '2', '3', '4'],
    'russia': ['5', '6', '7', '8']
}
x = '2'
print(*dict_city_country.values())
a = dict_city_country.values()
print(a)
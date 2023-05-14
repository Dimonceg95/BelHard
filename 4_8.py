# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны


def country_by_sity(x):
    x = x.lower()
    dict_city_country = {
        'belarus': ['gomel', 'minsk'],
        'russia': ['kazan', 'moskau'],
        'ukraine': ['kiev', 'lviv']
    }
    for country_city in dict_city_country.items():
        for city in country_city[1]:
            if city == x:
                return (country_city[0])

print(country_by_sity('Lviv'))
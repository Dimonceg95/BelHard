# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

def id_no_mails(dict_city_country):
    id_list = []
    for id_info in dict_city_country.items():
        print(id_info)
        info = id_info[1]
        print(info)
        a = 'mail'
        if a not in info:
            info['mail'] = ''
            print(info)
        if info['mail'] == '':
           id_str = ''
           id_str += id_info[0]
           id_list.append(id_str)

    return id_list


dict_city_country = {
        'id22': {
            'name': 'vasya',
            'surname': 'vasilev',
            'phone_number': '375333755775',
            'mail': 'vasya23@mail.ru'
        },
        'id24': {
            'name': 'petya',
            'surname': 'petrov',
            'phone_number': '375291865742',
        },
        'id23': {
            'name': 'petya',
            'surname': 'petrov',
            'phone_number': '375291865742',
            'mail': ''
        },
}

print(id_no_mails(dict_city_country))





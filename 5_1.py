# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле

class Car:

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.is_busy = False
        self.color = color
        self.count_passenger_sears = count_passenger_seats
        self.is_baby_seat = is_baby_seat

    def __str__(self) -> str:
        return f'color: {self.color}, count passenger seats: {self.count_passenger_sears}, is_baby_seat:' \
               f' {self.is_baby_seat}, is_busy: {self.is_busy}'
mersedes = Car('red', 5, True)
print(mersedes)
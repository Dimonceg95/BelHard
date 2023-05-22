# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None


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
audi_a2 = Car('blue', 4, False)
bmw = Car('blue', 5, False)
class Taxi:
    def __init__(self, cars: [Car]):
        self.cars = cars

    def find_car(self, count_passenger_seats: int, is_baby: bool):
        self.count_passenger_sears = count_passenger_seats
        self.is_baby = is_baby
        for car in Car:
            if count_passenger_seats == count_passenger_seats(car):
                print('ok')


# def find_car(self, ):






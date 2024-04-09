class Car:
    price = 1000000

    def horse_power(self):

        return 'лошадь сила', self.price


class Nissan(Car):
    price = 1500000

    def horse_power(self):

        return 'лошадь сила', self.price


class Kia(Car):
    price = 200000

    def horse_power(self):

        return 'лошадь сила', self.price


cube = Nissan()
rio = Kia()
cube.horse_power()
rio.horse_power()

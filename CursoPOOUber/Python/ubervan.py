from car import Car

class UberVan(Car):
    type_car_accepted = list
    seats_material = list

    def __init__(self,license,driver,type_car_accepted,seats_material):
        super().__init__(license,driver)
        self.type_car_accepted = type_car_accepted
        self.brand = seats_material
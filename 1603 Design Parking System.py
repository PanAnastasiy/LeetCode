class ParkingSystem(object):

    def __init__(self: object, big: int, medium: int, small: int) -> None:
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self: object, carType: int) -> bool:
        data = {1: 'big', 2: 'medium', 3: 'small'}
        if getattr(self, data[carType]) > 0:
            setattr(self, data[carType], getattr(self, data[carType]) - 1)
            return True
        return False


obj = ParkingSystem(1, 1,  0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))


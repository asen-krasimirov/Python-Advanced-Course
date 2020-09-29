class Parking:
    def __init__(self):
        self.__lot = set()

    def operation(self, __direction, car):

        action = {
            "IN": self.__lot.add,
            "OUT": self.__lot.remove
        }

        action[__direction](car)

    def print_cars(self):
        if self.__lot:
            print('\n'.join(self.__lot))
        else:
            print("Parking Lot is Empty")


number_of_command = int(input())
parking_lot = Parking()

for _ in range(number_of_command):
    direction, plate = input().split(', ')
    parking_lot.operation(direction, plate)

parking_lot.print_cars()

# Exercise 1 from powerpoint handout.

class Bus():
    """
    A class that describes a bus
    """
    num_bus_created = 0

    def __init__(self, seats, color, name):
        self.number_of_seats = seats
        self.color = color
        self.driver_name = name
        self.increment_bus_created()

    def increment_bus_created(self):
        # self.num_bus_created = self.num_bus_created + 1
        Bus.num_bus_created = self.num_bus_created + 1

    def change_color(self,color):
        self.color = color

# Bus = Bus(34, "Yellow", "Mikayla")
# print(Bus.color)
# print(increment_bus_created)


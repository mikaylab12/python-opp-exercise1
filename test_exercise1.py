import unittest

from main import Bus


class TestBusClass(unittest.TestCase):
    """
    Testcase class for Bus
    """
    # Bus = Bus(34, "Yellow", "Mikayla")
    def setUp(self) -> None:
        self.bus = Bus(34, "Yellow", "Mikayla")

    def test_class_init_method(self):
        self.assertEqual(self.bus.color, "Yellow", "Color should be Yellow")
        self.assertEqual(self.bus.driver_name, "Mikayla", "The name of the driver should be Mikayla")
        self.assertEqual(self.bus.number_of_seats, 34, "The number of seats should be 34(thirty-four")

    def test_change_color(self):
        self.bus.change_color("Blue")
        self.assertEqual(self.bus.color, "Blue", "The bus should be Blue")

    def test_num_bus_created(self):
        # bus_one = Bus(10, "Green" , "Jack")
        # bus_two = Bus (20, "Blue", "Test")
        self.assertEqual(self.bus.num_bus_created, 3, "There should have been 3 buses created")
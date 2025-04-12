import unittest
from src.car import Car

class TestCarMovement(unittest.TestCase):

    def test_rotation_left(self):
        car = Car("A", 0, 0, "N")
        car.rotate_left()
        self.assertEqual(car.direction, "W")

    def test_rotation_right(self):
        car = Car("A", 0, 0, "N")
        car.rotate_right()
        self.assertEqual(car.direction, "E")

    def test_move_forward_north(self):
        car = Car("A", 0, 0, "N")
        x, y = car.move_forward()
        self.assertEqual((x, y), (0, 1))

    def test_move_forward_west(self):
        car = Car("B", 3, 3, "W")
        x, y = car.move_forward()
        self.assertEqual((x, y), (2, 3))

if __name__ == '__main__':
    unittest.main()

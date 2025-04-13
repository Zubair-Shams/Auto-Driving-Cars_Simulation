import unittest
from src.car import Car

 """This test class checks if the car moves and turns correctly."""


class TestCarMovement(unittest.TestCase):

    def test_rotation_left(self): """ checing that car left from North direction to West"""
        car = Car("A", 0, 0, "N")
        car.rotate_left()
        self.assertEqual(car.direction, "W")

    def test_rotation_right(self): """checing that car right from North direction to East"""
        car = Car("A", 0, 0, "N")
        car.rotate_right()
        self.assertEqual(car.direction, "E")

    def test_move_forward_north(self): """checing that car moving Forward while facing North direction increasing Y by 1"""
        car = Car("A", 0, 0, "N")
        x, y = car.move_forward()
        self.assertEqual((x, y), (0, 1))

    def test_move_forward_west(self):"""checing that car moving Forward while facing West direction decreasing X by 1"""
        car = Car("B", 3, 3, "W")
        x, y = car.move_forward()
        self.assertEqual((x, y), (2, 3))

if __name__ == '__main__':
    unittest.main()

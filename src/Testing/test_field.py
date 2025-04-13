import unittest
import sys, os

# Adding the parent directory to the path due to which we can access to project fiels
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from field import Field #now we can import filed Class from the project

class TestField(unittest.TestCase): 
"""this class will check that the car is in the given grid or not"""
    def setUp(self):
        self.f = Field(10, 10)   # this will create grid ten by ten to check different position

    def test_inside_bounds(self):  """ this test case will check that 5 by 5 is inside the box or not if yes return true"""
        self.assertTrue(self.f.is_within_bounds(5, 5)) 

    def test_outside_bounds(self): """this test case will return false because ediges are not included"""
        self.assertFalse(self.f.is_within_bounds(10, 10))  

    def test_negative_coords(self): """if there is negative value then return False as negtive is out of the box"""
        self.assertFalse(self.f.is_within_bounds(-1, 0))  

if __name__ == '__main__': 
    unittest.main()

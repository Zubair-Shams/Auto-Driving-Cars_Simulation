import unittest
import sys, os

# Adding the parent directory to the path due to which we can access to project fiels
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from field import Field #now we can import filed Class from the project

class TestField(unittest.TestCase): 

    def setUp(self):
        self.f = Field(10, 10)   # Creating a 10x10 field to test the confirmation

    def test_inside_bounds(self):  # Tst case: check if a normal inside coordinate returns True 
        self.assertTrue(self.f.is_within_bounds(5, 5))  # should be inside

    def test_outside_bounds(self): #Test Case: check if a coordinate on the border edge returns False it mean fasle
        self.assertFalse(self.f.is_within_bounds(10, 10))  # max edges will be invalide invalid

    def test_negative_coords(self): #Test Case: check if a coordinate that is negative on the border edge returns False
        self.assertFalse(self.f.is_within_bounds(-1, 0))  # negative x is incorrect 

if __name__ == '__main__': #start execution when this called
    unittest.main()

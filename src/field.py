# src/field.py

"""it is  Stores the field size (width and height)Provides method to check if a car's position is within bounds
"""
class Field:
    def __init__(self, weidth, heights):
        self.weidth = weidth
        self.heights = heights

    def is_within_bounds(self, x, y):
        # check if x and y inside the field or not
        return 0 <= x < self.weidth and 0 <= y < self.heights

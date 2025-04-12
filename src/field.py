# src/field.py
class Field:
     # storing field size for checking bounds letar
    def __init__(self, weidth, heights):
        self.weidth = weidth
        self.heights = heights

    def is_within_bounds(self, x, y):
        # check if x and y inside the field or not
        return 0 <= x < self.weidth and 0 <= y < self.heights

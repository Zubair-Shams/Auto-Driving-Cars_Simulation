# src/test_field.py

from field import Field

f = Field(10, 10)

print(f.is_within_bounds(5, 5))   # True
print(f.is_within_bounds(10, 10)) # False (outside)
print(f.is_within_bounds(-1, 0))  # False

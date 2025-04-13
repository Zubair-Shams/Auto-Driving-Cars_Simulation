# src/test_field.py

from field import Field

f = Field(10, 10)

print(f.is_within_bounds(5, 5))   # it will give True in input
print(f.is_within_bounds(10, 10)) # it will give False in output
print(f.is_within_bounds(-1, 0))  # it also give False in output

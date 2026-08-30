# Notes:
# 1. The problem asks us to calculate the total surface area of a cylinder.
# 2. I take radius and height as integer inputs and store them in radius and height.
# 3. I store the value of PI as 3.142.
# 4. I use the formula 2 * PI * radius * (radius + height) to calculate the area.
# 5. I store the calculated value in the area variable.
# 6. I use f-string formatting with :.4f to print the area up to 4 decimal places.
# 7. Concept: input(), variables, arithmetic operators, formula-based calculation, and formatted output.

import DataTypes

radius = int(input())
height = int(input())

PI = 3.142

area = 2*PI*radius* (radius + height)

print(f"{area:.4f}")
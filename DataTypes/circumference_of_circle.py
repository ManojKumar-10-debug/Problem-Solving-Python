# Notes:
# 1. The problem asks us to find the circumference of a circle using the given radius.
# 2. I store 3.142 in PI because it is needed in the circumference formula.
# 3. I take the radius as an integer input and store it in radius.
# 4. I calculate the circumference using the formula 2 * PI * radius.
# 5. I store the calculated value in circumference.
# 6. I print circumference using an f-string and format it to 4 decimal places.
# 7. Concept: Variables, user input, arithmetic operators, formula, and decimal formatting.

import DataTypes

PI = 3.142

radius = int(input())

circumference = 2 * PI * radius

print(f"{circumference:.4f}")
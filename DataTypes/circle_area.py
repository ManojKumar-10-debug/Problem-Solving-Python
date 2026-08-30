# Formula area = pi*r*r
# pi = 3.142
# Notes:
# 1. The problem asks us to find the area of a circle using the given radius.
# 2. I store the value 3.142 in PI because it is needed in the area formula.
# 3. I take the radius as an integer input and store it in radius.
# 4. I calculate the area using the formula PI * radius * radius.
# 5. I store the calculated value in area.
# 6. I print area using an f-string and format it to 4 decimal places.
# 7. Concept: Variables, user input, multiplication, formula, and decimal formatting.

PI = 3.142

radius = int(input())

#  Formula
area = PI * radius * radius

print(f"{area:.4f}")
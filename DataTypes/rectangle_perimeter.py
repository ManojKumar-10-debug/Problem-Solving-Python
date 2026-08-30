# Notes:
#
# 1. The problem asks us to take the length and width of a rectangle
#    and find its perimeter.
#
# 2. I used input() to take the two values from the user.
#
# 3. int() converts the input values from string to integer.
#
# 4. length and width store the two input values.
#
# 5. I calculated the perimeter using the formula:
#    perimeter = 2 * (length + width)
#
# 6. The calculated value is stored in the perimeter variable.
#
# 7. Finally, I print perimeter to display the result.
#
# 8. The main concepts used are input(), int(), variables,
#    arithmetic operators, and print().



import DataTypes

length = int(input())
width = int(input())

perimeter = 2 * (length + width)

print(perimeter)
# Notes:
# 1. The problem asks us to convert a temperature from Fahrenheit to Celsius.
# 2. I take the Fahrenheit value as an integer input and store it in Fahrenheit.
# 3. I use the conversion formula (Fahrenheit - 32) * 5 / 9.
# 4. I first subtract 32 to adjust the Fahrenheit value, then multiply by 5 and divide by 9.
# 5. I store the calculated Celsius value in Celsius.
# 6. I print Celsius using an f-string and format the result to 4 decimal places.
# 7. Concept: User input, variables, arithmetic operations, formula, and decimal formatting.

import DataTypes

fahrenheit = int(input())

celsius = (fahrenheit - 32) * 5 / 9 #formula

print(f"{celsius:.4f}")
# Notes:
# 1. Problem: Check whether the given number is a 3-digit number and a multiple of 2, 5, and 10.
# 2. I take the number as input and store it in num.
# 3. I use 99 < num < 1000 to check whether num is a 3-digit number.
# 4. I use num % 10 == 0 to check whether num is a multiple of 10.
# 5. A multiple of 10 is automatically a multiple of both 2 and 5, so one check is enough.
# 6. I combine the two conditions using and because both must be satisfied.
# 7. I use a conditional expression to store "Yes" if both conditions are true, otherwise "No".
# 8. I store the result in res and print it.
# 9. Concepts used: %, and, chained comparison, conditional expression, and variable storage.

# ThreeDigit and Multiples of 2, 5, 10

import if_else

num = int(input())

res = "Yes" if 99 < num < 1000 and num % 10 == 0 else "No"

print(res)
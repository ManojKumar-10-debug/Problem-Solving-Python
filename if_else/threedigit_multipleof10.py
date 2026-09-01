# Notes:
# 1. The problem asks us to check whether the number is a 3-digit number
#    and also a multiple of 10.
# 2. I take the number as input and store it in num.
# 3. I use 99 < num < 1000 to check whether num is a 3-digit number.
# 4. I use num % 10 == 0 to check whether num is divisible by 10.
# 5. I combine both conditions using and because both must be true.
# 6. I use Python's conditional expression to choose "Yes" or "No".
# 7. I store the final result in res so I can reuse the result later
#    without writing the conditions again.
# 8. Finally, I print res.
# 9. Concepts used: input(), int(), %, and, chained comparison,
#    conditional expression, and variable storage.

import if_else

num = int(input())

res = "Yes" if 99 < num < 1000 and num % 10 == 0 else "No"

print(res)
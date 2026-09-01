"""
Notes:
1. Problem: Check whether the given number is a multiple of 5, 3, and 7.
2. I take the number as input and store it in num.
3. I use the modulus (%) operator to check divisibility by 5, 3, and 7.
4. I combine all three conditions using `and`, so all conditions must be True.
5. I use Python's conditional expression to choose "Yes" when all conditions are True; otherwise "No".
6. I store the selected result in res.
7. Finally, I print res.
8. Approach: Input → check divisibility → choose result → print result.
9. Concepts used: %, and, conditional expression, int input, and variable assignment.
"""

import if_else

num = (int(input()))

res = "Yes" if num % 5 == 0 and num % 3 == 0 and num % 7 == 0 else "No"

print(res)
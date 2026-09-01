"""
Notes:
1. Problem: Check whether the given number is a multiple of 5.
2. I take the number as input and store it in num.
3. I use num % 5 to find the remainder after dividing num by 5.
4. If the remainder is 0, I print "Yes" because num is a multiple of 5.
5. Otherwise, I print "No".
6. I used if-else to handle the two possible conditions.
7. Important concepts: input(), int(), modulus (%) and if-else.
"""

import if_else

num = int(input())

if num % 5 == 0:
    print("Yes")
else:
    print("No")
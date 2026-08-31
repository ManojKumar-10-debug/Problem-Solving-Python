# Notes:
# 1. The problem asks us to check whether the given number is even or odd.
# 2. I create even_odd() and pass num to it as an argument.
# 3. Inside the function, I use num % 2 to check the remainder after division by 2.
# 4. If the remainder is 0, the function returns "Yes"; otherwise, it returns "No".
# 5. I take the number as integer input and store it in num.
# 6. I call even_odd(num) and directly print the returned result.
# 7. Approach: take input → pass it to the function → check using % → return result → print it.
# 8. Python concepts: function, parameter, return value, if-else, modulus operator, and input().

import if_else
def even_odd(num):
    if num % 2 == 0:
        return "Yes"
    else:
        return "No"

num = int(input())
print(even_odd(num))
# Notes:
# 1. Problem: Print the first N even natural numbers.
# 2. I take N as input and store it in `n`.
# 3. I use a `for` loop because I need to repeat the process N times.
# 4. `range(1, n + 1)` generates values from 1 to N.
# 5. I multiply each `i` by 2 to generate the even numbers: 2, 4, 6, ...
# 6. `end=" "` keeps all numbers on the same line and adds a space after each.
# 7. Approach: take N → loop N times → generate each even number using `i * 2`
#    → print the numbers.
# 8. Concepts used: input(), for loop, range(), multiplication, and print().

n = int(input())

for i in range (1, n + 1):
    print(i * 2, end=" ")
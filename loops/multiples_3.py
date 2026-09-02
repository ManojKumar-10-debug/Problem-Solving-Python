# Notes:
# 1. Problem: Print the first N multiples of 3.
# 2. I take N as input and store it in `n`.
# 3. I use a `for` loop to repeat the process N times.
# 4. `range(1, n + 1)` generates values from 1 to N.
# 5. I multiply each `i` by 3 to generate the multiples: 3, 6, 9, ...
# 6. `end=" "` keeps all numbers on the same line with spaces.
# 7. Approach: take N → loop N times → calculate `i * 3` → print it.
# 8. Concepts used: input(), for loop, range(), multiplication, and print().

n = int(input())

for i in range (1, n + 1):
    print((i * 3), end=" ")
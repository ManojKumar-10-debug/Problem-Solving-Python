# Notes:
# 1. Problem: Print the first N odd natural numbers.
# 2. I take N as input and store it in `n`.
# 3. I use a `for` loop to repeat the process N times.
# 4. `range(1, n + 1)` generates values from 1 to N.
# 5. I use `(i * 2) - 1` to generate each odd number: 1, 3, 5, ...
# 6. `end=" "` keeps all numbers on the same line with spaces.
# 7. Approach: take N → loop N times → calculate odd number → print it.
# 8. Concepts used: input(), for loop, range(), multiplication, subtraction,
#    and print().

n = int(input())

for i in range (1, n + 1):
    print((i * 2) - 1, end=" ")
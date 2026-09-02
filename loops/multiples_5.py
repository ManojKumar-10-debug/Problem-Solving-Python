# Notes:
# 1. Problem: Print the first N multiples of 5.
# 2. I take N as input and store it in `n`.
# 3. I use a `for` loop to repeat the process N times.
# 4. `range(1, n + 1)` generates values from 1 to N.
# 5. I multiply `i` by 5 to generate the multiples: 5, 10, 15, ...
# 6. `end=" "` prints all multiples on the same line with spaces.
# 7. Approach: take N → loop N times → calculate `i * 5` → print it.
# 8. Concepts used: input(), for loop, range(), multiplication, and print().

n = int(input())

for i in range (1, n + 1):
    print((i * 5), end=" ")
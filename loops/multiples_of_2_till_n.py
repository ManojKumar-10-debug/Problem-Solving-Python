# Notes:
# 1. Problem: Print multiples of 2 from 2 up to N.
# 2. I take N as input and store it in `n`.
# 3. I use `range(2, n + 1, 2)` to generate the required numbers.
# 4. I start from 2 because 2 is the first multiple of 2.
# 5. `n + 1` makes the range include N when N itself is a multiple of 2.
# 6. The step `2` moves to the next multiple: 2, 4, 6, 8, ...
# 7. I print each value using `print(i, end=" ")` so they stay on one line.
# 8. Approach: start at 2 → jump by 2 → stop at N → print each value.
# 9. Concepts used: input(), for loop, range(start, stop, step), and print().

n = int(input())

for i in range(2, n + 1, 2):
    print(i, end=" ")
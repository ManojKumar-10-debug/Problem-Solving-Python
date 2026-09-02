# Notes:
# 1. Problem: Print numbers from 2 to N that are multiples of 2, 5, or 7.
# 2. I take N as input and store it in `n`.
# 3. I use a `for` loop to check every number from 2 to N.
# 4. `i % 2 == 0` checks whether `i` is a multiple of 2.
# 5. `i % 5 == 0` checks whether `i` is a multiple of 5.
# 6. `i % 7 == 0` checks whether `i` is a multiple of 7.
# 7. I use `or` because satisfying any one of the three conditions is enough.
# 8. If any condition is true, I print `i`.
# 9. `end=" "` keeps all numbers on the same line with spaces.
# 10. Approach: take N → check each number → test multiple of 2, 5, or 7
#     → print the number if any condition is true.
# 11. Concepts used: input(), for loop, range(), %, if condition, logical
#     `or`, and print().

n = int(input())

for i in range(2, n + 1):
    if i % 2 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
# Notes:
# 1. Problem: Print numbers from 1 to N that are multiples of 2 or 3.
# 2. I take N as input and store it in `n`.
# 3. I use a `for` loop to check every number from 1 to N.
# 4. `i % 2 == 0` checks whether `i` is a multiple of 2.
# 5. `i % 3 == 0` checks whether `i` is a multiple of 3.
# 6. I use `or` because satisfying either condition is enough.
# 7. If the condition is true, I print `i`.
# 8. `end=" "` keeps all numbers on the same line.
# 9. Approach: take N → check each number → test multiple of 2 or 3
#    → print the number if the condition is true.
# 10. Concepts used: input(), for loop, range(), %, if condition,
#     logical `or`, and print().

n = int(input())

for i in range (1, n + 1):
    if i % 2 == 0 or i % 3 == 0:
        print(i, end=" ")
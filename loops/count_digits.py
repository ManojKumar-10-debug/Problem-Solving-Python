# Notes:
# 1. Problem: Count the number of digits in a given number.
# 2. I take the number as input and store it in `num`.
# 3. I create `count = 0` to keep track of how many digits are present.
# 4. I use `while num > 0` because the number of digits is not fixed.
# 5. `count = count + 1` counts one digit in every loop iteration.
# 6. `num // 10` removes the last digit from `num`.
# 7. The loop continues until all digits are removed and `num` becomes 0.
# 8. Approach: count one digit → remove one digit → repeat until num is 0.
# 9. `print(count)` displays the total number of digits.
# 10. Concepts used: input(), while loop, counter variable, floor division,
#     and variable updating.

num = int(input())
count = 0

while num > 0:
    count = count + 1
    num //= 10

print(count)
# Notes:
# 1. Problem: Find the sum of all digits in a number.
# 2. `sum = 0` stores the total of the digits.
# 3. `while num > 0` continues until all digits are processed.
# 4. `num % 10` extracts the last digit.
# 5. `sum += digit` adds the extracted digit to the total.
# 6. `num //= 10` removes the last digit from the number.
# 7. The loop is used because the number of digits is not fixed.
# 8. We use `while` because the loop continues based on the condition
#    `num > 0`, not on a predetermined number of iterations.
# 9. Approach: extract last digit → add it to sum → remove last digit
#    → repeat until the number becomes 0.
# 10. `print(sum)` displays the final sum of the digits.

num = int(input())
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

print(sum)
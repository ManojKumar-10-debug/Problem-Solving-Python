# Notes:
# 1. Problem: Find the largest number among three given numbers.
# 2. I take three numbers as input and store them in `a`, `b`, and `c`.
# 3. First, I check whether `a` is greater than or equal to both `b` and `c`.
# 4. If true, I store `a` in `largest`.
# 5. Otherwise, I check whether `b` is greater than or equal to both `a` and `c`.
# 6. If true, I store `b` in `largest`.
# 7. If neither condition is true, `c` is the largest, so I store `c`.
# 8. I use the `largest` variable to store the final result instead of
#    printing inside every condition.
# 9. Finally, `print()` displays the value stored in `largest`.
# 10. Approach: compare each number with the other two → store the largest
#     value → print it.
# 11. Concepts used: input(), variables, comparison operators, and
#     if-elif-else.

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)
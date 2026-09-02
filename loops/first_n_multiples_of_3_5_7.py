# Notes:
# 1. Problem: Print the first N numbers that are multiples of 3, 5, or 7.
# 2. I take N as input and store it in `n`.
# 3. I use `count` to track how many valid numbers have been printed.
# 4. I start `i` from 3 because 3 is the first possible valid number.
# 5. I use `while count < n` because I need exactly N valid numbers,
#    but I don't know how far `i` must go to find them.
# 6. I check whether `i` is a multiple of 3, 5, or 7 using `%` and `or`.
# 7. When a valid number is found, I print it and increase `count` by 1.
# 8. `i += 1` checks the next number.
# 9. I did not use a `for` loop because the number of iterations is not
#    fixed; the loop must continue until N valid numbers are found.
# 10. Approach: start from 3 → check each number → print valid numbers
#     → count them → stop when N valid numbers are printed.
# 11. Concepts used: input(), while loop, counter variable, `%`, if condition,
#     logical `or`, and print().

n = int(input())
count = 0
i = 3
while count < n:
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
        count += 1
    i += 1
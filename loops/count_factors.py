# Notes:
# 1. Problem: Count the total number of factors of a given number.
# 2. `factors(num)` is a separate function that contains the factor-counting logic.
# 3. `count = 0` stores how many factors are found.
# 4. The `for` loop checks every number from 1 to `num`.
# 5. `num % i == 0` checks whether `i` divides `num` exactly.
# 6. If the remainder is 0, `i` is a factor, so `count` is increased.
# 7. `return count` sends the final factor count back to the caller.
# 8. `print(factors(n))` calls the function and prints its returned value.
# 9. I use a function because the factor-counting logic can be reused later.
# 10. Approach: take num → check possible factors → count valid factors
#     → return count → print the result.
# 11. Example 1: 12 → factors: 1, 2, 3, 4, 6, 12 → count = 6.
# 12. Example 2: 10 → factors: 1, 2, 5, 10 → count = 4.
# 13. Concepts used: function, parameter, return value, for loop,
#     range(), `%` modulus, if condition, counter, and function call.

def factors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    return count

n = int(input())
print(factors(n))
# Notes:
# 1. Problem: Find and print all factors of a given number.
# 2. `factors(n)` is a separate function that contains the factor logic.
# 3. I use a `for` loop from 1 to `n` to check every possible factor.
# 4. `n % i == 0` checks whether `i` divides `n` exactly.
# 5. If the remainder is 0, `i` is a factor, so I print it.
# 6. I use a function so the factor logic can be reused by calling
#    `factors()` whenever needed.
# 7. `factors(n)` passes the input value `n` into the function parameter.
# 8. Approach: start from 1 → check each number → if remainder is 0,
#    print it → continue until n.
# 9. Example 1: Factors of 12 → 1 2 3 4 6 12.
# 10. Example 2: Factors of 10 → 1 2 5 10.
# 11. Concepts used: function, parameter, function call, for loop,
#     range(), `%` modulus, if condition, and print().

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")


n = int(input())
factors(n)
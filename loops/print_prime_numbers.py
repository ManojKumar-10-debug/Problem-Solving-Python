# Notes:
# 1. Problem: Print all prime numbers from 2 to n.
# 2. `is_prime(n)` checks whether a number is prime.
# 3. The function returns `True` for prime and `False` for non-prime.
# 4. `n <= 1` → not prime, so return `False`.
#
# 5. The loop checks possible divisors starting from 2.
# 6. `n % i == 0` means n is exactly divisible by i, so n is not prime.
# 7. If a divisor is found, `return False` immediately.
# 8. If no divisor is found, `return True`.
#
# 9. `n ** 0.5` calculates the square root of n.
# 10. `0.5` means `1/2`, so `n ** 0.5 = √n`.
# 11. We check only up to `√n` because a factor greater than √n
#     always has a matching factor smaller than √n.
# 12. This reduces unnecessary iterations and makes prime checking faster.
# 13. `int(n ** 0.5) + 1` is used because `range()` excludes the ending value.
# 14. `n / 2` could also work, but it checks more numbers than necessary.
#
# 15. `for i in range(2, n + 1)` checks every number from 2 to n.
# 16. `is_prime(i)` checks whether the current number is prime.
# 17. If `is_prime(i)` returns `True`, that number is printed.
#
# 18. Example 1: n = 10 → prints 2, 3, 5, 7.
# 19. Example 2: n = 20 → prints 2, 3, 5, 7, 11, 13, 17, 19.
#
# 20. Concepts used: function, parameter, boolean, return, for loop,
#     range(), `%` modulus, `**` power, square root, and function calling.

def is_prime(n):
    if n <= 1:
        return False

    # n ** 0.5 means square root of n (because 0.5 = 1/2)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input())
for i in range(2, n + 1):
    if is_prime(i):
        print(i)
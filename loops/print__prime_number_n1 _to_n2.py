# Notes:
# 1. Problem: Print all prime numbers between n1 and n2.
# 2. `is_prime(n)` checks whether a number is prime.
# 3. The function returns `True` for prime and `False` for non-prime.
#
# 4. `n <= 1` → not prime, so return `False`.
# 5. The loop checks possible divisors starting from 2.
# 6. `n ** 0.5` calculates √n because 0.5 = 1/2.
# 7. We check only up to √n because checking beyond √n is unnecessary.
# 8. `int(n ** 0.5) + 1` is used because `range()` excludes the ending value.
# 9. `n % i == 0` means n is exactly divisible by i, so n is not prime.
# 10. If a divisor is found, `return False` immediately.
# 11. If no divisor is found, `return True`.
#
# 12. `n1` stores the starting number and `n2` stores the ending number.
# 13. `range(n1, n2 + 1)` checks every number from n1 through n2.
# 14. `is_prime(i)` checks each number in the range.
# 15. If it returns `True`, that number is printed.
#
# 16. Example 1: n1 = 10, n2 = 20 → 11 13 17 19.
# 17. Example 2: n1 = 2, n2 = 10 → 2 3 5 7.
#
# 18. Concepts used: function, parameter, boolean, return, for loop,
#     range(), modulus `%`, power `**`, square root, and function calling.

def is_prime(n):
    if n <= 1:
        return False

    # n ** 0.5 means square root of n (because 0.5 = 1/2)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


n1 = int(input())
n2 = int(input())
for i in range(n1, n2 + 1):
    if is_prime(i):
        print(i)
# Notes:
# 1. Problem: Print the first N prime numbers.
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
# 12. `n` represents how many prime numbers we need to print.
# 13. `count = 0` keeps track of how many prime numbers have been printed.
# 14. `i = 2` because 2 is the first prime number.
# 15. `while count < n` continues until N prime numbers are printed.
# 16. `is_prime(i)` checks whether the current value of `i` is prime.
# 17. If it returns `True`, `i` is printed and `count` is increased by 1.
# 18. `i += 1` moves to the next number to check.
#
# 19. We use `count < n` instead of `i <= n` because the requirement is
#     to find the first N prime numbers, not primes up to N.
# 20. Example 1: N = 5 → 2 3 5 7 11.
# 21. Example 2: N = 3 → 2 3 5.
#
# 22. Concepts used: function, parameter, boolean, return, while loop,
#     counter variable, `%` modulus, `**` power, square root,
#     condition, and function calling.

def is_prime(n):
    if n <= 1:
        return False

    # n ** 0.5 means square root of n (because 0.5 = 1/2)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input())
count = 0
i = 2
while count < n:
    if is_prime(i):
        print(i)
        count += 1

    i += 1
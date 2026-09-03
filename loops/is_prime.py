# Notes:
# 1. Problem: Check whether a given number is prime or not.
# 2. `is_prime(n)` is a function that returns `True` or `False`.
# 3. `n <= 1` → not prime, so return `False`.
# 4. The loop checks possible divisors from 2 up to the square root of n.
# 5. `n ** 0.5` gives the square root of n.
# 6. `n % i == 0` means n is exactly divisible by i, so it is not prime.
# 7. If a divisor is found, `return False` immediately.
# 8. If no divisor is found, `return True`.
# 9. `if is_prime(n):` calls the function and checks its returned boolean value.
# 10. Important: `if is_prime(n):` is correct. `if is_prime(n):` must include `()`
#     because the function needs to be called.
# 11. Example 1: n = 7 → no divisor found → `True` → prints "Yes".
# 12. Example 2: n = 12 → divisible by 2 → `False` → prints "No".
# 13. Concepts used: function, parameter, boolean, return, for loop,
#     range(), square root, modulus `%`, and function calling.

def is_prime(n):
    if n <= 1:
        return False

    # n ** 0.5 means square root of n (because 0.5 = 1/2)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input())

if is_prime(n):
    print("Yes")
else:
    print("No")
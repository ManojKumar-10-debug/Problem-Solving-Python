# Notes:
# 1. Problem: Print the first N natural numbers, excluding 0.
# 2. I created `print_first_N_natural_numbers()` to keep the printing logic
#    separate and make the logic reusable.
# 3. `num` stores the N value taken from the user.
# 4. I use a `for` loop with `range(1, num + 1)` to generate numbers from 1
#    up to N.
# 5. I start the range from 1 because 0 must be excluded.
# 6. `num + 1` is used because the ending value of `range()` is excluded.
# 7. `print(i, end=" ")` prints each number on the same line with a space.
# 8. Finally, I call the function and pass `num` to it.
# 9. Approach: take N → start from 1 → loop until N → print each number.
# 10. Concepts used: function, parameter, for loop, range(), and print().

def print_first_N_natural_numbers(num):
    for i in range(1, num + 1):
        print(i, end=" ")


num = int(input())

print_first_N_natural_numbers(num)


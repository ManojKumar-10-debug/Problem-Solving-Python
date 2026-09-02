# Notes:
# 1. Function checks whether an ASCII value represents uppercase, lowercase,
#    numerical, or special character.
#
# 2. 65–90  → Uppercase letters (A–Z).
#
# 3. 97–122 → Lowercase letters (a–z).
#
# 4. 48–57  → Numerical characters (0–9).
#
# 5. Any value outside these ranges → Special Character.
#
# 6. Function keeps the checking logic separate from input/output,
#    so the function can be reused later.
#
# 7. The function is called with `num` after taking input from the user.
#
# 8. Approach: Compare the input ASCII value with the known ASCII ranges
#    instead of converting the number into a character.

def is_uppercase_or_lowercase(num):
    if 65 <= num <= 90:
        print("Uppercase")
    elif 97 <= num <= 122:
        print("Lowercase")
    elif 48 <= num <= 57:
        print("Numerical")
    else:
        print("Special Characters")


num = int(input())
is_uppercase_or_lowercase(num)
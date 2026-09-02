# Notes:
# 1. input() → takes input as a string.
# 2. [0] → gets the first character from the input.
# 3. ord() → converts the character into its numeric ASCII/Unicode value.
# 4. Store the numeric value in ascii_value so it can be reused later.
# 5. print() → displays the numeric value.
# 6. Approach: input → first character → ord() → store value → print.

ascii_value = ord(input()[0])
print(ascii_value)
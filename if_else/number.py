# Notes:
# 1. num stores the input number.
# 2. num % 10 gives the last digit of the number.
# 3. If num % 10 == 0, the number ends with 0.
# 4. The ternary expression stores "Yes" or "No" in res.
# 5. Using res lets us reuse the result without writing the condition again.
# 6. print(res) displays the stored result.
# Number ends with zero or not
num = int(input())

res = "Yes" if num % 10 == 0 else "No"
print(res)
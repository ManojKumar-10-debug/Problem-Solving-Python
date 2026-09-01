
# 1. Read the number as input.
# 2. Check whether the number is between 10 and 99.
# 3. Used Python's chained comparison to check both limits in one condition.
# 4. Store "Yes" if the condition is true, otherwise store "No".
# 5. Print the stored result.

import if_else

num = int(input())

res = "Yes" if 9 < num < 100 else "No"

print(res)
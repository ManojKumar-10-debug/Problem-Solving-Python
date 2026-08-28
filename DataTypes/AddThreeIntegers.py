import DataTypes

# 1. Take three integer inputs using input().
# 2. Store the inputs in first_number, second_number, and third_number.
# 3. Pass the three numbers to add_three_integers().
# 4. The function adds the three numbers and returns the result.
# 5. Store the returned result in res.
# 6. Print res using print().
# 7. return sends the result/value back to where the function was called.

def add_three_integers(first_number, second_number, third_number):
    return first_number + second_number + third_number



first_number = int(input())
second_number = int(input())
third_number = int(input())

res = add_three_integers(first_number, second_number, third_number)
print(res)




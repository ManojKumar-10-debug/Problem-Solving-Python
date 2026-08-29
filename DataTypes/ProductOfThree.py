# Notes:
# 1. Take three integer inputs and find their product.
# 2. Store the inputs in firstNumber, secondNumber, and thirdNumber.
# 3. Pass the three values to product_of_three() function.
# 4. The function multiplies them and returns the result.
# 5. Store the returned value in res and print it.
#
# Concept: Function calling, arguments, return value.

def product_of_three(firstNumber, secondNumber, thirdNumber):
    return firstNumber * secondNumber * thirdNumber


first_number = int(input())
second_number = int(input())
third_number = int(input())

res = product_of_three(first_number, second_number, third_number)
print(res)
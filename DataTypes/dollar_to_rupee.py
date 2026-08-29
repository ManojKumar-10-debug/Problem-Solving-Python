# Notes:
# 1. Take dollar amount and exchange rate as inputs.
# 2. Store them in dollar and exchange_rate.
# 3. Pass both values to dollar_to_rupee() function.
# 4. The function multiplies dollar by exchange_rate and returns the result.
# 5. Store the returned value in inr and print it with 4 decimal places.
#
# Concept: Function calling, arguments, return value, formatted output.

def dollar_to_rupee(dollar, exchange_rate):
    return dollar * exchange_rate


dollar = int(input())
exchange_rate = float(input())

inr = dollar_to_rupee(dollar, exchange_rate)

print(f"{inr:.4f}")
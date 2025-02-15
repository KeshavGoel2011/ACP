#to calculate exponential result of a number
base = int(input("Enter a number to act as the base: "))
exponent = int(input("Enter a number to act as the exponent: "))
result = 1

for i in range(exponent):
    result = result*base

print(f"{base} raised to the power of {exponent} is {result}")
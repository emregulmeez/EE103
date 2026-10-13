x = int(input("Enter a number to calculate its factorial: "))
number = x
factorial = 1

while x > 0:
    factorial = factorial * x
    x = x - 1

print(f"The factorial of {number} is {factorial}")
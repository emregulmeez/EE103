x=int(input("Enter a number to calculate its factorial: "))
factorial=1
for i in range (1,x+1):
    factorial=factorial*i
print(f"The factorial of {x} is {factorial}")


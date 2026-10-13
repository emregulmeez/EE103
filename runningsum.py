x=int(input("Enter a number:"))
runningsum=0
for i in range(0,x+1):
    runningsum=runningsum+i
print(f"The running sum of {x} is {runningsum}")
runningsum_gauss=(x*(x+1))/2
print(f"The running sum of {x} using Gauss formula is {runningsum_gauss}")  


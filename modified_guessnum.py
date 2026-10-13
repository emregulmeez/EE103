from secretnumber import secretnum
guess=float(input("What is your guess?\n"))
while guess<secretnum:
    print("Your guess is too low")
    guess=float(input("What is your guess?\n"))
while guess>secretnum:
    print("Your guess is too high")
    guess=float(input("What is your guess?\n"))
while guess==secretnum:
    print("You guessed it!")
    break   

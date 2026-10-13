from secretnumber import secretnum
guess=float(input("What is your guess?\n"))
if guess<secretnum:
    print("Your guess is too low.")
elif guess>secretnum:
    print("Your guess is too high.")
else:
    print("You guessed it!")
    
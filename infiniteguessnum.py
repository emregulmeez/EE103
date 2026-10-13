from secretnumber import secretnum
attempts=0
guessed=False
while attempts<5:
    guess=float(input("What is your guess?\n"))
    attempts+=1
    if guess<secretnum:
        print("Your guess is too low.")
    elif guess>secretnum:
        print("Your guess is too high.")    
    else:
        print("You guessed it!")
        guessed=True
        break
if not guessed:
     while True:
        print("Oh nooooooooo")


   
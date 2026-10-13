x=float(input("What x to find the cube root of?\n"))
guess=float(input("What guess to start with?\n"))
print(f"Current estimated cube:{guess**3}")
nextguess=guess-((guess**3-x)/(3*guess**2))         
print(f"Next guess is{nextguess}")


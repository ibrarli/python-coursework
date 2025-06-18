secret = 7
guess = int(input("Guess the number: "))

while guess != secret:
    print("Wrong! Try again.")
    guess = int(input("Guess the number: "))

print("Correct! You guessed it.")

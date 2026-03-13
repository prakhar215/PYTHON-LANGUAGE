number=43
while True:
    guess=int(input("Guess number:"))
    if guess < number:
        print("Guessed number is samller")
    elif guess > number:
        print("Guessed number is higher")
    else:
        print("CONGRATS! you guessed the number")
        break
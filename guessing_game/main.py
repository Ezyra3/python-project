import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)  # includes top_of_range
guess = None

while guess != random_number:
    guess = input(f"Guess a number between 0 and {top_of_range}: ")
    if guess.isdigit():
        guess = int(guess)
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
    else:
        print("Please type a valid number.")

print(f"Congrats! You guessed it: {random_number}")

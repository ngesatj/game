import random

number = random.randint(1, 100)
attempts = 0

print("Guess thee numberrr betweennn 1 and 100!")

while True:
    guess = int(input("Enter yourr guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Tryyy again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break

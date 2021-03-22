import random

highest = 10
answer = random.randint(1, highest)

print("Please guess the number between 1 to {}: " .format(highest))
guessed_number = int(input())

while guessed_number != answer:
    if guessed_number < answer:
        print("Incorrect answer, guess higher")
    else:
        print("Incorrect answer, guess lower")

    guessed_number = int(input())
    if guessed_number == answer:
        print("well-done, you got it right")

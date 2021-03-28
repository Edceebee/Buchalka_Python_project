import random

highest = 10
answer = random.randint(1, highest)
print(f'Please guess the number between 1 to {highest}: ')

guessed_number = int(input())


while guessed_number != answer:

    guessed_number = int(input())

    if guessed_number < answer:
        print("Incorrect answer, guess higher")
    else:
        print("Incorrect answer, guess lower")

    if guessed_number == answer:
        print("well-done, you got it right")

    continue
    # print()

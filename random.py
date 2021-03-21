import random

highest = 10
answer = random.randint(1, highest)

print("Please guess the number between 1 to {}" .format(highest))
guessed_number = int(input())

if guessed_number != answer:
    if guessed_number < answer:
        print("Answer is greater than {}: " .format(guessed_number))
    else:
        print("Answer is lesser than {}: " .format(guessed_number))

    guessed_number = int(input())
    if guessed_number == answer:
        print("Well-done, you guessed right")
    else:
        print("Sorry, incorrect answer")

# want to use while loop to continue to take input
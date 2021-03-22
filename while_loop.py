import random

highest = 10
answer = random.randint(1, highest)

print("Please guess the number between 1 to {}: ".format(highest))
guessed_number = int(input())

while answer != guessed_number:
    print("Please guess the number between 1 to {}: ".format(highest))
    guessed_number = int(input())

    if guessed_number > answer:
        print("number is less than {}".format(guessed_number))
    else:
        print("number is greater than {}".format(guessed_number))

    if guessed_number == answer:
        print("Well-done, you got it right")
    else:
        print("Sorry, try again.")
guessed_number += 1

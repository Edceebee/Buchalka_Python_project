fruits = {"orange": "good for vitamins", "apple": "red and green", "pineapple": "i don't like it",
          "watermelon": "chewable seeds"}
print(fruits)


while True:
    snack = input("Enter name of fruit\n")
    if snack in fruits:
        description = fruits.get(snack)
        print(description)

    else:
        print("we don't have " + snack)

    if snack == "quit":
        print("the end")
        break


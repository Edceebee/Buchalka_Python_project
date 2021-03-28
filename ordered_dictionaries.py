fruits = {"orange": "good for vitamins", "apple": "red and green", "pineapple": "i don't like it",
          "watermelon": "chewable seeds"}
print(fruits)

# ordered_fruits = list(fruits.keys())
# ordered_fruits.sort()
# for i in ordered_fruits:
#     print(i + ' is ' + fruits[i])

# OR

for i in sorted(fruits.keys()):
    print(i + " - " + fruits[i])

# for numbers in range(1, 5):
#     # print ("No %d squared is %4d and cubed is %4d" % (numbers, numbers **2, numbers**3))
#     #  print()
#     print("no {0} squared is {1:4} and cubed is {2:4}".format(numbers, numbers ** 2, numbers ** 3))
#
# name = input("Enter your name")
# print("My name is: " + name)

name = input("please enter your name: ")
age = int(input("How old are you, " + name + ": "))
# print(age)
if age >= 18:
    print("You are eligible to vote")
else:
    print("Sorry, you are not eligible to vote, come back in " + str(18 - age ) + "years")
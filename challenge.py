# create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order
#
# Yo can either enter a text from the keyboard or
# initialize a string variable with the string

#
# text = "My name is Star Boy"
# vowels = ('a', 'e', 'i', 'o', 'u')
#
# new_text = set(text).difference(vowels)
# print(new_text)
#
# final_text = sorted(new_text)
# print(final_text)


text = input("enter name\n")
vowels = ('a', 'e', 'i', 'o', 'u')
for x in text:
    if x in vowels:
        text = text.replace(x, "_")

    # Print string without vowels
print(text)

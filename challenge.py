# create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order
#
# Yo can either enter a text from the keyboard or
# initialize a string variable with the string


text = "My name is Star Boy"
vowels = ('a', 'e', 'i', 'o', 'u')

new_text = set(text).difference(vowels)
print(new_text)

final_text = sorted(new_text)
print(final_text)

# # for letters in text:
# for l in text:
#     if vowels in text:
#         text = text.replace(l, "")
#
# print(text)

# Write your own version of the find command.
# The user will input a word, you will then ask them to input a string to search for. Display
# the first location of that string.
# Bonus: Display all the locations of those strings.


word = input("Please enter a word: ")
search = input("Please enter a string to search for: ")
for i in range(len(word)):
    if word[i:i+len(search)] == search:
        print(i)
        break

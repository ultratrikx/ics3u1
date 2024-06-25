# Get the input from the user
sentence = input("Please enter a sentence: ")
spaceLocation = "Spaces located at: "
newSentence = ""
evenSentence = "Even string is: "
oddSentence = "Odd string is: "
# Iterate over the indices of the sentence
for index in range(len(sentence)):
    print("%s(%s)" % (sentence[index], str(index)), end=" ")

    if sentence[index] == " ":
        spaceLocation += str(index) + " "
        newSentence += "mouse"
    else:
        newSentence += sentence[index]

for index in range(len(newSentence)):
    if index % 2 == 0 and newSentence[index] != " ":
        evenSentence += newSentence[index]
    elif index % 2 == 1 and newSentence[index] != " ":
        oddSentence += newSentence[index]

print("\n", spaceLocation, "\n", newSentence, "\n", evenSentence, "\n", oddSentence, "\n")
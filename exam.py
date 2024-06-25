# Level 2
userString = input("Please enter a string: ")

# wordsList = userString.split()
# print(wordsList)

# Level 3
# wordsList = userString.split()
#
# def remove_deuplicates(list):
#     newList = []
#     newListLower = []
#     for i in list:
#         if i.lower() not in newListLower:
#             newList.append(i)
#             newListLower.append(i.lower())
#     return newList
#
# uniqueWordsList = remove_duplicates(wordsList)
#
#
# print(wordsList)
# print(uniqueWordsList)

# Level 4
wordsList = userString.split()
lowerWordsList = userString.lower().split()


def remove_deuplicates(list):
    newList = []
    newListLower = []
    for i in list:
        if i.lower() not in newListLower:
            newList.append(i)
            newListLower.append(i.lower())
    return newList, newListLower


uniqueWordsList, lowerUniqueWordsList = remove_deuplicates(wordsList)

uniqueWordsCount = []

for uniqueWord in lowerUniqueWordsList:
    count = 0
    for word in lowerWordsList:
        if word == uniqueWord:
            count += 1
    uniqueWordsCount.append(count)

print(wordsList)
print(uniqueWordsList)
print(uniqueWordsCount)

# Level 4+
secondString = input("Please enter a second string: ")
secondStringWords = secondString.split()

secondStringUniqueWords, _ = remove_deuplicates(secondStringWords)

sameWordsList = []
for firstWord in uniqueWordsList:
    for secondWord in secondStringUniqueWords:
        if firstWord == secondWord:
            sameWordsList.append(firstWord)

maxLen = 0
longestWord = ""
alsolongestWord = ""
for word in sameWordsList:
    if len(word) > maxLen:
        longestWord = word
        maxLen = len(word)
        alsolongestWord = ""
    if len(word) == maxLen:
        alsolongestWord = word

if longestWord != alsolongestWord:
    print("The two longest common substrings are: \"%s\" and \"%s\"" % (longestWord, alsolongestWord))
else:
    print("The longest common substring is \"%s\"" % longestWord)

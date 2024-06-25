# count = 1 # only used to display 10 characters on a line
# for i in range(ord('A'), ord('Z') + 1):  # characters can't count, but i can count from 65 to 90
#     print("%s (%i)" %(chr(i), i), end = " ")  # remember end =
#     if count % 10 == 0: # for display purposes
#         print()
#     count += 1
#

def yUpper(string):
    output = ""
    for letter in string:
        if ord(letter) in range(ord('a'), ord('z') + 1): # if upper case
            output += chr(ord(letter) - 32)
        elif ord(letter) in range(ord('A'), ord('Z') + 1):
            output += letter
        else:
            output += letter
    return output

def ySwap(string):
    output = ""
    for letter in string:
        if ord(letter) in range(ord('a'), ord('z') + 1): # if upper case
            output += chr(ord(letter) - 32)
        elif ord(letter) in range(ord('A'), ord('Z') + 1):
            output += chr(ord(letter) + 32)
        else:
            output += letter
    return output

testString = "      yOuR sTrInG hErE"
print(yUpper(testString)) # should print
print(ySwap(testString)) # should print

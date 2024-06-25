# Rohanth Marem
# Unit 2 Programming Test Part 2
# ICS3U1 Ms. Bokhari


nameAndNumber = input("Please enter a digit and your full name: ")

digit = int(nameAndNumber[0])

nameNoSpace = nameAndNumber[1:].replace(" ", "")

nameSpace = nameAndNumber[2:]

nameLength = len(nameNoSpace)

spacePlace = nameSpace.find(" ")

lastInitalFirstName = nameSpace[spacePlace+1:spacePlace+2] + nameSpace[:spacePlace]

print("The full name has %i characters." % nameLength)
print(nameNoSpace*digit)
print(nameNoSpace.swapcase()*digit)
print(lastInitalFirstName*nameLength)
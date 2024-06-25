def seperate_colour_number(input, colour):
    if input.find(colour) > -1:
        index = input.find(colour)
        colour = input[index:len(colour)]
        number = int(input.replace(colour, ""))
        global colourChoice
        global numberChoice
        global numberEven
        global colourEven
        global choice
        colourChoice = colour
        numberChoice = number
        colourEven = True if len(colourChoice) % 2 == 0 else False
        numberEven = True if number % 2 == 0 else False
import random

COLOUR1 = "RED"
COLOUR2 = "GREEN"
COLOUR3 = "BLUE"
COLOUR4 = "YELLOW"

MESSAGE1 = "You are beautiful!"
MESSAGE2 = "I wish you have a wonderful day."
MESSAGE3 = "I think you like mangos"
MESSAGE4 = "You are a good person!"
MESSAGE5 = "Funny person, you are."
MESSAGE6 = "I see your smile and my soul is happy."
MESSAGE7 = "In all of time, the world has never been blessed by a person as wonderful as you."
MESSAGE8 = "Hee haw"

def check_colour(input, colour):
    if input.find(colour) == -1:
        return False
    else:
        return True

def check_all_colours(input):
    if check_colour(input, COLOUR1) == True:
        return COLOUR1
    elif check_colour(input, COLOUR2) == True:
        return COLOUR2
    elif check_colour(input, COLOUR3) == True:
        return COLOUR3
    elif check_colour(input, COLOUR4) == True:
        return COLOUR4
    else:
        return

def random_message(number):
    randomizer = random.randint(1, 2)
    if number == 1 or number == 2:
        if randomizer == 1:
            return MESSAGE1
        else:
            return MESSAGE2
    elif number == 3 or number == 4:
        if randomizer == 1:
            return MESSAGE3
        else:
                return MESSAGE4
    elif number == 5 or number == 6:
        if randomizer == 1:
            return MESSAGE5
        else:
             return MESSAGE6
    elif number == 7 or number == 8:
        if randomizer == 1:
            return MESSAGE7
        else:
            return MESSAGE8
    
def main():
    global userChoice
    colour = check_all_colours(userChoice)

    if colour == None:
        userChoice = input("Invalid input. Please enter a valid colour from the choices (%s, %s, %s, %s) and a number: " % (COLOUR1, COLOUR2, COLOUR3, COLOUR4)).replace(" ", "").replace(",","").upper()
        return main()

    number = userChoice.replace(colour, "")

    if len(number) == 0:
        userChoice = input("You didn't enter a number. Please enter a number between 1 and 8: ")
        return main()
    elif number.isdigit() == False:
        userChoice = input("Please enter ONE valid colour from the choices (%s, %s, %s, %s) and a number: " % (COLOUR1, COLOUR2, COLOUR3, COLOUR4)).replace(" ", "").replace(",","").upper()
        return main()
    else:
        number = int(number)

    if number > 8 or number < 1:
        userChoice = input("Pick a colour and a number between 1 and 8: ").replace(" ", "").replace(",","").upper()
        return main()
    elif len(colour) % 2 == 0 and number % 2 != 0:
        userChoice = input("Pick a colour and a number from 2, 4, 6 and 8: ").replace(" ", "").replace(",","").upper()
        return main()
    elif len(colour) % 2 != 0 and number % 2 == 0:
        userChoice = input("Pick a colour and a number from 1, 3, 5 and 7: ").replace(" ", "").replace(",","").upper()
        return main()
    
    # print("You chose the colour %s and the number %s." % (colour, number))
    return print("\n", random_message(number))
    

print("Welcome to the Fortune Teller Game!\nAvailable colours are %s, %s, %s and %s.\n" % (COLOUR1, COLOUR2, COLOUR3, COLOUR4))
userChoice = input("Pick a colour and a number: ").replace(" ", "").replace(",","").upper()
main()

    
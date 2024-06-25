"""
Name: Rohanth Marem
Date: 2024-04-04
Course: ICS3U1-02
Description:
This is a fortune-teller program which takes a user input of a colour and a number and returns a random happy message.
It has error handling to deal with incorrect user inputs and gives the user a second chance to correct their input.
"""

# Import the random module for message randomization
import random

# Define the colour constants, change as you wish **MUST BE IN ALL CAPS**
COLOUR1 = "RED"
COLOUR2 = "GREEN"
COLOUR3 = "BLUE"
COLOUR4 = "YELLOW"

# Define the message constants, change as you wish
MESSAGE1 = "You are beautiful!"
MESSAGE2 = "I wish you have a wonderful day."
MESSAGE3 = "I think you like mangoes"
MESSAGE4 = "You are a good person!"
MESSAGE5 = "Funny person, you are."
MESSAGE6 = "I see your smile and my soul is happy."
MESSAGE7 = "In all of time, the world has never been blessed by a person as wonderful as you."
MESSAGE8 = "Hee haw, you like living a wild life!"

# Define the number lower limit, change as you wish. **MUST BE INTEGER**
NUMBER_MIN_LIMIT = 256  # Minimum number limit for the user input


# Function to standardize the user input
def standardize_input(user_input):
    return user_input.replace(" ", "").replace(",", "").upper()  # Remove spaces and commas and convert to uppercase


# Function to check if a given colour is in the user input.
def check_colour(user_input, colour):
    if user_input.find(colour) == -1:  # The colour is NOT in the user input
        return False
    else:
        return True


# Function to check if the specified colours are in the user input using the check_colour function on each colour
def check_all_colours(user_input):
    if check_colour(user_input, COLOUR1):
        return COLOUR1
    elif check_colour(user_input, COLOUR2):
        return COLOUR2
    elif check_colour(user_input, COLOUR3):
        return COLOUR3
    elif check_colour(user_input, COLOUR4):
        return COLOUR4
    else:
        return  # None value if no colour is found, to be caught in the find_number function


# Function to check for errors in the user input and return the number if no errors are found
def find_number(user_input, colour):
    if colour is None:  # No colour found in the user input, based on output of check_all_colours function
        print("Invalid colour. Available choices are (%s, %s, %s, %s)."
              % (COLOUR1, COLOUR2, COLOUR3, COLOUR4))
        return

    num = user_input.replace(colour, "", 1)  # Isolating for the number (or any garbage characters)

    if len(num) == 0:  # No number found in the user input
        print("A number was not entered. Enter a number between 1 and 8.")
        return
    elif not num.isdigit():  # "Number" is not a digit or more than one number was entered
        print("More than one valid colour was entered or there was a typo. Available choices are (%s, %s, %s, %s)."
              % (COLOUR1, COLOUR2, COLOUR3, COLOUR4))
        return
    else:
        num = int(num)
        if num > (NUMBER_MIN_LIMIT + 7) or num < NUMBER_MIN_LIMIT:  # Number is not between 1 and 8
            print("The number entered is not between %s and %s." % (NUMBER_MIN_LIMIT, NUMBER_MIN_LIMIT + 7))
            return
    return num  # Return the number if no errors are found


# Function to check if the number and colour length are even or odd and give the user another chance to correct it
def number_error(colour_input, number_input):
    global userChoice
    # Check if the number is even and the number of characters in a colour is even or vice versa and give second chance
    if len(colour_input) % 2 == 0 and number_input % 2 != 0:
        # Check if the minimum number limit is even or odd to determine the order of the numbers in the prompt
        if NUMBER_MIN_LIMIT % 2 == 0:
            userChoice = standardize_input(input("Pick a colour and a number from %s, %s, %s and %s: " %
                                                 (NUMBER_MIN_LIMIT, NUMBER_MIN_LIMIT + 2, NUMBER_MIN_LIMIT + 4,
                                                  NUMBER_MIN_LIMIT + 6)))
        else:
            userChoice = standardize_input(input("Pick a colour and a number from %s, %s, %s and %s: " %
                                                 (NUMBER_MIN_LIMIT + 1, NUMBER_MIN_LIMIT + 3, NUMBER_MIN_LIMIT + 5,
                                                  NUMBER_MIN_LIMIT + 7)))
        number_input = find_number(userChoice, colour_input)  # Check for errors and get the number in the new input
        return number_input
    elif len(colour_input) % 2 != 0 and number_input % 2 == 0:
        # Same check being done here but with the opposite conditions
        if NUMBER_MIN_LIMIT % 2 == 0:
            userChoice = standardize_input(input("Pick a colour and a number from %s, %s, %s and %s: " %
                                                 (NUMBER_MIN_LIMIT + 1, NUMBER_MIN_LIMIT + 3, NUMBER_MIN_LIMIT + 5,
                                                  NUMBER_MIN_LIMIT + 7)))
        else:
            userChoice = standardize_input(input("Pick a colour and a number from %s, %s, %s and %s: " %
                                                 (NUMBER_MIN_LIMIT, NUMBER_MIN_LIMIT + 2, NUMBER_MIN_LIMIT + 4,
                                                  NUMBER_MIN_LIMIT + 6)))
        number_input = find_number(userChoice, colour_input)  # Check for errors and get the number in the new
        return number_input
    else:
        return number_input  # Return the number if no errors are found


# Function to return a random message based on the number
def random_message(number):
    if number == NUMBER_MIN_LIMIT or number == NUMBER_MIN_LIMIT + 1:
        return random.choice([MESSAGE1, MESSAGE2])
    elif number == NUMBER_MIN_LIMIT + 2 or number == NUMBER_MIN_LIMIT + 3:
        return random.choice([MESSAGE3, MESSAGE4])
    elif number == NUMBER_MIN_LIMIT + 4 or number == NUMBER_MIN_LIMIT + 5:
        return random.choice([MESSAGE5, MESSAGE6])
    elif number == NUMBER_MIN_LIMIT + 6 or number == NUMBER_MIN_LIMIT + 7:
        return random.choice([MESSAGE7, MESSAGE8])


# Main function to run the game
def main():
    global userChoice
    print("Welcome to the Fortune Teller Game!\nAvailable colours are %s, %s, %s and %s.\n"
          % (COLOUR1, COLOUR2, COLOUR3, COLOUR4))  # Print the welcome message

    userChoice = standardize_input(input("Pick a colour and a number: "))  # Standardize the user input
    userColour = check_all_colours(userChoice)  # Isolate for the colour
    userNumber = find_number(userChoice, userColour)  # Check for errors and isolate the number

    # Gives user a second chance to correct their input based on the error message
    if userNumber is None:
        userChoice = standardize_input(input("Pick a colour and a number: "))
        userColour = check_all_colours(userChoice)
        userNumber = find_number(userChoice, userColour)
        if userNumber is None:  # if user enters an incorrect input again, the program will quit
            print("You have entered an incorrect input twice. Please restart the program.")
            return

    # Check for the number error (number and colour length are not matching as even or odd)
    userNumber = number_error(userColour, userNumber)

    return print("\n" + random_message(userNumber))  # Print the random message based on the number


userChoice = ""
# Call the main function to start the game
main()

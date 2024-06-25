# Write a program that asks the user to input a single digit.  Your program should then 
# output that digit in words.  For example, 9 is output as nine.

number = int(input("Enter a single digit: "))

def toonumber(number):
    if number == 0:
        return "zero"
    elif number == 1:
        return "one"
    elif number == 2:
        return "two"
    elif number == 3:
        return "three"
    elif number == 4:
        return "four"
    elif number == 5:
        return "five"
    elif number == 6:
        return "six"
    elif number == 7:
        return "seven"
    elif number == 8:
        return "eight"
    elif number == 9:
        return "nine"
    else:
        return "Invalid input"
    
print(toonumber(number))
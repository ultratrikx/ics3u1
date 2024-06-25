# Rohanth Marem
# Date: 26/02/2024
# ICS3U1
# Practice Assessment for Unit 2.5

# Change the values of the height and the base
height = float(input("Enter the height of the triangle: "))  # in cm
base = float(input("Enter the base of the triangle: "))  # in cm

# Calculate the new area of the triangle
area = base * height / 2

# Display the new area of the triangle to 1 decimal place
print("The area of a triangle with height of %.1f cm and base %.1f cm has an area of %.1f cm^2." % (height, base, area))
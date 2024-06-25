# Get the coordinates for two points from the user and compute the distance between the two points.  Output your answer rounded to two decimal places.

import math

# Get the coordinates for the first point
x1 = float(input("Enter the x-coordinate for the first point: "))
y1 = float(input("Enter the y-coordinate for the first point: "))

# Get the coordinates for the second point
x2 = float(input("Enter the x-coordinate for the second point: "))
y2 = float(input("Enter the y-coordinate for the second point: "))

# Compute the distance between the two points
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output the answer rounded to two decimal places
print("The distance between the two points is: %.2f"% distance)
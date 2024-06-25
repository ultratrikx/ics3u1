# Write a program that asks the user to enter five test marks.  If the test was out of 60, display the average for each test as a percentage (to one decimal place) and find the average of all the tests.

# For example:	

# Mark	        Percent
# 55		 91.7
# 41		 68.3
# 17		 28.3
# 35		 58.3
# 60	           100.0
	
# The average for the test is: 69.3%


# Note: Mark is left justified and percent is right justified.
# #

# Initialize the total sum of marks
total = 0

# Ask the user to enter five test marks
i = 1
marksList = []
percentList = []

while i <= 5:
    mark = float(input(f"Enter mark for test {i}: "))
    marksList.append(mark)
    percent = (mark / 60) * 100
    total += percent
    percentList.append(percent)
    i += 1

print("Mark\tPercent\n---------------\n%-3i %11.1f\n%-3i %11.1f\n%-3i %11.1f\n%-3i %11.1f\n%-3i %11.1f" % 
    (marksList[0], percentList[0], marksList[1], percentList[1], marksList[2], percentList[2], marksList[3], percentList[3], marksList[4], percentList[4]))

# Calculate the average of all the tests
average = total / 5

# Display the average for all the tests
print(f"\nThe average for the test is: {average:.1f}%")
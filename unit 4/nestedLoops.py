'''
Generate the following pyramid of digits:
      1 (6 spaces)
     232 (5 spaces)
    34543 (4 spaces)
   4567654 (3 spaces)
  567898765 (2 spaces)
 67890109876 (1 space)
7890123210987 (0 spaces)

'''

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1): # i corresponds to the row number and the first number of the row
    # Print leading spaces
    for j in range(1, rows - i + 1):
        print(" ", end="")
    # Print the first half of the numbers
    for j in range(i, 2 * i):
        print(j % 10, end="")
    # Print the second half of the numbers
    for j in range(2 * i - 2, i - 1, -1):
        print(j % 10, end="")
    print()
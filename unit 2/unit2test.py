# Rohanth Marem
# ICS3U1
# Ms. Bokhari
# Unit 2 Evaluation 1

#level 4+
bookPrice = 15.00

readerName1 = input("Please enter the first reader's name: ")
booksPurchased1 = int(input("Please enter the number of books for %s: " % readerName1))
readerName2 = input("Please enter the second reader's name: ")
booksPurchased2 = int(input("Please enter the number of books for %s: " % readerName2))
readerName3 = input("Please enter the third reader's name: ")
booksPurchased3 = int(input("Please enter the number of books for %s: " % readerName3))

print("%-10s %7s %10s" % ("Reader", "Books", "Cost"))
print("%-10s %7i %10.2f" % (readerName1, booksPurchased1, booksPurchased1*bookPrice))
print("%-10s %7i %10.2f" % (readerName2, booksPurchased2, booksPurchased2*bookPrice))
print("%-10s %7i %10.2f" % (readerName3, booksPurchased3, booksPurchased3*bookPrice))
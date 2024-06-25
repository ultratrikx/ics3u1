# Write a simple cash register program that asks for the product name and cost for three
# products. The program should then calculate HST (13%) on the product and add the tax to
# the total price. An example of the output is as follows:


# WOSS Gift Shop Receipt
# -------------------------------
# glove                    12.89
# toque                    18.99
# scarf                     20.00
# -------------------------------
# HST (13%)            6.74
# -------------------------------
# TOTAL                58.62
# Note: Product Name is left justified and no more than 10 characters (do not need to check, just won’t be)
# Cost, HST and Total values are all right justified.


# Define the HST rate
HST_RATE = 0.13

# Ask for the product name and cost for three products
product1 = input("Enter the name of the first product: ")
cost1 = float(input("Enter the cost of the first product: "))
product2 = input("Enter the name of the second product: ")
cost2 = float(input("Enter the cost of the second product: "))
product3 = input("Enter the name of the third product: ")
cost3 = float(input("Enter the cost of the third product: "))

# Calculate the total cost and HST
total_cost = cost1 + cost2 + cost3
HST = total_cost * HST_RATE
total = total_cost + HST

# Print the receipt
print("WOSS Gift Shop Receipt")
print("-------------------------------")
print("%-10s %20.2f" % (product1, cost1))
print("%-10s %20.2f" % (product2, cost2))
print("%-10s %20.2f" % (product3, cost3))
print("-------------------------------")
print("HST (13%%) %21.2f" % HST)
print("-------------------------------")
print("TOTAL %25.2f" % total)
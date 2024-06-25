# You are to write a program that does the following:
# Real Estate agents make, on average, 2.5% commission on the sale of a house.

# Level 2:

# Display the following table of information:

# Agent			Price		Commission
# Smith			875000		21875.00
# Jones			1125000		28125.00
# Khan			520000		13000.00

# Level 3:
# You are to ask the user to input three house sales, each sale with the following information:
# Selling Agent Last Name (no more than 20 letters)
# Sale Price of Home (less than 10 million, no decimal places)

# For Example:
# Please enter the first agent:	Smith
# Please enter the sale price:	875000
# Please enter the second agent:  Jones
# Please enter the sale price:	1125000
# Please enter the third agent:	Khan
# Please enter the sale price:	520000

# Level 4:
# Continue from Level 3:
# Display in a table form all of the information with headings of Agent, Price and Commission.
# Information is expected to be formatted!!!!  Names of agents are left justified.  Price and commission are right justified.  

# Output should look as follows:
# Agent		    Price	  Commission
# Smith		  875000		21875.00
# Jones		 1125000        28125.00
# Khan		  520000		13000.00

# Level 4+
# Modify the input to include the agent’s name.
# For Example:
# Please enter the first agent:	Smith
# Please enter the sale price for agent Smith:	875000


agent1 = input("Please enter the first agent: ")
price1 = int(input("Please enter the sale price for agent " + agent1 + ": "))
agent2 = input("Please enter the second agent: ")
price2 = int(input("Please enter the sale price for agent " + agent2 + ": "))
agent3 = input("Please enter the third agent: ")
price3 = int(input("Please enter the sale price for agent " + agent3 + ": "))

print("%-20s %10s %10s" % ("Agent", "Price", "Commission"))
print("%-20s %10d %10.2f" % (agent1, price1, price1 * 0.025))
print("%-20s %10d %10.2f" % (agent2, price2, price2 * 0.025))
print("%-20s %10d %10.2f" % (agent3, price3, price3 * 0.025))

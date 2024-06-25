# create a program which outputs the fibonacci sequences to the nth number entered by the user
num = int(input("Enter a number: "))
a = 0
b = 1
for i in range(num):
    print(a, end=" ")
    a, b = b, a + b

# create a program that finds the value of the nth fibonacci number inputted by user
num = int(input("Enter a number: "))
a = 0
b = 1
for i in range(num):
    a, b = b, a + b
print("{:.2e}".format(a))



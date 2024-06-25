# # for i in range(1,100):
# #     print(i)
# #
# # for i in range (20, 40, 2):
# #     print(i)
# #
# # for i in range(31,21,-2):
# #     print(i)
#
# # have the user input two numbers. the program sould count from the first number to the second number. note the first number is not always less than the second number
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# if num1 < num2:
#     for i in range(num1, num2 + 1):
#         print(i)
# else:
#     for i in range(num1, num2 - 1, -1):
#         print(i)

# write a program that moves a circile across a screen horizontally in pygame
import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
keepGoing = True
RED = (255,0,0)
radius = 20
x = 20
y = 20
clock = pygame.time.Clock()
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    screen.fill((0,0,0))
    pygame.draw.circle(screen, RED, (x,y), radius)
    pygame.display.update()
    x += 1
    if x > 800:
        x = 0
    clock.tick(60)
pygame.quit()

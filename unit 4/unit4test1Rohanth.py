import random

'''
level 2/3/4
'''
# dice = random.randint(1,6)
# dice2 = random.randint(1,6)
# total = dice+dice2
# print('You rolled a %i and %i' %(dice,dice2))
# print('Total score is %i' %total)
#
# target = 10 #int(input("Enter the target score: "))
#
# rolls = 1

# while dice + dice2 != target:
#     dice = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     total = dice + dice2
#     print('You rolled a %i and %i' % (dice, dice2))
#     print('Total score is %i' %total)
#     rolls +=1
#
# print("It took %i rolls" %rolls)
#

'''
level 4+
some conditions (based on what the supply teacher told us):
- each target score is treated as its own scenario and does carry over the rolls count from the previous target score.
- for target values 5-12, the code uses the same logic as the level 4 prompt (as written in the above code)
- for target values 14-15, where the sum of two dice cannot be the target, the logic changes to be a rolling sum.
 where the rolling total score across multiple dice rolls is taken. whenver the total exceeds the target score, 
 the total resets while the rolls count does not. 
'''

total = 0
for i in range(5,16):
    rolls = 1
    dice = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice + dice2

    if i < 13:
        while dice + dice2 != i:
            dice = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total = dice + dice2
            rolls +=1
    else:
        while total != i:
            if total > i:
                total = 0
            dice = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total += dice + dice2
            rolls+=1

    print("Target score %i took %i rolls." %(i, rolls))
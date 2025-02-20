# Lesson 7
import random
dc_value = int(input("enter value of dc (1-20): "))
rolled_dice = random.randrange(1,20)

if (dc_value > rolled_dice): 
    print("you have failed!")
else: 
    print("You are sucessful!")

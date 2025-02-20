# Lesson 10
four_digs = input("Enter the last 4 digits of the phone number calling you: ")
count = 0
if(four_digs[0] == "8" or four_digs[0] == "9"):
    count = count + 1

if(four_digs[2] == four_digs[1]):
    count = count + 1

if(four_digs[3] == "8" or four_digs[3] == "9"):
    count = count + 1

if(count == 3):
    print("This is a telemarketer ")

else: 
    print("Not a telemarketer")
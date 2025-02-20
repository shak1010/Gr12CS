# Lesson 8

counter = 0
for i in range(6): # 0,1,2,3,4,5
    check = input("Enter win or loss (w or l): ")

    if (check == "w"):
        counter += 1


if (counter >= 5):
    print("Group 1")
elif (counter >= 3):
    print("Group 2")
elif (counter >= 1):
    print("Group 3")
else: 
    print("Eliminated")
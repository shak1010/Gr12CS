# Lesson 13
date = input("Enter the month (1-12) and day (1-31): ")
date = list(map(int, date.split(' ')))

month, day = date

if(month == 2):
    if(day == 18):
        print(" Exact date of Feb 18th!")
    elif(day > 18):
        print("After Feb 18th")
    else: 
        print("Before Fb 18th")
elif(month > 2):
    print("After Feb 18th")

else: 
    print("Before Feb 18th")


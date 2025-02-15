# Lesson 4
#imported math to use math.ceil
import math
#get three F inputs from user
f = input("Enter F1: ")
f2 = input("Enter F2: ")
f3 = input("Enter F3: ")
fTotal = len(f) + len(f2) + len(f3)
if (fTotal % 12 ==0):
    print(fTotal/12)
    print("0")
    print(14.95*(fTotal/12))
else: 
    print(math.ceil(fTotal/12))
    if(fTotal > 12):
        print(fTotal - 12)
    else:
        print(12-fTotal)
    print(14.95*math.ceil(fTotal/12))

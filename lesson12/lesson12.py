# Lesson 12
# My answer

angles = input("Enter the repective angles: ")
angles = list(map(int, angles.split()))

a, b, c = angles

if(sum(angles) != 180):
    print("Invalid Input doesnt equal to 180")
    exit(0)

if(a == b == c):
    print("Equilateral")

elif(a==b or c==a  or b==c):
    print("Isosceles")
else:
    print("Scalene")
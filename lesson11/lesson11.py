# Lesson 11
# My answer
'''
x_cord = int(input("Enter x cordinate: "))

y_cord = int(input("Enter y cordinate: "))

if(x_cord>0):
    if(y_cord>0):
        print("Will be in Quadrant 1")
    else:
        print("Will be in Quadrant 4")

elif(x_cord<0):
    if(y_cord>0):
        print("will be in Quadrant 2")
    else:
        print("Will be in Quadrant 3")
'''

# Answer using Maps

point = input()

point = point.split(' ') #will create a list for us

point = list(map(int, point))
print(point)

x, y = point # cool

if(x>0):
    if(y>0):
        print("Will be in Quadrant 1")
    else:
        print("Will be in Quadrant 4")

elif(x<0):
    if(y>0):
        print("will be in Quadrant 2")
    else:
        print("Will be in Quadrant 3")
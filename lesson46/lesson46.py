# Lesson 46
user = int(input("Enter a number: "))

while(user != 1):
    if(user %2 == 0):
        user = user//2
        print(user)
    else:
        user = 3*user + 1
        print(user)
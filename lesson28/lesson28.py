# Lesson 28
user = input()
palindrome = True
for i in range(len(user) // 2):
    if(user[i] != user[(len(user)-1) - i]):
        palindrome = False
        print(f"{user} is not a palindrome")
        break

if (palindrome == True):
    print(f"{user} is a palindrome")

# lesson 24

user = ""
length = 0
max_len = 0
max_string = ""
while(user != "x"):
    user = input("Enter a string(type x to stop): ")
    if (user == "x"):
        break
    
    length = len(user)

    if(max_len<length):
        max_len = length
        max_string = user


print(f"{max_string} is the longest word with {max_len} characters")


    

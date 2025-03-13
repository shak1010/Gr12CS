# Lesson 30
user = int(input("Enter number"))
temp = ""
i = 1
while(i <= user):
    if(i % 2 ==0):
        temp += "0"
    else:
        temp += "1"
    print(temp)
    i += 1
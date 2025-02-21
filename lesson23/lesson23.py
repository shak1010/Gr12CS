user = 0
total = 0
counter = 0

while user != -1:
    user = int(input("Enter Value: (type -1 to stop) "))
    
    if user == -1:
        break  

    total += user
    counter += 1


if counter > 0:
    print(f"{total / counter} is the average of your numbers")
else:
    print("No numbers were entered.")

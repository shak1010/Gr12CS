# Lesson 17

num = int(input("Enter number: "))
initial_num = num
fact = num

while(num>1): # number 1 doesnt matter as it will remain as same number
    fact = fact*(num-1)

    num-=1
else:
    print(f"Factorial of {initial_num} is: {fact}")
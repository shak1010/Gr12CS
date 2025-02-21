# Lesson 18

num = int(input("Enter number: "))
initial_num = num
fact = num

factors = ""

while(num>0): # number 1 doesnt matter as it will remain as same number
    if(fact%num == 0):
        factors += f"{num}"
        if(num != 1):
            factors+= ","
    num-=1
else:
    print(f"Factors of {initial_num} is: [{factors}]")
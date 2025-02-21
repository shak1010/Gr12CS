# Lesson 19
num = int(input("Enter number: "))
initial_num = num
fact = num
primecheck = 0
factors = ""

while(num>0): # number 1 doesnt matter as it will remain as same number
    if(fact%num == 0):
        factors += f"{num}"
        primecheck+=1
        if(num != 1):
            factors+= ","
    num-=1
else:
    if(primecheck == 2):
        print(f"{initial_num} is a prime number with the following factors: [{factors}]")
    else:
        print(f"{initial_num} is not prime and has the following factors: [{factors}]")
# Lesson 36

def factors(user):
    temp = []
    for i in range(1, user + 1): 
        if user % i == 0:  
            temp.append(i)
    return temp 
def prime(text):
    if(len(factors(text)) != 2):
        return "Not A Prime Number"
    else:
        return "A Prime Number"

# Get user input and print factors
num = int(input("Enter a number: "))
print(f"Factors are {factors(num)}")
print(f"Therefore the number is {prime(num)}")
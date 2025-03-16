# Lesson 39
def gcd(num1, num2):
    temp = []
    for i in range(1, min(num1,num2)+1): # Only up to smaller num
            if(num1 % i == 0 and num2 % i == 0):
                temp.append(i)
    return max(temp)
    
num1 = int(input())
num2 = int(input())
print(gcd(num1, num2))
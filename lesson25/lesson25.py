num = int(input("Enter number: "))
factor = 2
largest_prime = 1

while num > 1:
    if num % factor == 0:
        largest_prime = factor  
        num //= factor  
    else:
        factor += 1  

print(f"The largest prime factor is {largest_prime}")

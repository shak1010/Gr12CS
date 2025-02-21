# Lesson 21

N = int(input("Enter N input: "))

max_factors = 0
number_with_max_factors = 1

for num in range(1, N + 1): 
    factors = []  
    for i in range(1, num + 1): 
        if num % i == 0:
            factors.append(i)  

    if len(factors) > max_factors:
        max_factors = len(factors)
        number_with_max_factors = num

print(f"Number with most factors: {number_with_max_factors} (Total Factors: {max_factors})")
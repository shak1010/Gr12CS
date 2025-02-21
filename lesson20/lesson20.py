# Lesson 20
total_sum = 0

for num in range(0, 10000): 
    divisors_sum = 0

    for i in range(1, num): 
        if num % i == 0:
            divisors_sum += i

    if divisors_sum == num: 
        total_sum += num

print(f"Sum of all perfect numbers under 10,000: {total_sum}")
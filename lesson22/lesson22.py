# Lesson 22

# Straight to video lol

upper_limit = int(input("Enter Nth num: "))

fib_0 = 0
fib_1 = 1
fib_n = 0

for n in range (2, upper_limit + 1):
    fib_n = fib_1 + fib_0

    fib_0 = fib_1
    fib_1 = fib_n

print(f"Fibonacci[{upper_limit}] is {fib_n}")
# Lesson 5
money = int(input("Enter amount of money you started with: "))
cookiename = input("Enter a string contaning b(large cookie) and c(normal cookie) ")

numb = cookiename.count("b")
numc = cookiename.count("c")

print(f"Number of Normal cookies: {numb}")
print(f"Number of Big cookies: {numc}")

print(f"profit of normal cookie: {numb*(1.25-0.5)} ")
print(f"profit of big cookie: {numb*(2.00-0.75)} ")

print(f"You have {money - (numc*1.25 + numb*2.00)} dollars remaining")
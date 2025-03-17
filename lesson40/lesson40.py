# Lesson 40
def factors(num):
    i = 1
    fact_list = []
    while(num>=i):
        if(num % i == 0):
            fact_list.append(i)
        i+=1
    if(len(fact_list)!=2):
        return "Not A prime Number"
    else:
        return "prime"

num = int(input())
print(factors(num))


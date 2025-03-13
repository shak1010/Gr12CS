# Lesson 33
from random import seed
from random import randrange

def mean(a_list):

    return sum(a_list)/ len(a_list)

def median(a_list):
    sorted_a_list = sorted(a_list)
    middle = len(a_list)//2
    if(len(a_list)%2==0):
        left = sorted_a_list[middle-1]
        right = sorted_a_list[middle+1]
        return (left+right) / 2
    else:
        return sorted_a_list[middle]

seed(2)
data = [randrange(1,100) for _ in range(randrange(10,30))]
print(data)
print(mean(data))
print(median(data))
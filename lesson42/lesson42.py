# Lesson 42
def possiblesum(a_list, target):
    
    for i, value in enumerate(a_list):
        new_target = target - value

        if new_target in a_list[i+1:]:
            return True 
    return False

test = [1,3,5,8,12,13,22]
target= 16

print(possiblesum(test, target))
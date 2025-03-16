# Lesson 38
def pal(text):
    return text == text[::-1] # slicing to reverse a slicable object

pal_num = []

for num1 in range(999,99,-1):
    for num2 in range(999,99,-1):
        cp = num1*num2

        if pal(str(cp)):
            pal_num.append(cp)

print(max(pal_num))
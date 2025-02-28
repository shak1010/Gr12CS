# Lesson 29
def consonant_counter(text):
    counter = 0
    text.lower()

    for i in range (0, len(text)):
        if(text[i].isalpha()):
            if text[i] not in "aeiou":
                counter+=1
    
    return counter

print(consonant_counter(input("enter string: ")))
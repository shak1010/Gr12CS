# Lesson 44
user = input()

def frequency(word):
    return {char: word.count(char) for char in word}

print(frequency(user))
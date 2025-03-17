# Lesson 45
user = input()
user = user.split(", ")

def length(words):
    return {word: len(word) for word in words}

print(length(user))
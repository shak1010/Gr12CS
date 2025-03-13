# Lesson 27
def string_cleaner(text):
    result = " "
    for character in text:
        if(character.isalpha()):
            print(character, end = "")
    return result

string_cleaner(input("Enter word"))
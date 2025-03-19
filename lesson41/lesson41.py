# Lesson 41
def scrabble(word): 
    total_score = 0
    for character in word.upper():  
        if character in "EAIONRTLSU":
            total_score += 1
        elif character in "DG":
            total_score += 2
        elif character in "BCMP":
            total_score += 3
        elif character in "FHVWY":
            total_score += 4
        elif character in "K":  
            total_score += 5
        elif character in "JX":
            total_score += 8
        elif character in "QZ":
            total_score += 10
    return total_score

def highest_scrabble_score(words):
    highest_word = words[0]  
    highest_score = scrabble(words[0])
    
    for word in words: 
        score = scrabble(word)  
        if score > highest_score: 
            highest_word = word  
            highest_score = score  
    
    return highest_word  

words = input("Enter words separated by spaces: ").split()
print(f"{highest_scrabble_score(words)} is word with most points")  



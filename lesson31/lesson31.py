# Lesson 31
def anagrams_check(user1, user2):
    if(len(user1) != len(user2)):
        return "Not A Anagram"
    if(sorted(user1) == sorted(user2)):
        return "Anagram"
    else:
        return "Not A Anagram"

word1 = input()
word2 = input()

print(anagrams_check(word1, word2))
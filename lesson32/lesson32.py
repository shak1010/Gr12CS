# Lesson 32
def duplicate_check(user1, user2):
    sort = ""
    user1 = sorted(set(user1)) # remove duplicates
    user2 = sorted(set(user2))

    for i in range(0, len(user1)):
        for x in range(0, len(user2)):

            if(user1[i] == user2[x]):
                sort += user1[i]

    return sort

word1 = input()
word2 = input()

print(duplicate_check(word1, word2))
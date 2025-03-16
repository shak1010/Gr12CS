# Lesson 37
def compress_string(s):
    compressed = []
    count = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            compressed.append(s[i] + str(count))
            count = 1  # Reset counter for the next character


    compressed.append(s[-1] + str(count))

    compressed_str = "".join(compressed)
    

    return compressed_str if len(compressed_str) < len(s) else s


print(compress_string(input()))  
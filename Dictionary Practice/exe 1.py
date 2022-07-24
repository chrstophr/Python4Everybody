dictionary_words = dict()
fhand = open('words.txt')

for line in fhand:
    words = line.split()
    for word in words:
        if word in dictionary_words:
            continue
        dictionary_words[word] = 1
    
print(dictionary_words)
    

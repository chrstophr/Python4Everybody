fhand = open('mbox-short.txt')

for line in fhand:
    words = line.split()
#    print(words)
    if len(words) == 0 or words[0] != 'From' :
        continue
    print(words[2])


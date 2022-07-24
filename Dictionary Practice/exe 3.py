address_count = dict()

fhand = open('mbox-short.txt')

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[1] not in address_count:
            address_count[words[1]] = 1
        else:
            address_count[words[1]] +=1
print(address_count)


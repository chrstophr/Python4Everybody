mails_count = dict()

fhand = input('Enter a file name: ')
try:
    mail = open(fhand)
except:
    print('Please enter a valid file name!')

for line in mail:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[1] not in mails_count:
            mails_count[words[1]] = 1
        else:
            mails_count[words[1]] += 1
#print(mails_count)
maximum = 0
maximum_adress = ''
for address in mails_count:
    if mails_count[address] > maximum:
        maximum = mails_count[address]
        maximum_adress = address
print(maximum_adress, maximum)


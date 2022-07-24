domain_name = dict()

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
        atpos = words[1].find('@')
        domain = words[1][atpos+1:]
        if domain not in domain_name:
            domain_name[domain] = 1
        else:
            domain_name[domain] += 1
print(domain_name)


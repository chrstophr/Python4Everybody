days_mail = dict()
mails = open('mbox-short.txt')

for line in mails:
    word = line.split()
    if len(word) < 3 or word[0] != 'From':
        continue
    else:
        if word[2] not in days_mail:
            days_mail[word[2]] = 1
        else:
            days_mail[word[2]] +=1
    
print(days_mail)
        



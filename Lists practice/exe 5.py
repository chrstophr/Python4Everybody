fhand = input('Enter a file name: ')
fname = open(fhand)
count = 0
for line in fname:
    if line.startswith('From '):
        line = line.split()
        print(line[1])
        count = count + 1
    
print('There were ', count, ' lines with From as the first word in ', fhand, 'file')

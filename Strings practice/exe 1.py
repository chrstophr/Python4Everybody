fname = input('Enter a file name: ')
filename = open(fname)
for line in filename: 
    line= line.rstrip()
    print(line.upper())

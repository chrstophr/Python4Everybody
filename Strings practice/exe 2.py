fname = input('Enter the file name: ')
try:
    filename = open(fname)
except:
    print('File cannot be opened: ', fname)
count = 0
total = 0
for line in filename:
#    if len(line) > 0 and line.startswith('X-DSPAM-Confidence:'):
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        confidence = float(line[20:])
        total = total + confidence
print('Average spam confidence: ' + str(total/count))

# Try with the following files: 
#    mbox-short.txt
#    mbox.txt

lst = []
while True:
    fhand = input('Enter a number: ')
    try: 
        fhand = float(fhand) 
        lst.append(fhand)
    except: 
        if fhand == 'done' or fhand == 'Done':
            break
        else:
            print('Please enter a valid input!')
            continue
        
print('Maximum: ', max(lst))
print('Minimum: ', min(lst))



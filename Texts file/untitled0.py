x = 'banana'
print(type(x))
print(x.count('a'))


stri = 'X-DSPAM-Confidence:0.8475'
colpos= stri.find(':')
print(colpos)
flo= float(stri[colpos + 1:])
print(flo)


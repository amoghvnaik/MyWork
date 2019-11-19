sentence = input('Enter a string:')
vowels = 'A,a,E,e,I,i,O,o,U,u'
count = 0
for each_char in sentence:
    if each_char in vowels:
        count += 1 
print('There are {} vowels in the string: \'{}\''.format(Count,sentence))


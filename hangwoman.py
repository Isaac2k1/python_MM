searchword="hangthewhitch"
print('Your word has %d letters.' % len(searchword))
foundword = '-' * len(searchword)   # create a string with filling characters
contained_letters = set()
found_letters = set()

for i in searchword:                # collect all letters of searchword in a set
    contained_letters.update(i)
print(contained_letters)            # debug only, comment this line

lives = len(contained_letters)      # minimum trials needed to not hung
print('Totally {0:d} trials'.format(lives))


while True:
    print('\nYou have {0:d} trials left.'.format(lives))
    inputchar = input("Guess a letter:")
    lives -= 1
    if inputchar in found_letters:
        print('DEJA VU!')       # letter has been entered before
        lives += 1              # do not punish player
    else:                       # a new letter has been entered
        for letter in searchword:    # check if letter is contained
            print('check letter {0:s}'.format(letter))
            lives -= 1
            if inputchar == letter:
                #print(inputchar, end='')
                found_letters.update(inputchar)
                print(found_letters)
            for letter in searchword:    # loop thru searchword and... check if letter from found_letter matches
                if letter in found_letters:
                    print(letter, end='')
                else:
                    print('-', end='')
        
    inputchar = ''
                
                
            
    if lives <= 0:
        break

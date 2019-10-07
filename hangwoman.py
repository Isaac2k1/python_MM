searchword="hangthewhitch"
print('Your word has %d letters.' % len(searchword))
foundword = '-' * len(searchword)   # create a string with filling characters
contained_letters = set()   # this is the set of all letters of searchword
found_letters = set()   # this set contains all sucessfully guessed letters

for i in searchword:                # collect all letters of searchword in a set
    contained_letters.update(i)
print(contained_letters)            # debug only, comment this line

lives = len(contained_letters)      # minimum trials needed to not hung
print('Totally {0:d} trials'.format(lives))

while True:
    print('\nYou have {0:d} trials left.'.format(lives))
    inputchar = ''
    inputchar = input("Guess a letter:")
    lives -= 1
    if inputchar in found_letters:
        print('DEJA VU!')       # letter has been entered before
        lives += 1              # do not punish player
    else:                       # a new inputchar has been entered
        for letter in searchword:    # check for inputchar in searchword
            print('check letter {0:s}'.format(letter))
            lives -= 1
            if inputchar == letter: # input is a new letter, store it in found_letters
                #print(inputchar, end='')
                found_letters.update(inputchar)
                print(found_letters)
            for letter in searchword:    # loop thru searchword and... check if letter from found_letter matches
                if letter in found_letters:
                    print(letter, end='')
                else:
                    print('-', end='')

                
                
            
    if lives <= 0:
        break

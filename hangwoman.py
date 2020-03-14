searchword="abcd"
print('The word to find has %d letters.' % len(searchword))
foundword = '-' * len(searchword)   # create a string with filling characters
contained_letters = set()   		# this is the set of all letters of searchword
found_letters = set()  				# this (empty) set contains all sucessfully guessed letters

for i in searchword:                # collect all letters of searchword in a set
    contained_letters.update(i)
# print(contained_letters)            # debug only, comment this line

lives = len(contained_letters)      # minimum trials needed to not hung
print('You got totally {0:d} trials'.format(lives))

while True:
    print('You have {0:d} trials left.'.format(lives))
    #inputchar = ''
    inputchar = input("Guess a letter:")
    print('You entered: {}'.format(inputchar))
    lives -= 1
    if inputchar in found_letters:
        print('DEJA VU LETTER {}!'.format(inputchar))       # letter has been entered before
        lives += 1              	# do not punish player
    else:                       	# a new inputchar has been entered
        for letter in searchword:   # check for inputchar in searchword
            #print('check letter {0:s}'.format(letter))
            if inputchar == letter: # input is a new letter and in searchword, store it in found_letters
                #print(inputchar, end='')
                found_letters.update(inputchar)
                #print(found_letters)
        tofindletters=0

    for letter in searchword:    # loop thru searchword and... check if letter from found_letter matches
        if letter in found_letters:
            print(letter, end='')
        else:
            print('-', end='')
            tofindletters +=1
    #print("  - minusse:{}".format(tofindletters))

    if tofindletters <=0:
        print("You WIN with {} live(s) left!".format(lives))
        break

    if lives <= 0:
        print("YOU LOST!")
        break
    else:
        print("{} lives left".format(lives))


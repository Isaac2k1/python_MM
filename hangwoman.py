searchword="hangthewhitch"
print('Your word has %d letters.' % len(searchword))
print(len(searchword))
foundword = '-' * len(searchword)
foundletters = set()

for i in searchword:    
    print('-', end='')
print(' ')
print (searchword)


lives = 6
while True:
    print('\nYou have {0:d} trials.'.format(lives))
    inputchar = input("Enter a letter:")
    print("input was:", inputchar)
    lives -= 1
    for i in searchword:
        if inputchar in foundletters:
            print(inputchar, end='')
            lives += 1
            if inputchar == i:
                print(inputchar, end='')
                
            else:
                print('-', end='')
            
    if lives <= 0:
        break

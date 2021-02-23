found_letters = set()

for i in range(10):
    inputchar = input("Guess a letter {0:d}:".format(i))
    if inputchar in found_letters:
        print('DEJA VU!')
    else:
        if inputchar != '':
        	found_letters.update(inputchar)
print(found_letters)

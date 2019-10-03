found_letters = set()

for i in range(10):
    inputchar = input("Guess a letter:")
    if inputchar in found_letters:
        print('DEJA VU!')
    else:
        found_letters.update(inputchar)
print(found_letters)

# perm4WofW helper to solve Words of Wonders (German language, others possible)
''' get German word list from
https://www1.ids-mannheim.de/kl/projekte/methoden/derewo.html
Rename to DeReWo.txt and store it a readable ASCII format.
Enter the letters given in game 'Words of Wonders' as searchword
program produces all combinations of given letters and reduces down 
to three letter words. Then all words of DeReWo are checked if they appear 
in permutations of searchword letters.'''

liste = set()
def analine(line, liste):
    '''analine analyses line and adds words to liste. Since liste is a set
    there is no repetition of words. Also case is changed to upper.'''
    import re  
    line = re.split(' ', line)[0]
    if ' ' in line:
        parts = re.split(' ', line)
        liste.add(parts[0])

    if '(' in line:
        parts = re.split('\(|\)', line)
        liste.add(parts[0]) # append root word
        brackets = re.split(',',parts[1])
        for sil in brackets:
            liste.add(parts[0]+sil)

    else:
        if ',' in line:
            for sil in line.split(","):
                liste.add(sil)
        else:
            liste.add(line)
             
    return liste
 
# Ale's refactor from 2020-03-29 19h01
import itertools

def generate_words(data):
    permutations = []
    for i in range(len(data), 2, -1): # second parameter: length of shortest word -1
        permutations = permutations + [''.join(p) for p in itertools.permutations(data, i)]
    return permutations

# === MAIN PROGRAM ===
ObjRead = open("DeReWo.txt", "r")
print("start reformatting of wordlist...")
words = 0
with ObjRead as textfile:
    while True:    
        line = textfile.readline()
        analine(line.upper(), liste)
#        if words < 50:
#            print(line, liste)
        words += 1
        
        if len(line) == 0:
            break

print("...ferdisch, found",words,"words")
ObjRead.close()

data = input("enter your searchword:")
permutations = generate_words(data.upper())
#print(permutations) # do not print 324567 words ;-)
print("The string", data, "has", len(permutations), "unique combinations.")

found = 0
found_words = []
for word in liste: # this could be speeded-up by sorting liste for length
    # and test only words of liste up to the length of searchword
    if word in permutations:
        found_words.append(word)
print("There is", len(found_words), "words in the German dictionary.")
found_words.sort()
for word in found_words:
    print(word)

print("Ferdisch!")
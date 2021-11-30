# perm4WofW helper to solve Words of Wonders (German language, others possible)
'''
Get German word list from
https://www1.ids-mannheim.de/kl/projekte/methoden/derewo.html
Rename to DeReWo.txt and store it a readable ASCII format.
'''

liste = set()
def analine(line, liste):
    '''analine analyses a line of the word list and generates the word(s) for liste. Since liste is a set
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

filename = "//Mac/Home/Documents/GitHub/python_MM/WordSearch/DeReWo.txt"
ObjRead = open(filename, "r")
print("START reformatting of wordlist...")
words = 0
with ObjRead as textfile:
    while True:    
        line = textfile.readline()
        analine(line.upper(), liste)
        words += 1
        if len(line) == 0:
            break
print("...FERDISCH, found",words,"words")
ObjRead.close()

# === MAIN PROGRAM ===
print(55 * "=")
'''Enter the letters given in game 'Words of Wonders' as searchword
program produces all combinations of given letters and reduces down 
to three letter words. Then all words of DeReWo are checked if they appear 
in permutations of searchword letters.'''

# Ale's refactor from 2020-03-29 19h01
import itertools

def generate_words(data):
    permutations = []
    for i in range(len(data), 2, -1): # second parameter: length of shortest word -1
        permutations = permutations + [''.join(p) for p in itertools.permutations(data, i)]
    return permutations

def length_sort(foundwords, displayarray, colindexes, maxwords):
    """foundwords contains the input list of words to be sorted into displayarray"""
    displayarray = [[]]
    colindexes = []
    maxwords = 0
    # Sort words according length
    longestword = len(max(foundwords, key=len))
    # Prepare array to store lists with for each word lenght group
    for i in range(longestword):
        displayarray.append([])
    # Append word to its word length group list
    for word in foundwords:
        displayarray[len(word)].append(word)

    # Prepare table of words for column output
    for line in displayarray:
        len_line = len(line)
        if len_line > 0:
            colindexes.append(len(line[0]))
            if maxwords < len_line:
                maxwords = len_line
    return foundwords, displayarray, colindexes, maxwords

# === MAIN PROGRAM ===
data = "indexs" # input("enter your searchword:")

permutations = generate_words(data.upper())
print("The string", data, "has", len(permutations), "unique combinations.")

found = 0
found_words = []
display_array = [[]]
col_indexes = []
max_words = 0

for word in liste: # this could be speeded-up by sorting liste for length
    # and test only words of liste up to the length of searchword
    if word in permutations:
        found_words.append(word)
print("There is", len(found_words), "words in the German dictionary.")
found_words.sort()

found_words, display_array, col_indexes, max_words = length_sort(found_words, display_array, col_indexes, max_words)

for i in col_indexes:
    print(len(display_array[i]), "x ", i, "-letter words")

print("max_words:", max_words)
# Print table in columns with increasing string length
for i in range(max_words):
    for j in col_indexes:
        try: 
            word2print = display_array[j][i]
            print(word2print, end = " ")
        except IndexError:
            print(j*"_", end = " ")
    print("")
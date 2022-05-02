# W5 is a WORDLE helper to find five letter words and search for them
# Ale's refactor from 2020-03-29 19h01
import itertools
import re
from math import perm

def generate_wordle(data):
    permutations = []
    for i in range(5): # assuming WORDLE uses always 5 letters
        permutations = permutations + [''.join(p) for p in itertools.permutations(data, i)]
    return set(permutations)
    
def analineW5(line, liste):
    line = line.rstrip("\n")
    if len(line) == 5:
        liste.add(line)
    return liste

# === PREPARE WORDLIST ===
ObjRead = open("web2.txt", "r")
print("start reading wordlist...")
words5 = 0
totalwords = 0
liste = set()
with ObjRead as textfile:
    while True:
        line = textfile.readline().upper()
        if len(line) == 0:
            break
        totalwords += 1
        analineW5(line, liste)

liste = list(liste)
liste.sort()

found = []
ReEx = re.compile(r'OO')

#find all the words starting with 'a' or 'e'
for word in liste:
    found.append(ReEx.search(word))

print('found words:', len(found), found)

print("List had", totalwords, "words, found",len(found),"five letter words")
ObjRead.close()

column = 0
lines = 0
nofcol = 10

for word in liste:
    print(word, end=' ')
    column += 1
    if not(column % nofcol):
        print(lines)
        lines += 1

print("\nList had", totalwords, "words, found") #,len(liste),"five letter words")

# Enter up to 5 letters to get suggestions for WORDLE.



'''
Get German word list from
https://www1.ids-mannheim.de/kl/projekte/methoden/derewo.html
Rename to DeReWo.txt and store it a readable ASCII format.
'''

# liste = set()
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

print(dir())
liste = set()
filename = "//Mac/Home/Documents/GitHub/python_MM/WordSearch/DeReWo.txt"
filename = "C:\\Users\\chmamai\\OneDrive - Hitachi Energy\\Documents\\Python Scripts\\python_MM\\WordSearch\\DeReWo"
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

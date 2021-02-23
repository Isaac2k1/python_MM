searchword = 'hangthewitch'
foundletters = set()

for i in searchword:
    print(i,end='')
    validletters.update(i)
print(validletters)


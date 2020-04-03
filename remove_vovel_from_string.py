# remove vovels from word
word = "Erdbeeren"
result = ""
vovel=['a','e','i','o','u']
vovels="aeiou"

for c in word:
    if not c in vovels:
        result = result + c
print(result)

# rdbrn


# ein wort -> vokalen entfernen
# remove vowels from word

word = "Erdbeeren"
result = ""

# nimm jedes Zeichen von word
#   wenn kein vokal hänge an result an.
for c in word:
    if not c in "aeiou":
        result = result + c
print(result)
# rdbrn

vowel=['a','e','i','o','u']

print(', '.join(vowel))

print("".join([c for c in word if c.lower() not in vowel]))



def get_word_without_vocals(word):
    return "".join([c for c in word if c.lower() not in 'aeoiu'])

print(get_word_without_vocals(word))

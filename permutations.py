# Python function to print permutations of a given list
# Ale: https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list/104436#104436
#import itertools
# list(itertools.permutations([1, 2, 3])
def permutation(lst):

	# If lst is empty then there are no permutations
	if len(lst) == 0:
		return []
		
	# If there is only one element in lst then, only
	# one permuatation is possible
	if len(lst) == 1:
		return [lst]
		
	# Find the permutations for lst if there are
	# more than 1 characters
	
	l = [] # empty list that will store current permutation
	
	# Iterate the input(lst) and calculate the permutation
	for i in range(len(lst)):
		m = lst[i]
		
		# Extract lst[i] or m from the list.  remLst is
		# remaining list
		remLst = lst[:i] + lst[i+1:]
		
		# Generating all permutations where m is first
		# element
		for p in permutation(remLst):
			l.append([m] + p)
	return l

# Function to convert a list to string 
def listToString(s): 
	
	# initialize an empty string 
	str1 = "" 
	
	# traverse in the string 
	for ele in s: 
		str1 += ele 
	
	# return string 
	return str1 
			
	
# Driver program to test above function
import itertools
data = list(input("enter your searchword:"))
#print(data)

for lwords in range(len(data),1,-1):
	print(lwords,"-letter words")
	print(len(data),"-letter words")
	all_permutations = set()
	count = 0
	for p in itertools.permutations(data):
	#for p in permutation(data):
		count +=1
		strg=listToString(p)
		all_permutations.update({strg[0:lwords]})
	#print(all_permutations)
	all_permutations = sorted(all_permutations)
	for word in all_permutations:
		print(word)
	print(len(all_permutations)," of ",count)
	print("Permutations: ",count)


# Ale's refactor from 2020-03-29 18h22
def generate_words(data):
    for lwords in range(len(data), 1, -1):
        print(lwords, "-letter words")
        print(len(data), "-letter words")
        all_permutations = set()
        count = 0
        for p in permutation(data):
            count += 1
            strg = listToString(p)
            all_permutations.update({strg[0:lwords]})
        #print(all_permutations)
        all_permutations = sorted(all_permutations)
        for word in all_permutations:
            print(word)
        print(len(all_permutations), " of ", count)
        print("Permutations: ", count)
 
# Driver program to test above function
data = list(input("enter your searchword:"))
generate_words(data)

# ----
# Ale's refactor from 2020-03-29 19h01
import itertools

def generate_words(data):
    for i in range(len(data), 1, -1):
        permutations = [''.join(p) for p in itertools.permutations(data, i)]
        print(permutations)

# data = input("enter your searchword:")
# generate_words(data)
generate_words('casa')

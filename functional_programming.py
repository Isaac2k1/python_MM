# if statements
# procedural
def a(i):
	if i==1:
		return "one"
	elif i==2:
		return "two"
	else:
		return "three"
		
print(a(1)) # one
print(a(2)) # two
print(a(3)) # three

#functional
a = lambda x: x
b = lambda x: (x == 1 and a("one"))\
	or (x == 2 and a("two"))\
	or (a("three")) 
	
print(b(1)) # one
print(b(2)) # two
print(b(3)) # three

print("===== grocery list =====")
# procedural
print("*** procedural ***")
grocery_list = ['apples','bananas','oranges','milk']

for grocery in grocery_list:
	print(grocery)
	
#functional
print("*** functional ***")
grocery_list = ['apples','bananas','oranges','milk']

def grocery(list):
	print(list)
	
map(grocery, grocery_list)
#print(result)
#print(list(result))

#grocery_list)


# Python program to demonstrate working 
# of map. 
  
# Return double of n 
def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 


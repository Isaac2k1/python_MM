#print biggest number of three without using max function

numbers = [-3, 42, 0]
max=numbers[0]		# initialize the maximum with the first element of the array
# max=-1E90			# initialize with a very small value, this is not good because it could be that all values are smaller than this
# -1*float("inf")	# initialize with negative infinite, might probably also work always

for n in numbers:
	if n > max:
		max = n
print(max)

print(len(numbers))	# show length of input field

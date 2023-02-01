# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(dict):

	sum = 0
	for i in dict.values():
	    sum = sum + i
	return sum
	


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

# define a function of dict
# take an empty variable
# using for loop get the dict of values , because we need to get each
# value and we have to sum  all the values in to one.
# return sum
# call the function
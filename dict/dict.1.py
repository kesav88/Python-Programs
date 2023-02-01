# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of
#  List

# initializing Dictionary
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Key-Value list Dictionary to Lists of List
res = []
for i in test_dict.keys():
    test_dict[i].insert(0, i)
    res.append(test_dict[i])
# printing result
print("The converted list is : " + str(res))

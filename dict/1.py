myDict = {'ravi': 10, 'rajnish': 9,'sanjeev': 15, 'yash': 2, 'kesav': 32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
print(sorted_dict)


# take a list of keys
# and sort those
# and iterate them in loop and allot them to a saperate variable.
# and print them

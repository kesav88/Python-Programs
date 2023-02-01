#remove no value items from Dictionary
mydict = {'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}
key_list=[]
for key,val in mydict.items():
    if val== None:
        key_list.append(key)

for i in key_list:
    del mydict[i]

print(mydict)
#Python Program to Reverse a String without using slice 

string='kesava'
rev_str=""
for i in range(len(string)-1,-1,-1):
    rev_str += string[i]


print(rev_str)
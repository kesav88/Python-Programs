#Python Program to Remove Odd Indexed Characters in a string

# s='kesava'
# string=s[::2]
# print(string)

#another way

def rm_odd_index(s):
    return ''.join(s[i] for i in range(0,len(s),2))


s='kesavaraju'
print(rm_odd_index(s))
#Python Program to Check if a Key Exists in a Dictionary or Not
def check_key(d,key):
    keys=d.keys()
    if key in keys:
       return f'key {key} is present in {d}'
    else:
        return f'key {key} is not present in {d}'



d={1:'a',2:'b',3:'c'}
key=2
print(check_key(d,key))
#Python Program to Determine How Many Times a Given Letter Occurs in a String 

def count(s,i):
    
    count=0
    for letter in s:
        if letter == i:
            count += 1
    return count


s='kesava'
i='a'
print(count(s,i))
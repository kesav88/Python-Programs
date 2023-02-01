#Python Program that Displays which Letters are in First String but not in Second

def letters_in_str1(str1,str2):
    s=''
    for i in str1:
        if i not in str2: 
            s += i
    return s

str1="kesava"
str2="raju"
print(letters_in_str1(str1,str2))

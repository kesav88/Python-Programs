#Python Program that Displays Letters that are not Common in Two Strings
def not_common_chars(str1,str2):
    s=''
    for i in str1:
        if i not in str2:
            s += i
    for i in str2:
        if i not in str1:
            s += i
    
    return s


str1="kesava"
str2="raju"
print(not_common_chars(str1,str2))
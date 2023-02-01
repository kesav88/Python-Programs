#Python Program to Find Common Characters in Two Strings

def common_chars(str1,str2):
    s=''
    for i in str1:
        if i in str2:
            if i not in s:
                s += i
            else:
                continue
    return s



str1="kesava"
str2="raju"
print(common_chars(str1,str2))
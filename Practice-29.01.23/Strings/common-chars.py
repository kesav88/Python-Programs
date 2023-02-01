#Python Program to Print All Letters Present in Both Strings

def common_chars(str1,str2):
    s=''
    for i in str1:
        if i in str2:
            s += i
    return s


str1="kesava"
str2="kanumuri"
print(common_chars(str1,str2))
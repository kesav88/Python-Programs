#Python Program to Remove the nth Index Character from a Non-Empty String

def rm_nth_index(s,n):
    if n < 0 or n >= len(s):
        print("invalid index")
    return s[:n] + s[n+1:]


s="kesava"
n=4
print(rm_nth_index(s,n))
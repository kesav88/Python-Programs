s1=input()
s2=input()
i=0
if len(s1) == len(s2):
    k=s1[i]
    if k in s2:
        print("its a anagram")
        i += 1
    else:
        print("is not anagram")
else:
    print("its not a angram string")

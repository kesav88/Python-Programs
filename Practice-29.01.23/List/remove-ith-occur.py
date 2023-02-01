#Python Program to Remove the ith Occurrence of the Given Word in a List

def remove_word(L,word,i,count=0):
    if not L:
        return []
    elif L[0] == word:
        count += 1
        if count == i:
            return L[1:]
        else:
            return [L[0]] + remove_word(L[1:],word,i,count)
    else:
        return [L[0]] + remove_word(L[1:],word,i,count)



L=['msys','devops','IT','msys','IT','devops','msys']
word= 'IT'
i= 2
result= remove_word(L,word,i)
print(result)
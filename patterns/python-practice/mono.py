a=[1,2,3,4]
def func(a):
    res=[]
    for i in a[::-1]:
        res.append(i)

    return res


b=func(a)
print(b)

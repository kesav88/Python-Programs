#Python Program to Find the Cumulative Sum of a List

def cum_sum(L):
    if len(L) == 1:
        return L
    else:
        return [L[0]] + [L[0] + L[1]] + cum_sum(L[1:])


L=[1,2,3,4,5]
print(cum_sum(L))
# l=[]
# # result=cum_sum(L)
# # print(result)
# for i in L:
#     l.append(i)
    
# print(l)

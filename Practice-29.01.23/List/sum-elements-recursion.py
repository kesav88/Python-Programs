def find_sum(L, leng):
    if leng == 0:
        return L[leng]          # if length is 0 it will return L[0]
    else:
        return L[leng] + find_sum(L, leng-1)  # if len != 0, it will return last elements + all elements before it

L = [1, 2, 3, 4, 5]
leng = len(L)
print("The sum of all elements in the list is: ", find_sum(L, leng-1))

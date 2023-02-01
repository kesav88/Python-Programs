# #Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List
L=[-5,1,9,7,8,-4,-2,6,3]
neg_sum=0
even_sum=0
odd_sum=0
for i in L:
    if i < 0:
        neg_sum += i
    elif i % 2 ==0:
        even_sum += i
    else:
        odd_sum += i
print("sum of even numbers: ", even_sum)        
print("sum of odd numbers: ", odd_sum)
print("sum of negative numbers: ", neg_sum)

# second way, long program
# L=[-1,1,2,3,4,8,9,7,-9,-5]
# neg_lst=[]
# even_lst=[]
# odd_lst=[]
# for i in L:
#     if i < 0:
#         neg_lst.append(i)
#     elif i % 2 == 0:
#         even_lst.append(i)
#     else:
#         odd_lst.append(i)
# # print(neg_lst)
# # print(even_lst)
# # print(odd_lst)

# neg_sum=0
# even_sum=0
# odd_sum=0
# for i in neg_lst:
#     neg_sum += i
# print("sum of negative number: ", neg_sum)

# for i in even_lst:
#     even_sum += i
# print("sum of even numbers: ", even_sum)
# for i in odd_lst:
#     odd_sum += i
# print("sum of odd numbers: ", odd_sum)
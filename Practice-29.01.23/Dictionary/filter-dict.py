#filter dictionary where the value is less than 20000

di = {'Jack': 12000, 'Max': 2000, 'Hack': 25000, 'Nack': 80000}
new_dic={}
for key,value in di.items():
    if value < 20000:
        new_dic[key] = value

print(new_dic)
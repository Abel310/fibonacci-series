list1=[12,-7,5,64,-14]
list2=[12,14,-95,3]
list3=[]
list4=[]
for number in list1:
    if(number>=0):
        list3.append(number)
print("positive numbers in list1: ",list3)
for number in list2:
    if(number>=0):
        list4.append(number)
print("positive numbers in list2: ",list4)

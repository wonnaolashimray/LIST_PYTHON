list1=[7,90,56,45,3,8]
i=0
while i<len(list1):
    j=0
    while j<len(list1)-1:
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
        j+=1
    i+=1
print(list1)
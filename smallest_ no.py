#write a python program to get the smallest number from the list.

# list1=[56,7,35,27,78,12]
# i=0
# smallest=list1[0]
# while i< len(list1):
#     if list1[i]<smallest:
#         smallest=list1[i]
#     i+=1
# print(smallest)



list1=[[1,2,4,8,10],[1,4,15,11],[10,20,30,40,50,60]]
i=0
l=[]
s=0
while i<len(list1):
    j=0
    sum=0
    while j<len(list1[i]):
        sum=sum+list1[i][j]
        j+=1
    s+=sum
    i+=1
l.append(s)
print(l)

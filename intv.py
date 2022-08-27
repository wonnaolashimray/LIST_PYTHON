# list=['a','b',['c',['d','e',['f','g','h','i','j'],'k'],'l'],'m','n']
# a=[]
# i=0
# while i<len(list):
#     if type(list[i])==type([]):
#         j=0
#         while j<len(list[i]):
#             a.append(list[i][j])
#             j+=1
#     else:
#         a.append(list[i][j])
#     i+=1
# print(a)

# list=[['g','f','g'],['i','s'],['b','e','s','t']]
# i=0
# sum=""
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         sum+=list[i][j]
#         j+=1
#     i+=1
# print(sum)

def num():
    a=[]
    sum=0
    i=0
    while i<10:
        user=int(input("enter the number"))
        a.append(user)
        sum+=a[i]
        i+=1
    return sum
print(num())


i=0
a=[]
b=[]
rev=0
while i<10:
    user=int(input("enter the number"))
    a.append(user)
    i+=1
j=-1
while j>=-len(a):
    b.append(a[j])
    j-=1
print(b)

list=["p","q"]
n=5
i=1
sum=0
a=[]
while i<=n:
    j=0
    while j<len(list):
        b=list[j]+str(i)
        a.append(b)
        j+=1
    i+=1
print(a)

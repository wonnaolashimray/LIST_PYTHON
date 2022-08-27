i=0
count1=0
count2=0
count3=0
count4=0
count5=0
while i<20:
    user=int(input("enter th number"))
    if user<0:
        count1+=1
        print("negative=",user,",","count=",count1)
    if user>0:
        count2+=1
        print("positive=",user,",","count=",count2)
    if user==0:
        count3+=1
        print("zero",",","count=",count3)
    if user%2!=0:
        count4+=1
        print("odd=",user,",","count=",count4)
    if user%2==0:
        count5+=1
        print("even=",user,",","count=",count5)
    i+=1
# user=int(input("enter the number  :"))
# a=user//2
# i=1
# while i<=a:
#     print(user)
#     i+=1


# user1=int(input("enter the number :"))
# user2=int(input("enter the number  : "))
# i=1
# j=1
# l=[]
# while i<=user2:
#     if i<=user2:
#         k=j*user1
#         l.append(k)
#     j+=1
#     i+=user1
# print(l)


# user=float(input("enter the number : "))
# if user>1.0:
#     print("Error")
# elif user>=0.0 or user<=1.0:
#     if user>=0.9 or user <0.8:
#         print("Grade A")
#     elif user>=0.8 or user<0.7:
#         print("Grade B")
#     elif user>=0.7 or user<0.6:
#         print("Grade C")
#     elif user>=0.6 or user<0.6:
#         print("Grade D ")
#     elif user<0.6:
#         print("Grade F")


# user=int(input("enter the number  :"))
# a=user//2
# i=1
# while i<=a:
#     print(user)
#     i+=1


def x(nums):
    i=0
    k=1
    l=[]
    while i<len(nums):
        sum=nums[i]+k
        l.append(sum)
        i+=1
        k+=1
    print(l)
x([1,2,3,4])

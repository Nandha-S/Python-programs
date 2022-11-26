# a=["SH","DM","CL","HR"]
# b=["2","3","4","5","6","7","8","9"]
# list=[]
# for i in a:
#     for j in b:
#         list.append(i+j)
# print(list)
# print("enter any number bw 1 to 7")
# n=int(input())
# for i in range(1,7+1,2):
#     if i==1:
#         print("Sunday")
#     elif i==2:
#         print("Monday")
#     elif i==3:
#         print("Thuesday")
#     elif i==4:
#         print("Wenesday")
#     elif i==5:
#         print("Thursday")
#     elif i==6:
#         print("Friday")
#     elif i==7:
#         print("Saturday")
#     else:
#         print("Please enter valid number")
# filename: views.py (Django view functions)

k=int(input())
n=int(input())
a=[]
if k==2:
    num=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j%i==0:
                num+=1
    print(num)
            
# print(a)
# count=0
# for k in a:
#     if k[1]%k[0]==0:
#         count+=1
#         print(k)
# print(count)
    
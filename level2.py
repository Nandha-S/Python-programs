# from ast import And
# start=int(input("START:"))
# end=int(input("END:"))
# limit=int(input("LIMIT:"))
# sum=0
# n1=0
# n2=1
# list=[]
# for i in range(1,50):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     if start<=n3 and end>=n3:
#         print(n3)
#         list.append(n3)
# print(list)
# for i in list:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count==2:
#         print(i)
#         sum=sum+i
# print("sum:",sum)
# print(limit)
# if limit>sum:
#     print("yes")
# else:
#     print("no")
# for i in range(20,500):
#     count=0
#     for j in range(1,i+1):
#         if i %j==0:
#             count=count+1 
#     if count==2:
#         print(i,end=" ")   

string=str(input("enter the number randomly from 0 to 9:"))
find=str(input("enter the number:"))
a=0
b=0
for i in find:
    count=0
    for j in string:
        if i==j:
            a=abs(a-count)
            break
        else:
            count=count+1
    b=b+a
print(abs(b))

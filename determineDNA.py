from operator import index


l=['a','b','c','a']
# number=int(input())
# l1=[]
# l2=[]
# for i in range(number):
#     l1.append(input())
# for j in range(number):
#     l2.append(input())
# for i in l1:
#     print(i,end=" ")
# print()
# for i in l2:
#     print(i,end=" ")
from tkinter.tix import MAX


l1=['a','b','c','aa','d','b']
l2=[1,2,3,4,5,6]
x=zip(l1,l2)
lst=list(x)
print(lst)
first=1
last=5
list1=[]
list2=[]
for i in range(first,last+1):
    list1.append(l1[i])
print(list1)
for i in range(first,last+1):
    list2.append(l2[i])
print(list2)
max=[]
for i in list1:
    count=0
    for j in list1:
        if i==j:
            count+=1
    max.append(count)
print(max)
temp=[]
genes='caaab'
for i in range(len(genes)):
    for j in range(i+1,len(genes)):
        if genes[i]==genes[j]:
            n=genes[i]+genes[j]
            temp.append(n)
            break
        else:
            if i>1:
                temp.append(genes[j])
            else:
                temp.append(genes[i])
            break
print(temp)
final=[]
for i in range(len(temp)):
    count=0
    for j in range(len(list1)):
        if temp[i]==list1[j]:
            final.append(j)        
print(final)
sum=0
for i in final:
    sum=sum+list2[i]
print(sum)


    
            

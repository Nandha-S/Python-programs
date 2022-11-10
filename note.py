n=int(input())
list=[]
for i in range(n):
    str=input("enter string:")
    list.append(str)
list1=[]
for i in list:
    s=''
    for j in i:
        if j>='0'and j<='9' and j!='':
            s=s+j
    list1.append(s)
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]<list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
list2=[]
for i in list1:
    for j in list:
        for k in range(len(j)):
            if i[0]==j[k]:
                list2.append(j)
                break
for i in list2:
    print(i)
            
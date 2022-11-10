n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
b=[]
b=a
c=[]
for i in a:
    count=0
    for j in b:
        if  i==j:
            count+=1
            if count==2:
               c.append(i) 
        else:
            continue
c=len(c)//4
print(c)
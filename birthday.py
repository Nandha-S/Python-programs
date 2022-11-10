from itertools import count


k=int(input())
n=int(input())
a=[]
if n==2:
    for i in range(1,k+1):
        for j in range(1,k+1):
            a.append([i,j])
    print(a)
    count=0
    for k in a:
        if k[1]%k[0]==0:
            print(k)
            count+=1
    print(count)
else :
    for i in range(1,k+1):
        a.append([i])
        print(a)
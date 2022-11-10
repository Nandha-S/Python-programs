k=int(input())
if k%2==0:
    n=int(input())
    a=[]
    for i in range(k//2):
        n1=int(input())
        n2=int(input())
        a.append([n1,n2])
    print(a)
    count=0
    for i in a:
        if i[0]+i[1]<n:
            count+=2
        else:
            continue
    print(count)
else:
    print("enter the even number")
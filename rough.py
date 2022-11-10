n=int(input("enter the number:"))
size=2*n-1
start=0
end=size-1
a=[]
for i in range(size):
    list=[]
    for j in range(size):
        list.append(0)
    a.append(list) 
 
while n!=0:
    for i in range(start,end+1):
        for j in range(start,end+1):
            if (i==start or i==end or j==start or j==end):
              a[i][j]=n
    start+=1
    end-=1
    n-=1
for i in range(size):
    for j in range(size):
        print(a[i][j],end=" ")
    print()
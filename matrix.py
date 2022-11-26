r=int(input("enter the number of rows: "))
c=int(input("enter the number of columns: "))
a=[]
print("enter the elements of 1st matrix")
for i in range(r):
    list=[]
    for j in range(c):
        list.append(int(input()))
    a.append(list)
for i in range(r):
    for j in range(c):
        print(a[i][j],end=" ")
    print()
b=[]
print("enter the elements of 2nd matrix")
for i in range(r):
    list=[]
    for j in range(c):
        list.append(int(input()))
    b.append(list)
for i in range(r):
    for j in range(c):
        print(b[i][j],end=" ")
    print()
sum=[]
for i in range(r):
    list=[]
    for j in range(c):
        list.append(0)
    sum.append(list)
for i in range(r):
    for j in range(c):
        for k in range(r):
            sum[i][j]+=a[i][k]*b[k][j]
for i in range(r):
    for j in range(c):
        print(sum[i][j],end=" ")
    print()
print("-----insert the element in martix")
x=int(input("enter the element to insert: "))
y=int(input("enter the position: "))
z=int(input("enter the position: "))
for i in range(r):
    for j in range(c):
        sum[y][z]=x
        print(sum[i][j],end=" ")
    print()
print("--------search the element")
n1=int(input("enter the element to search: "))
if n1>0:
    for i in range(r):
        for j in range(c):
            if n1==sum[i][j]:
                print(i,j)
                break
else:
    print("invaild search")
n2=int(input("enter the element to search: "))
n3=int(input("enter the element to search: "))
print(sum[n2][n3])

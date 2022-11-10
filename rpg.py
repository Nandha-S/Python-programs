from cgi import print_environ


n=int(input("enter the number of monsters: "))
e=int(input("enter the experience: "))
p=[]
b=[]
a=[]
sum=0
for i in range(n):
    p.append(int(input()))
for j in range(n):
    b.append(int(input()))
for k in range(0,n):
    a.append([p[k],b[k]])
a.sort()
print(a)
for i in a:
    if i[0]>e:
        break
    else:
        e+=i[1]
        sum+=1
print(e)
print(sum)
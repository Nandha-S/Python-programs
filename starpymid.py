r=int(input())
c=int(input())
row=r*2
temp=row-1
c=0
while row>0 and c<temp:
    print(" "*row+"*"+"*"*c)
    row=row-1
    c=c+2
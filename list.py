n=5
for  i in range(1,n+1):
    for k in range(1,n-i):
        print(" ",end=" ")
        for j in range(1,n):
            if j==n-i+1:
                print(" *",end=" ")
        print()

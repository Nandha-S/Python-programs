a=[1,2,9,4,5]
b=[3,2,5]
for i in a:
    for j in b:
        if i==j:
            break
    else:
        print(i)
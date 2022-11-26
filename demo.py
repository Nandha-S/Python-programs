num=5
def square():
    for i in range(1,num+1):
        for i in range(num):
            print("*",end=" ")
        print(" ")
def rightangle():
    for i in range(1,num+1):
        for i in range(i):
            print("*",end=" ")
        print(" ")
def invertedright():
    for i in range(1,num+1):
        for i in range(i,num+1):
            print("*",end=" ")
        print(" ")

square()
rightangle()
invertedright()

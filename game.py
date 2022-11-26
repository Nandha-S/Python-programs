from ntpath import join
import random
from re import I, S
from tracemalloc import start


a=["SP,","CL,","HR,","DM,"]
b=["2","3","4","5","6","7","8","9"]
x=[]
for i in a:
    l=[]
    for j in b:
        l=i+j
        x.append(l)
print(x)
print("Shuffled deck:")
random.shuffle(x)
print(x)
sum=[]
for i in range(3):
    l=[]
    for j in range(3):
        l.append(random.choice(x))
    sum.append(l)
print("Wellcome to the game")
for i in range(3):
    for j in range(3):
        print(sum[i][j],end="|")
    print()
# n2=int(input("enter the element to search: "))
# n3=int(input("enter the element to search: "))
# print(sum[n2][n3])
for i in range(1,20+1):
    card=20-i
    score=i*-1
    
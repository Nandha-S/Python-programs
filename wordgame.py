from random import random
import random
def function(a):
    return a
print("nandhu,sathish,pravin")
list=['nandhu','sathish','pravin']
word=random.choice(list)
len=len(word)
print("_"*len)
guess=""
chance=12
while chance>0:
    print(" you have",chance,"chances")
    for i in range(len):
        letter=input("enter the char:")
        if letter==word[i]:
            guess+=letter
            print(guess+"_"*(len-(i+1)))
            if guess==word:
                print(word)
                chance=0
                break
        else:
            chance-=1
            print("you have",chance)
        
    
    
            
            
        

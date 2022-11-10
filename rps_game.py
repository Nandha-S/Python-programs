from secrets import choice
import random
print("lets play rock papper scissors!!!")
print("how many times you want to play?")
chance=int(input())
l=['r','p','s']
computer=0
user=0
while 1<=chance:
    print("enter rock for r, papper for p, scissors for s")
    guess=random.choice(l)
    choice=input()
    if choice=='r' and guess=='r':
        print("Draw")
    elif choice=='p' and guess=='r':
        print("you win")
        user+=1
    elif choice=='s' and guess=='r':
        print("computer win")
        computer=+1
    elif choice=='r' and guess=='p':
        print("computer win")
        computer+=1
    elif choice=='p' and guess=='p':
        print("draw")
    elif choice=='s' and guess=='p':
        print("you win")
        user+=1
    elif choice=='r' and guess=='s':
        print("you win")
        user+=1
    elif choice=='p' and guess=='s':
        print("computer win")
        computer+=1
    elif choice=='s' and guess=='s':
        print("Draw")
    chance-=1
print("Game finish")
print("Final score")
print("Your score is:",user)
print("Computer score is:",computer)


   
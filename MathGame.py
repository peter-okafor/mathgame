import random

Right=0
Wrong=0
TimeTaken=0
while TimeTaken<5:
    no1=random.randint(1,30)
    no2=random.randint(1,30)
    no3=no1+no2
    no1=str(no1)
    no2=str(no2)

    print('what is '+no1+'+'+no2)
    ans=input()
    ans=int(ans)

    if ans!=no3:
        print('olodo')
        Wrong=Wrong+1
        no3=str(no3)
        print('The answer is '+no3)
    if ans==no3:
        print('correct')
        Right=Right+1
    TimeTaken=TimeTaken+1

if Right==0:
    print('How much more dumb can you get? Mtchew!')

if Right==5:
    print('You are a GENIUS! You got it all RIGHT!')

if Right<5:
    Right=str(Right)
    Wrong=str(Wrong)
    print('You were right '+Right+' times')
    print('You were wrong '+Wrong+' times')

input()

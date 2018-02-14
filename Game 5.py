import random
import time
def cls():
    print('\n'*50)
characters=['A','A','B','B','C','C','D','D','E','E','F','F','G','G','H','H','I','I','J','J']
nums=['1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0']
nums1=['1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0']
N=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
n=0
turn=1
p1=0
p2=0
for i in range (0,20):
    index=random.randint(0,19)
    swap=characters[i]
    characters[i]=characters[index]
    characters[index]=swap
while n<10:
    for i in nums:
        print(i,end=' ')
    if turn%2==1:
        print('\nPlayer 1 - score ',p1,':')
    else:
        print('\nPlayer 2 - score ',p2,':')
    x=int(input())
    y=int(input())
    i=0
    while x>20 or x<1 or y>20 or y<1 or x==y or i<n:
        if x>20 or x<1 or y>20 or y<1:
            print('enter numbers between 1 and 20')
            x=int(input())
            y=int(input())
        elif x==y:
            print('enter two different numbers')
            x=int(input())
            y=int(input())
        elif N[i]==x or N[i+10]==x or N[i]==y or N[i+10]==y:
            print('these numbers is already sloved')
            x=int(input())
            y=int(input())
            i=0
        else:
            i+=1
    nums[x-1]=characters[x-1]
    nums[y-1]=characters[y-1]
    for i in nums:
        print(i,end=' ')
    if characters[x-1]==characters[y-1]:
        nums[x-1]='*'
        nums[y-1]='*'
        N[n]=x
        N[n+10]=y
        n+=1
        if turn%2==1:
            p1+=1
        else:
            p2+=1
    elif characters[x-1]!=characters[y-1]:
        nums[x-1]=nums1[x-1]
        nums[y-1]=nums1[y-1]
    turn+=1
    time.sleep(2)
    cls()
if p2<p1:
    print('Player 1 won with a score of ',p1)
elif p2>p1:
    print('Player 2 won with a score of ',p2)
elif p2==p1:
    print('Players draw')

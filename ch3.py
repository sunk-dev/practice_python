# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:19:41 2023

@author: jskre
"""

'''#05
x,y,z=eval(input('3개의 정수를 입력하시오'))


if(x>z):
    if(x>y):
        if(y>z):
            print(z)
        else:
            print(y)
    else:
        print(z)
else:
    if(z>y):
        if(y>x):
            print(x)
        else:
            print(y)
    else:
        print(x)

#eval()문자열로 있는 표현식을 실행해서 결과값을 받아오는 함수
a="1+3"
print(eval(a))
x=float(input('x값입력'))
fx=0
if x<=0:
    fx=x**2-9*x+2
else:
    fx=7*x+2
    
print(f'fx={fx}')
우물의깊이=30
날=1
올라간높이=0
하루에올라가는높이=7
밤에미끄러지는높이=5
while(True):
    if 우물의깊이<=올라간높이:
        break
    elif 날==1:
        올라간높이+=하루에올라가는높이 #day1은 하루에 7미터 오르고 바로 다음 2일로 넘어감
    else:
        올라간높이+=하루에올라가는높이#즉 잘때,day2부터 5미터 미끄러지고 다시 7미터 오름.
        올라간높이-=밤에미끄러지는높이
    print(f'day{날} 달팽이의 높이{올라간높이}')
    날+=1'''

'''n=int(input('n을 입력하시오'))
a = [[False for col in range(n)] for row in range(n)]
print(a)
k=1
for i in range(n):
    if((i+1)%2==1):
        for j in range(n):
            a[i][j]=k
            k+=1
    else:
        for j in range(n-1,-1,-1):
            a[i][j]=k
            k+=1
for list_row in a:
    for list_num in list_row:
        print(list_num,end=' ')
    print()'''
'''n=int(input('줄수'))

#finalstar=2*n-1

for i in range(1,n+1):
    print(' '*(n-i),'*'*(2*i-1))'''

import random as r
x,y,z=r.randint(1, 9)
luck=[x,y,z]
ax,ay,az=map(int,input('세 복권번호를 입력하시오').split(' '))
answer=[ax,ay,az]
lucknum=0
for i in answer:
    if i in luck:
        lucknum+=1
if lucknum==3:
    print(lucknum,'1억원')
elif lucknum==2:
    print(lucknum,'1천만원')
elif lucknum==1:
    print(lucknum,'1만원')
else:
    print(lucknum,'다음기회에')


    
    

  




    

    
    
    
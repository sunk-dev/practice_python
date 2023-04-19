# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:16:19 2023

@author: jskre
"""
#6
'''import math as m
print('각도',end="\t")
print('sin값',end="\t")
print('cos값')
for degree in range(10,90+1,10):
    r=3.14*degree/180.0
    Sin=m.sin(r)
    Cos=m.cos(r)
    print(degree,end='\t')
    print(Sin,end='\t')
    print(Cos,end='\t')
    print()'''

'''#8
n=0
while(n**2<500):
    n+=1

print(n)

#10
n=int(input('n의 값을 입력하시오'))
#a1 for문
result=0
for i in range(n+1):
    result+=i*i
print(f'계산값은{result}입니다')

#a2수식
result_1=n*(n+1)*(2*n+1)/6
print(f'계산값은{result_1}입니다')

#11
n1=int(input('첫번째 정수 값을 입력하시오'))
n2=int(input('두번째 정수 값을 입력하시오'))
n3= n1 if n1>n2 else n2
MAX_COMMON_DIVISOR=0
for i in range(1,n3):
    if n1%i==0 and n2%i==0:
        if i>MAX_COMMON_DIVISOR:
            MAX_COMMON_DIVISOR=i
        else:
            continue
    else:
        continue
print(f'{n1}과{n2}의 최대공약수는{MAX_COMMON_DIVISOR}')
'''
'''
#13 피보나치 수열

f1=0
f2=1
f3=0
n=int(input('몇번째 항까지 구할까요'))
print(f1,f2,end=' ')
for i in range(n-2):
    f3=f1+f2
    print(f3,end=' ')
    f1=f2
    f2=f3
    '''
'''
#14 2-20사이 소수

for i in range(2,20+1):#2-20까지
    b=0
    for j in range(2,i):
        if i%j==0:
            b=1
        else:continue
    if b==0:
        print(i,end=' ')
#15
result=0
for i in range(1,99+1,2):
    result+=(i)/(i+2)
print(result)
'''

'''
#16
n=int(input('게임판의 크기'))
width='---  '
height='|'
print(height,end='   ')
print(height)
total_line=2*n+1
for i in range(1,total_line+1):
    if i%2==1:#가로줄
        print(width*n)
    else:#세로줄
        for j in range(2):
            for j in range(n+1):
                print(height,end='   ')
            print()
            
        




            
    
    
#18
import turtle
import random as r

t=turtle.Turtle()
t.shape("turtle")

for i in range(10):
    x=r.randint(1,300)
    y=r.randint(1,300)
    rad=r.randint(1,300)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(rad)
    
turtle.exitonclick()
'''
'''
def display(mag='환영합니다',count=1):
    for i in range(count):
        print(mag)
display('hello',3)
'''
'''
import turtle
import random as r

t=turtle.Turtle()
t.shape("turtle")
n=int(input('몇각형을 그릴 것인가?'))
r=360/n
for i in range(n):
    t.fd(100)
    t.rt(r)
turtle.exitonclick() '''
'''def sub(a,b,c,d):
    print(a,b,c,d)
#sub(1,2,3,d=4)
#sub(a=1,2,3,4)
#sub(a=1,b=2,3,4)
sub(a=1,2,3,d=4)  '''

x=int(input())
if x<0:
    y=10
print(y)


    
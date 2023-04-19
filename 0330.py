# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:07:20 2023

@author: jskre
"""

'''country=input('배송국가').upper()
price=int(input('상품총가격'))
dilver_cost=0
if country=='KOREA':
    if price>=20000:
        dilver_cost=0
    else:
        dilver_cost=3000
elif country=='US':
    if price>=100000:
        dilver_cost=0
    else:
        dilver_cost=8000

print(f'상품가격{price}+배송비{dilver_cost}={price+dilver_cost}')


score=int(input('성적을 입력하세요'))
if score>=90:
    print('학점A')
if score>=80:
    print('학점B')
if score>=70:
    print('학점C')
if score>=60:
    print('학점D')


n=float(input('리히터 규모를 입력하시오'))
if n>=8.0 and n<=9.0:
    print('대부분의 구조물이 파괴됩니다') 
elif n>=7.0 and n<=7.9:
    print('지표면에 균열이 발생합니다') 
elif n>=4.0 and n<=6.9:
    print('빈약한 건물에 큰 피해가 있습니다') 
elif n>=2.0 and n<=3.9:
    print('물건들이 흔들리거나 떨어집니다')
else:
    print('지진계에 의해서만 탐지가능합니다')


import random as r
my=int(input('선택하시오 가위:1 바위:2 보:3'))
list=['가위','바위','보']
com=r.randint(1, 3)
  
if my==com:
    print('비겼습니다')
elif my==1:
    if com==2:
        print(f'나:{list[my-1]} 컴퓨터:{list[com-1]}-- 컴퓨터 승리')
    else:
        print(f'나:{list[my-1]} 컴퓨터:{list[com-1]}-- 본인 승리!')
elif my==2:
    if com==3:
        print(f'나:{list[my-1]} 컴퓨터:{list[com-1]}-- 컴퓨터 승리')
    else:
        print(f'나:{list[my-1]} 컴퓨터:{list[com-1]}-- 본인 승리!')
elif my==3:
    if com==1:
        print(f'나:{list[my-1]} 컴퓨터:{list[com-1]}-- 컴퓨터 승리')
    else:
        print(f'나:{list[my-1]} 컴퓨터:{list[com-1]}-- 본인 승리!')
else:
    print('잘못된 숫자를 입력하셨습니다')
'''
'''x,y,z=map(int,input('세개의 정수를 입력하시오').split(' '))
min_number=x
if x>y:
    if y>z:
        min_number=z
    else:
        min_number=y
elif y>z:
    if z>x:
        min_number=x
    else:
        min_number=z
elif z>y:
    if y>x:
        min_number=x
    else:
        min_number=y
print(min_number)'''

'''n=int(input('정수를 입력하시오'))
if n%3==0 and n%5==0:
    print('python Express')
elif n%3==0 and n%5!=0:
    print('python')
elif n%5==0 and n%3!=0:
    print('Express')
else:
    print('none')'''

'''weight=float(input('무게(킬로그램)'))
height=float(input('키(미터)'))
bmi=weight/(height**2)
print('당신의 bmi',bmi)
if bmi>=30.0:
    print('비만입니다')
elif bmi>=25.0:
    print('과체중입니다')
elif bmi>=20.0:
    print('정상입니다')'''
'''list=[]
list.append(1)
list.append(2)
list.append(8)
list[-1]=7
print(list)
print(list[2])
import random as r
number=r.randint(1, 100)
sum=0
while True:
    my_num=int(input('예측숫자'))
    sum+=1
    if my_num==number:
        print('정답! 시도 횟수:',sum)
        break;
    elif my_num>=number:
        print('원래숫자보다 커요')
    else:
        print('원래숫자보다 작아요')'''

'''for i in [9,8,7,6,5]:
    print('i=',i)'''
    
'''for i in range(2,20+1,2):
    print(i,end=' ')
print()
for i in range(20,0,-1):
    if i%2==0:
        print(i,end=' ')'''

'''n=int(input('숫자를 입력하시오'))
sum=0
for i in range(1,n+1):
    sum+=i

print(f'1부터 {n}까지의 합은 {sum}')'''

#n=int(input('숫자를 입력하시오'))
'''for i in range(2,n+1):
    print(f'----{i}단----')
    for j in range(1,9+1):
        print(f'{i}x{j}={i*j}')
    print('--------')

for i in range(1,9+1):
    for j in range(2,n+1):
        print(f'{j}x{i}={j*i}',end='\t')
    print()
    #end='\t'->사용시 좀더 넓고 깔끔한 띄어쓰기 가능.
    '''
'''result=1
result_1=1
for i in range(1,n+1):
    result*=i
print(result)
for i in range(n,0,-1):
    result_1*=i
print(result_1)
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''

n=int(input('입력'))
sum=0
list=list(map(int,input().split()))
fn=int(input('입력'))
for i in list:
    if i==fn:
        sum+=1
print(sum)
        
        


           
    
        
 